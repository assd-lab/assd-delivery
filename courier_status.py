from datetime import datetime

STATUSES = ["Прийнято", "В дорозі", "Доставлено"]


def update_status(order, new_status, proof_of_delivery=None):
    """Змінює статус доставки та зберігає час зміни (ASSD-9)."""
    if new_status not in STATUSES:
        raise ValueError("Невідомий статус доставки")
    if new_status == "Доставлено" and not proof_of_delivery:
        raise ValueError("Потрібне підтвердження вручення")
    order["status"] = new_status
    order["status_changed_at"] = datetime.now().isoformat()
    return order
