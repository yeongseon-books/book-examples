# 5_event.py
class OrderService:
    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    def place(self, payload):
        order = self.repo.save(payload)
        self.bus.publish("OrderPlaced", {"id": order.id})
        return order
