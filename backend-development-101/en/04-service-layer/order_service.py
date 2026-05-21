# services/order_service.py
class OrderService:
    def __init__(self, repo, mailer):
        self.repo = repo
        self.mailer = mailer

    def create(self, payload):
        if payload.amount <= 0:
            raise ValueError("amount must be > 0")
        order = self.repo.save(payload)
        self.mailer.send(payload.email, "ordered")
        return order

# routers/orders.py
@router.post("")
def create_order(payload, svc: OrderService = Depends(get_order_service)):
    return svc.create(payload)
