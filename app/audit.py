from flask import request

from app import db
from app.models import AccountEvent


def log_account_event(user, event_type: str) -> None:
    """Record a security-relevant event (login, reset, ...) for a user.

    Best-effort: request context (IP/user-agent) is only available inside a
    real request, which is always the case for the auth routes that call
    this.
    """
    event = AccountEvent(
        user_id=user.id,
        event_type=event_type,
        ip_address=request.remote_addr,
        user_agent=(request.user_agent.string or "")[:255],
    )
    db.session.add(event)
    db.session.commit()
