meals = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
	},
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
	},
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
	},
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
	},
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
	},
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
	},
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
	}
]

combos = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    }
]

def preprocess_data(items):
    return {item["id"]: item for item in items}

meals_dict = preprocess_data(meals)
combos_dict = preprocess_data(combos)

def combo_calories_counter(combo_id):
    combo_meals = combos_dict.get(combo_id, {}).get("meals", [])
    combo_calories = calculate_calories(*combo_meals)
    return combo_calories

def calculate_calories(*meal_ids):
    total_calories = 0
    
    for meal_id in meal_ids:
        try:
            meal = meals_dict[meal_id]
            total_calories += meal["calories"]
            print(f"{meal['name']}: {meal['calories']} calories")
        except KeyError as e:
            print(f"{str(e)} is not on the menu")
    
    return total_calories

def calorie_counter(ordered_items_and_combos):
    total_calories = 0
    
    for item_or_combo_id in ordered_items_and_combos:
        try:
            if item_or_combo_id in combos_dict:
                combo_calories = combo_calories_counter(item_or_combo_id)
                total_calories += combo_calories
                print(f"{combos_dict[item_or_combo_id]['name']} Combo: {combo_calories} calories")
            elif item_or_combo_id in meals_dict:
                meal_calories = calculate_calories(item_or_combo_id)
                total_calories += meal_calories
                print(f"{meals_dict[item_or_combo_id]['name']}: {meal_calories} calories")
            else:
                raise KeyError(f"{item_or_combo_id} is not on the menu")
        except KeyError as e:
            print(str(e))
    
    return total_calories

# User input for ordered items and combos
user_order = input("Enter item and combo IDs separated by commas (e.g., meal-1, combo-1, meal-6): ").split(', ')

# Calculating and displaying calories for user order
print("\nCalculating calories for the ordered items and combos:")
result_user_order = calorie_counter(user_order)
print(f"\nTotal Calories for the order: {result_user_order} calories")
