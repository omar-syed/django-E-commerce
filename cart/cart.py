from decimal import Decimal
from django.conf import settings
from product.models import Product

class Cart(object):
    
    """
        Initialize the cart.
    """

    def __init__(self,request):
        
        self.session = request.session # to store the current session 
        cart         = self.session.get(settings.CART_SESSION_ID) # try to get the current session 

        if not cart :
            
            cart     = self.session[settings.CART_SESSION_ID] = {} # save an empty cart in session
        
        self.cart = cart
            

    def add(self,product,quantity=1,override_quantity=False):

        """
            Add a product to the cart or update its quantity.
        """

        product_id = str(product.id) # because Django use JSON to seralize session data and JSON allow only string key name
        
        if product_id not in self.cart :
            self.cart[product_id] = {'quantity':0,'price':str(product.PRDPrice)}

        
        if override_quantity :
            self.cart[product_id]['quantity'] = quantity

        
        else :
            self.cart[product_id]['quantity'] += quantity
        
        self.save()

    
    def save(self):
        self.session.modified = True # mark the session as "modified" to make sure it gets saved

    
    def remove(self,product):
        """
            Remove a product from the cart.
        """

        product_id =  str(product.id)

        if product_id in self.cart :
            del self.cart[product_id]
            self.save()

    
    def __iter__(self):

        """
            Iterate over the items in the cart and get the products from the database.
        """

        product_ids = self.cart.keys()
        # get the products objects and add them to the cart 
        products    = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products :
            cart[str(product.id)]['product'] = product

        
        for item in cart.values():
            item['price']    = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):

        """
            Count all items in the cart.
        """

        return sum(item['quantity'] for item in self.cart.values())



    def get_total_price(self):
        
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())



    def clear(self):

        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()