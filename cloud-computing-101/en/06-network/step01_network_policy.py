from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    return {'ok': True, 'service': service, 'action': action, 'payload': payload}


def build_network_policy() -> dict[str, object]:
    return record('network', 'apply_policy', public_ingress_ports=[443], app_subnet_private=True, db_ingress_from='app-sg')
