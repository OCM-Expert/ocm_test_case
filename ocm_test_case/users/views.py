from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, FormView, ListView


from ocm_test_case.users.forms import UserEmailForm, UserEmailEditForm, UserEmailCreateForm
from ocm_test_case.users.models import UserEmails

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class UserEmailWriteView(LoginRequiredMixin, FormView):
    template_name = "users/write_message.html"
    form_class = UserEmailForm
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

    def get_form_kwargs(self):

        kwargs = super(UserEmailWriteView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


user_write_message_view = UserEmailWriteView.as_view()


class UserEmailSenSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "users/success_email.html"


user_success_message_view = UserEmailSenSuccessView.as_view()


class UserEmailListView(LoginRequiredMixin, ListView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/email_list.html"

    def get_queryset(self):
        username = self.kwargs['username']
        query = self.request.GET.get('q', '')
        return UserEmails.objects.filter(user_id__username=username, destination__icontains=query)

    def get_context_data(self, **kwargs):
        context = super(UserEmailListView, self).get_context_data(**kwargs)
        email_list = self.get_queryset()
        context.update({'emails_list': email_list})
        return context


user_email_list_view = UserEmailListView.as_view()


class UserEmailEditView(LoginRequiredMixin, FormView):

    template_name = "users/email_edit.html"
    form_class = UserEmailEditForm
    model = UserEmails
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id = User.objects.get(username=self.kwargs['username']).id
        self.object.user_id_id = id
        self.object.pk = self.kwargs['pk']
        self.object.save()

        return super().form_valid(form)

    def get_queryset(self):
        username = self.kwargs['username']
        pk = self.kwargs['pk']

        return get_object_or_404(UserEmails, pk=pk, user_id__username=username)

    def get_context_data(self, **kwargs):
        context = super(UserEmailEditView, self).get_context_data(**kwargs)
        email = self.get_queryset()
        form = UserEmailEditForm(initial={
            'destination': email.destination,
            'mes_title': email.mes_title,
            'mes_text': email.mes_text,
            'status': email.status,
        })
        context.update({'email': email, 'form': form})
        return context


user_email_edit_view = UserEmailEditView.as_view()


class UserEmailCreateView(LoginRequiredMixin, FormView):
    template_name = "users/email_create.html"
    form_class = UserEmailCreateForm
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

    def get_form_kwargs(self):

        kwargs = super(UserEmailCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


user_email_create_view = UserEmailCreateView.as_view()
