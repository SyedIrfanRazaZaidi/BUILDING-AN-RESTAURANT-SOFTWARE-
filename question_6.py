class restaurant :
    print("==================================================================")
    
        
    menu_items = [
        "BIRYANI",
        "KARAHI",
        "KABAB",
        "ROLL",
        "BURGER",
        "CHICKEN BROAST",
        "FISH FRY",
        "CHICKEN FRY",
        "CHICKEN TIKKA",
        "CHICKEN WINGS",
        "CHICKEN NUGGETS",
        "CHICKEN PIZZA",
        "CHICKEN PASTA",
        "CHICKEN SALAD",
        "CHICKEN SOUP",
        "CHICKEN SANDWICH",
        "CHICKEN WINGS",
        "CHICKEN STRIPS",
        "CHICKEN FRIES",
        "CHICKEN BURGER",
        "CHICKEN NUGGETS",
        "CHICKEN TIKKA BONELESS",
        "CHICKEN TIKKA BONE",
        "BEEF MANDI",
        "BEEF TIKKA BONELESS",
        
        
        
    ]  
    print("                    MENU    ")
    print("                                  ")
    print("ITEMS ARE ",menu_items)
    print("=================================================================")
        
    def add_item(self,item):
        self.menu_items.append(item)
        print(f"{item} HAS BEEN ADDED TO THE MENU :")
        print(f"Updated Menu Is : {self.menu_items}")
        
        # Define a list to keep track of booked tables
    booked_tables = []

    def book_table(self):
        while True :
            
            t = int(input("ENTER TABLE NO. YOU WANT TO BOOK: "))
            if t in self.booked_tables:
                print("TABLE IS RESERVED , SELECT ANOTHER PLEASE !")
            else:
                self.booked_tables.append(t)
                print(f"TABLE NO. {t} HAS BEEN BOOKED FOR YOU :")
                break
            
   
      
    def take_order(self):
        num_items = int(input("HOW MANY ITEMS WOULD YOU LIKE TO ORDER? ( READ CAREFULLY ) : "))
        self.b = 0
        self.customer_order = []
            
        for i in range(num_items):
            item = input("ENTER YOUR ORDER PLEASE : ")
            if item in self.menu_items:
                self.customer_order.append(item)
                self.b += 1
            else:
                print("SORRY, ORDER IS NOT AVAILABLE !")
            
            print("YOUR ORDER HAS BEEN TAKEN !")
            print(f"YOUR ORDER: {self.customer_order}")     
                
                
    def bill(self):
        
        print(f"YOUR BILL FOR {self.b} ITEMS IS RS. {self.b*300}")
            
# LETS CREATE OBJECTS FOR RESTAURANT (CUSTOMER 1):
    
r1 = restaurant() 
r1.book_table()
r1.take_order()
r1.bill()
print("-------------------------------------------------------------------------------------------------------------")        
# LETS CREATE ANOTHER OBJECT HERE I AM GOING TO ADD ITEM 
r3 = restaurant()
r3.add_item("PIZZA")    # ITEM SHOULD BE IN UPPERCASE FOR SIMILAR LOOKING LIKE(BIRYANI , FISH FRY)

print("-------------------------------------------------------------------------------------------------------------")
# NOW CREATE SECOND OBJECT (CUSTOMER 2)
r2 = restaurant()
r2.book_table()
r2.take_order()
r2.bill()        
        
        
      
      
