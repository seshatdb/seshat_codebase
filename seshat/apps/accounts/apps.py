from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seshat.apps.accounts'

    ######EMAIL_CONFIRMATION_BRANCH
    # def ready(self):
    #     import seshat.apps.accounts.signals