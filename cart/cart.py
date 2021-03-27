from decimal import Decimal
from django.conf import settings
from product.models import Product

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_slug = product.PRDSLug
        if product_slug not in self.cart:
            self.cart[product_slug] = {'quantity': 0,'price': str(product.PRDPrice)}
  
        if override_quantity:
            self.cart[product_slug]['quantity'] = quantity    
        else:
            self.cart[product_slug]['quantity'] += quantity

        self.save()    

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        #Remove a product from the cart.
        product_slug = product.PRDSLug
        if product_slug in self.cart:
            del self.cart[product_slug]
            self.save()
            