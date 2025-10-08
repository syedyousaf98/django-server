from django.core.mail import send_mail
from django.conf import settings


def send_activation_mail(recipient, subject, html_content):
    try:
        print(recipient)
        send_mail(
            subject=subject,
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            html_message=html_content,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return str(e)