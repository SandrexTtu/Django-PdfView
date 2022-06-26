import datetime
from django.contrib.auth.signals import user_logged_in , user_logged_out , user_login_failed
from django.dispatch import receiver
from pkg_resources import require
import logging

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logging.info('user {} logged in through page {}'.format(user.username, request.META.get('HTTP_REFERER')))

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    logging.info('user {} logged in failed through page {}'.format(credentials.get('username'), request.META.get('HTTP_REFERER')))


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logging.info('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))


