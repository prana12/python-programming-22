def search_by_name(filename: str, word: str):
    recipes = {}
    matched_recipe_names = []
    
    with open(filename) as new_file:
        text = ""

        for line in new_file:
            text += f"{line}"
            
        parts = text.split("\n\n")
        for item in parts:
            recipe = item.split("\n")
            
            name = recipe[0]
            preparation_time = recipe[1]
            ingredients = []
            for ingredient in recipe[2:]:
                ingredients.append(ingredient)
            
            recipes[name] = (preparation_time, ingredients) 

    for item in recipes.items():
        item_name = item[0].lower()
        index = item_name.find(word.lower())
        if index >= 0:
            matched_recipe_names.append(item[0])
        
    return matched_recipe_names

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)