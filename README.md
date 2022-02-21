# OCM test case

OCM TestCase

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Тестовое задание

### Описание

  Необходимо реализовать backend приложения с минимальным фронтендом (можно голый html), который позволяет сохранить, просмотреть, отредактировать либо удалить сообщение и адрес электронной почты пользователя.

### Исходные данные
- дана ветка `task_1` в репозитории https://github.com/OCM-Expert/ocm_test_case
- необходимо сделать свою ветку от `task_1`, в качестве названия ветки принять свои имя и фамилию латиницей через нижнее подчеркивание `ivan_ivanov`
- установить pre-commit согласно документации cookiecutter
- прислать PR с решением задачи в Вашу ветку `ivan_ivanov`

### Чек-лист
Приложение позволяет:
- посмотреть полный список сообщений и email в интерфейсе веб приложения
- добавить сообщение вместе с email пользователя
- отфильтровать сообщения по email
- выбрать сообщение в качестве ссылки и попасть в форму, где можно отредактировать сообщение и сохранить
- удалить выбранное сообщение
- указанный выше функционал (CRUD) необходимо реализовать также в виде API используя DRF
- при смене локализации в настройках, подписи элементов интерфейса меняют свой язык

### Требования к реализации:
- Задание предполагает использование в качестве основы Django проекта сгенерированного с помощью Cookiecutter. https://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
- работу с сообщениями реализовать в интерфейсе пользователя, а не в стандартной админке Django
- реализовать авторизацию как по сессии Django так и по токену JWT для DRF
- использовать Class Based Views
- добавить модель в админку Django
- использование Django Forms
- валидация входящих данных
- написать тесты, должны быть зеленые, ORM не тестировать
- по возможности "толстые" модели и "тонкие" вьюхи
- процесс разработки должен быть отражен на github

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy ocm_test_case

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd ocm_test_case
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).
