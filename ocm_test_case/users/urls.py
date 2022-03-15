from django.urls import path

from ocm_test_case.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_write_message_view,
    user_success_message_view,
    user_email_list_view,
    user_email_edit_view,
    user_email_create_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("write_message/", view=user_write_message_view, name="write_message"),
    path("success/", view=user_success_message_view, name="success"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("<str:username>/email-list", view=user_email_list_view, name="email_list"),
    path("<str:username>/email-edit/<int:pk>", view=user_email_edit_view, name="email_edit"),
    path("<str:username>/email-create", view=user_email_create_view, name="email_create"),
]
