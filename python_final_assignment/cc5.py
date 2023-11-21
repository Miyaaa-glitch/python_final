from food_calories_complex import combos_complex, meals_complex

#function for calculating price of a meal or a combo

def price_counter(ordered_meal_name, meals_list, combos_list):
    total_price = 0
    
    # Check if the ordered meal is a single meal
    single_meal = next((meal for meal in meals_list if meal["name"].lower() == ordered_meal_name.lower()), None)
    
    if single_meal:
        total_price += single_meal["price"]
       
    else:
        # Check if the ordered meal is a combo
        combo = next((combo for combo in combos_list if combo["name"].lower() == ordered_meal_name.lower()), None)

        if combo:
            total_price = combo["price"]
    return total_price

def show_task5(ordered_meal):
    total_price = price_counter(ordered_meal, meals_complex, combos_complex)
    print(f'Total price for {ordered_meal}: {total_price}')