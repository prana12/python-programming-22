def search_by_time(filename: str, prep_time: int):
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
        item_duration = item[1][0]
        if item_duration <= prep_time:
            matched_recipe_output.append(f"{item[0]}, preparation time {item[1][0]} min")
        
        
    return matched_recipe_output

if __name__ == "__main__":
    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)