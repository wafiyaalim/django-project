from celery import shared_task

@shared_task
def send_email_task(email):
    print(f"Sending welcome email to {email}")
    # Here you could use send_mail for actual emails