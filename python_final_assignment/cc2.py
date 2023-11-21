combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

def combo_calories_counter(combo_name):
    combo_meals = combos.get(combo_name, [])
    combo_calories = calculate_calories(*combo_meals)
    return combo_calories

def calculate_calories(*meals):
    total_calories = 0
    
    for meal in meals:
        if meal in calories:
            total_calories += calories[meal]
            print(f"{meal}: {calories[meal]} calories")
        else:
            print(f"{meal} not found in the calories dictionary.")
    
    return total_calories

def calorie_counter(ordered_items_and_combos):
    total_calories = 0
    
    for item in ordered_items_and_combos:
        if item in combos:
            combo_calories = combo_calories_counter(item)
            total_calories += combo_calories
            print(f"{item} Combo: {combo_calories} calories")
        elif item in calories:
            total_calories += calories[item]
            print(f"{item}: {calories[item]} calories")
        else:
            print(f"{item} not found in the calories or combos dictionary.")
    
    return total_calories

# User input for ordered items and combos
user_order = input("Enter items and combos separated by commas (e.g., Hamburger, Cheesy Combo, Salad): ").split(', ')

# Calculating and displaying calories for user order
print("\nCalculating calories for the ordered items and combos:")
result_user_order = calorie_counter(user_order)
print(f"\nTotal Calories for the order: {result_user_order} calories")
