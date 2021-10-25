

secret_key = "cart"
class Cart(object):
    def __init__(self,request,db):
        self.session = request.session
        self.db = db
        cart = self.session.get(secret_key)

        if not cart:
            cart = self.session[secret_key] = {}

        self.cart = cart

    def add(self,product,quantity=1,update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart['product_id']

    def remove_all(self):
        product_ids = 

