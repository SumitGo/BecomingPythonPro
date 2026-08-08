# Ecommerce management System

store = {
    'tv': [200000, 20],
    'mobile': [65000, 4],
    'vr headset': [250000, 2]

}

class ecom:
    def __init__(self, store, customer_name, customer_mobile, customer_email):
        self.store = store
        self.customer_name = customer_name
        self.customer_mobile = customer_mobile
        self.customer_email = customer_email
        self.cart = []
    
    def order_procducts(self, *products):
        unavailable_products = []
        for i in products:
            if i in self.store and self.store[i][1] > 0:
                self.cart += [i]
            else:
                unavailable_products +=[i]
        # print("order booked for these products: ", self.cart)
        return self.cart, unavailable_products
    
    def payment(self):
        self.total_price = 0
        for i in self.cart:
            store[i][1] -= 1
            self.total_price += store[i][0]

        return self.total_price
    
    def discount(self):
        super_coins = (self.total_price // 1000) * 200
        total_discount = super_coins / 4
        return total_discount
    
    def final_price(self):
        return self.total_price - self.discount()

nandu = ecom(store, "Nandu", 9883759384, "nandu@mail.com")
cart, unordered = nandu.order_procducts('tv', 'fridge', 'mobile') 
total_price = nandu.payment()
discount = nandu.discount()
final_price = nandu.final_price()


print(cart, unordered,sep="\n")
print("Total price: ",total_price)
print("Discount: ",discount)

print("Final price: ",final_price)
