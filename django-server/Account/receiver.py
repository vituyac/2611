from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver

@receiver(reset_password_token_created)
def password_reser_token_created(reset_password_token, *args, **kwargs):
    sitelink = "http://localhost:8000/"
    token = "&token={}".format(reset_password_token.key)
    ful_link = str(sitelink)+str("password-reset")+str(token)
    
    full_link = ful_link,
    recipient_email = reset_password_token.user.email
    
    sender_email = "kisterev-volgait24@yandex.ru"
    subject = "Запрос на сброс пароля"
    message = f"Token: {reset_password_token.key}"
    send_mail(subject, message, sender_email, [recipient_email])