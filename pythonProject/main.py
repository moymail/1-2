cook_book = {}

with open('recipes.txt') as file:
    for recipe in file:
        recipes = recipe.strip()
        ingredients = int(file.readline())
        recipes_list = []
        for ingredient in range(ingredients):
            ingredient_name, quantity, measure = file.readline().split('|')
            recipes_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[recipes] = recipes_list
        file.readline()
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            print('Такого блюда в книге нет!')
            return
    for key, values in cook_book.items():
        if dish in key:
            ingredients_dict = {}
            for value in values:
                shop_dict_ingredient = value['ingredient_name']
                if shop_dict_ingredient not in shop_dict.keys():
                    shop_dict[shop_dict_ingredient] = {}
                    ingredients_dict['quantity'] = int(value['quantity']) * person_count
                    ingredients_dict['measure'] = value['measure']
                    shop_dict[shop_dict_ingredient] = ingredients_dict
                else:
                    new_quantity = ingredients_dict['quantity'] + int(value['quantity'] * person_count)
                    ingredients_dict['quantity'] = new_quantity
    print(shop_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)