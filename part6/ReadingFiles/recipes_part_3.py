def search_by_ingredient(filename: str, search_ingredient: str):
    recipes = {}
    matched_recipe_output = []
    
    with open(filename) as new_file:
        text = ""

        for line in new_file:
            text += f"{line}"

        parts = text.split("\n\n")
        for item in parts:
            recipe = item.split("\n")
            name = recipe[0]
            preparation_time = int(recipe[1])
            ingredients = []
            for ingredient in recipe[2:]:
                ingredients.append(ingredient)
            recipes[name] = (preparation_time, ingredients)
            
    for item in recipes.items():
        item_ingredients = item[1][1]
        if search_ingredient in item_ingredients:
            matched_recipe_output.append(f"{item[0]}, preparation time {item[1][0]} min")
            
    return matched_recipe_output

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)