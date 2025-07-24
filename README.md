# BUILDING-AN-RESTAURANT-SOFTWARE-
I just create a software for making digital restaurant in python by using object oriented programming concepts, It covers majority of problems that face by owner or restaurant staff, I highly recommend everyone to check it out. 

# 🍽️ Restaurant Management System

This Python project implements a **Restaurant Management System** with features such as menu display, table booking, order taking, and bill generation. The program runs in the console and provides a simple interactive interface for basic restaurant operations.

---

## Features

- **Menu Display**:
  - Shows a full list of available food items upon launching the program.
  - Items include local and fast food varieties (Biryani, Karahi, Burger, Pizza, etc.).

- **Add New Item to Menu**:
  - Staff can add new food items dynamically during runtime.

- **Table Booking**:
  - Customers can book a table.
  - Prevents duplicate booking of the same table number.

- **Take Order**:
  - Customers can place orders by selecting multiple items.
  - Items are validated against the menu.
  - Invalid or unavailable items are handled gracefully.

- **Bill Generation**:
  - Bill is calculated based on the number of valid items ordered.
  - Fixed price per item: Rs. 300.

---

## How It Works

1. **Menu Display**:
   - Automatically shown when the program starts.

2. **Table Booking**:
   - Users enter a table number to reserve.
   - If already booked, user is prompted to enter a different table number.

3. **Take Order**:
   - Users enter the number of items they wish to order.
   - Items are validated against the menu and added to the order list.
   - Invalid entries are rejected with a message.

4. **Bill**:
   - The system calculates the total bill using the formula:  
     `Total = Number of valid items × Rs. 300`



## Files Used

- `restaurant.py`: Main Python script containing the `Restaurant` class and object-based usage.



## Sample Menu Items

[
"BIRYANI", "KARAHI", "KABAB", "ROLL", "BURGER",
"CHICKEN BROAST", "FISH FRY", "CHICKEN TIKKA",
"CHICKEN PIZZA", "CHICKEN PASTA", "CHICKEN SOUP",
"CHICKEN WINGS", "CHICKEN NUGGETS", "BEEF MANDI", "BEEF TIKKA BONELESS"
]


> *Note: Menu items should be entered in **UPPERCASE** when placing orders.*



## Technologies Used

 **Python Standard Library**

No external packages or frameworks are required.


## Sample Bill Format

YOUR ORDER HAS BEEN TAKEN!
YOUR ORDER: ['BIRYANI', 'CHICKEN PIZZA', 'FISH FRY']
YOUR BILL FOR 3 ITEMS IS RS. 900


## Notes

- Menu is printed automatically when the class is initialized.
- `add_item()` method allows live modification of the menu.
- Table booking list is shared among all instances, preventing duplicate table reservations.


## License

This project is created for educational purposes and can be freely used, modified, or extended.

