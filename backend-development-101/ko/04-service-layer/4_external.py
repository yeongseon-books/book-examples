# 4_external.py
class CheckoutService:
    def __init__(self, repo, payment_gw):
        self.repo = repo
        self.gw = payment_gw

    def checkout(self, cart):
        receipt = self.gw.charge(cart.total)
        return self.repo.save_order(cart, receipt.id)
