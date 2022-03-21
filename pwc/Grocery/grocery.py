class Store():
    def __init__(self):
        self.cart = {}
        self.items =  {'soup': 0.65, 'bread': 0.80, 'milk': 1.3, 'apple': 1}
    
    def takeInput(self):
        key = input("Enter the item you want to buy: \n")
        value = input("Enter the quantity: \n")
        
        if key not in self.items:
            print ("Item not found.  Did you enter the correct item?")
        
        self.addToCart(key, int(value))
        loop = str(input('wanna add more items to the shopping cart?(yes or no)'))
        
        if loop == 'yes':
            self.takeInput()
        else:   
            self.checkout()

    def welcome(self):
        items = {'soup': '65p/tin', 'bread': '80p/loaf', 'milk': '£1.3/bottle', 'apple': '£1/piece'}
        print("Items we have on the store:")
        for key, value in items.items():
            print(key, ' : ', value)
        print("\nThis weeks discounts:")
        print("Apples have 10% off")
        print("Buy 2 tins of soup and get a loaf of bread for half price\n")
        
        self.takeInput()
        
    
    def addToCart(self, item, qty):
        if item in self.cart:
            self.cart[item]+=qty
        else:
            self.cart[item] = qty
    

    def getItemPrice(self, itemName):
        return self.items[itemName]
    

    # before discounts
    def getSubTotal(self):
        subtotal = 0
        for key,value in self.cart.items():
            subtotal += self.getItemPrice(key) * value
        return subtotal
    

    def getDiscount(self):
        # soup and bread
        discount = 0
        if 'soup' in self.cart and 'bread' in self.cart and self.cart['soup'] >= 2:
            breadPrice = self.getItemPrice('bread')
                  
            totalSoups = self.cart['soup']
            
            totalBreads = self.cart['bread']
            
            breadDiscountsAvailable = totalSoups//2
            
            
            for i in range (0,totalBreads):
                if (breadDiscountsAvailable > 0):
                    discount += breadPrice * 0.5
                else:
                    break
        
        # apple
        if 'apple' in self.cart:
            applePrice = self.getItemPrice('apple')
            
            totalApplePrice = self.cart['apple'] * applePrice
            
            discount += totalApplePrice * 0.10

        return discount
    

    def getTotal(self):
        subtotal = self.getSubTotal()
        discount = self.getDiscount()
        return subtotal - discount


    def checkout(self):
        subtotal = self.getSubTotal()
        discount = self.getDiscount()
        total = round(self.getTotal(),2)
        print("")
        print (f'Subtotal: £ {round(subtotal,2)}')
        if discount == 0:
            print("No available discounts")
        else:
            print (f'Discounts: £ {discount}')
        print ('---------------------')
        print (f"Total: £ {total:.2f}")
        print ('---------------------')
        print ("Thank you for shopping with us.")



if __name__ == '__main__':
    store = Store()
    store.welcome()
