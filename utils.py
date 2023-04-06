import logging
from typing import Any, Dict
from app.crud.users import user
from app.db.session import SessionLocal

import emails

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_email(
    email_to: str,
    subject: str = "",
    body: str = "",
    environment: Dict[str, Any] = {},
) -> None:
    assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.Message(
        subject=subject,
        text=body,
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS:
        smtp_options["tls"] = True
    if settings.SMTP_USER:
        smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD:
        smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"send email result: {response}")


def send_test_email(email_to: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    body = "Test email"
    send_email(
        email_to=email_to,
        subject=subject,
        body=body,
        environment={"project_name": settings.PROJECT_NAME, "email": email_to},
    )


def send_product_updated_email(product_sku: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    body = f"The Product with SKU {product_sku} has been modified"
    db = SessionLocal()
    email_to = user.get_superusers_emails(db)
    send_email(
        email_to=email_to,
        subject=subject,
        body=body,
        environment={"project_name": settings.PROJECT_NAME, "email": email_to},
    )
