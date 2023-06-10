from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name,set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    for i in drink_ingredients:
        if i in ALCOHOLS:
            return drink_name+' Cocktail'
    return drink_name+' Mocktail'

def categorize_dish(dish_name, dish_ingredients):
    if set(dish_ingredients).issubset(VEGAN):
        return dish_name + ': VEGAN'
    elif set(dish_ingredients).issubset(VEGETARIAN):
        return dish_name + ': VEGETARIAN'
    elif set(dish_ingredients).issubset(PALEO):
        return dish_name + ': PALEO'
    elif set(dish_ingredients).issubset(KETO):
        return dish_name + ': KETO' 
    elif set(dish_ingredients).issubset(OMNIVORE):
        return dish_name + ': OMNIVORE'

def tag_special_ingredients(dish):
    x,y=dish
    return (x,set(y).intersection(SPECIAL_INGREDIENTS))

def compile_ingredients(dishes):
    ingredients=set().union(*dishes)
    return ingredients

def separate_appetizers(dishes, appetizers):
    return list(set(dishes)-set(appetizers))

def singleton_ingredients(dishes, intersection):
    singletons = (dish - intersection for dish in dishes)
    return set.union(*singletons)
    
