import os
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
class Recipiebook:
    filename = 'recipe.txt'
    def __init__(self):
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()
    def add_recipe(self, recipe):

       
        with open(self.filename, 'a') as file: 
            file.write(f'{recipe.name}|{ingredients}|{recipe.instructions}\n')
        print('Recipe added successfully')
    def show_recipes(self):
        with open(self.filename, 'r') as file:
            recipes = file.readlines()
            if not recipes:
                print('No recipes found')
                return
            print('\n--- Recipes ---')
            for line in recipes:
                line = line.strip()
                if not line:
                    continue
                name, ingredients, instructions = line.split('|')
                print(f'{name}\nIngredients: {ingredients}\nInstructions: {instructions}\n')
    def search(self, name):
        with open(self.filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                r_name, ingredients, instructions = line.split('|')
                if r_name.lower() == name.lower():
                    print(f'Recipe found!\n{r_name}\nIngredients: {ingredients}\nInstructions: {instructions}')
                    return
        print('Recipe not found')
    def delete(self, name):
        with open(self.filename, 'r') as file:
            recipes = file.readlines()
        found = False
        with open(self.filename, 'w') as file:
            for line in recipes:
                line = line.strip()
                if not line:
                    continue
                r_name, _, _ = line.split('|')
                if r_name.lower() != name.lower():
                    file.write(line + '\n')
                else:
                    found = True
        if found:
            print('Recipe deleted')
        else:
            print('Recipe not found')

book = Recipiebook()
while True:
    print("\nRecipe Book Menu:")
    print("1. Add Recipe")
    print("2. Show Recipes")
    print("3. Search Recipe")
    print("4. Delete Recipe")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ").split(',')
        instructions = input("Enter instructions: ")
        recipe = Recipe(name, ingredients, instructions)
        book.add_recipe(recipe)

    elif choice == '2':
        book.show_recipes()

    elif choice == '3':
        name = input("Enter recipe name to search: ")
        book.search(name)

    elif choice == '4':
        name = input("Enter recipe name to delete: ")
        book.delete(name)

    elif choice == '5':
        break

    else:
        print("Invalid choice")