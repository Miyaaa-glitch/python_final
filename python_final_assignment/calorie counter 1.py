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

def calculate_calories(*meals):
    total_calories = 0
    
    for meal in meals:
        if meal in calories:
            total_calories += calories[meal]
            print(f"{meal}: {calories[meal]} calories")
        else:
            print(f"{meal} not found in the calories dictionary.")
    
    return total_calories

# User input for meals
user_meals = input("Enter meals separated by commas (e.g., Hamburger, Salad, Lemonade): ").split(', ')

# Calculating and displaying calories for user input
print("\nCalculating calories for the inputted meals:")
result_user_input = calculate_calories(*user_meals)
print(f"\nTotal Calories for the inputted meals: {result_user_input} calories")
