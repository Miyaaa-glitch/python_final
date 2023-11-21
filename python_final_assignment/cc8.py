from food_calories_complex import combos_complex, meals_complex
from datetime import datetime

class Order:
    counter = 0

    #initialization with constructors
    def __init__(self, items, date=None):
        Order.counter += 1
        self.order_id = f"order-{Order.counter}"
        self.order_accepted = False
        self.order_refused_reason = ""
        self.date = date or datetime.now()
        self.items = items

    #property for calorie counting 
    @property
    def calories(self):
        total_calories = 0
        for item_id in self.items:
            item = next((meal for meal in meals_complex if meal["id"] == item_id), None)
            if item:
                total_calories += item["calories"]
            else:
                # Unknown item, refuse the order
                self.order_refused_reason = f"Unknown item id: {item_id}"
                return 0

        return total_calories

    #property for price calculation
    @property
    def price(self):
        total_price = 0
        for item_id in self.items:
            item = next((meal for meal in meals_complex if meal["id"] == item_id), None)
            if item:
                total_price += item["price"]
            else:
                # Unknown item, refuse the order
                self.order_refused_reason = f"Unknown item id: {item_id}"
                return 0

        return total_price

# Example usage:
def show_task8(given_order):
    order = Order(given_order)
    print(f"Order ID: {order.order_id}")
    print(f"Order Calories: {order.calories}")
    print(f"Order Price: {order.price}")
    print(f"Order Date: {order.date}")