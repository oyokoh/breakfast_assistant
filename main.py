# Breakfast ingredients

eggs = 2
bread = 4
cooking_oil = 4
salt = 0.25


# Required ingredients

required_ingredients = [
    "Eggs",
    "Bread",
    "Cooking oil",
    "Salt"
]


# Available ingredients

available_ingredients = [
    "Eggs",
    "Bread",
    "Cooking oil",
    "Salt"
]


# Required equipment

required_equipment = [
    "Frying pan",
    "Spatula",
    "Plate",
    "Stove",
    "Egg bowl"
]


# Available equipment

available_equipment = [
    "Frying pan",
    "Spatula",
    "Plate",
    "Stove",
    "Egg bowl"
]


# Display ingredients

print("\n=== Breakfast Ingredients ===")
print("Eggs:", eggs)
print("Bread slices:", bread)
print("Cooking oil:", cooking_oil, "teaspoons")
print("Salt:", salt, "teaspoon")


# Check ingredients

print("\n=== Ingredient Availability ===")

ingredients_ready = True

for item in required_ingredients:
    if item not in available_ingredients:
        print(item, "is missing.")
        ingredients_ready = False
    else:
        print(item, "is available.")


# Check equipment

print("\n=== Equipment Availability ===")

equipment_ready = True

for item in required_equipment:
    if item not in available_equipment:
        print(item, "is missing.")
        equipment_ready = False
    else:
        print(item, "is available.")



if equipment_ready and ingredients_ready:
    print("\nEverything is ready. Start cooking.")

    print("\n=== Cooking Instructions ===")
    print("1. Wash your hands.")
    print("2. Crack the eggs into the egg bowl.")
    print("3. Add salt and mix.")
    print("4. Put cooking oil into the frying pan.")
    print("5. Turn on the stove.")
    print("6. Add the eggs to the pan.")
    print("7. Cook until the eggs are properly set.")
    print("8. Toast the bread.")
    print("9. Serve the eggs and bread on a clean plate.")
    print("10. Turn off the stove.")

else:
    print("\nCannot start cooking. Check the missing items above.")    