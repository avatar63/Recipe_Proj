import spoonacular as sp



class recipe_parser:
    api=''
    def __init__(self, spoonacular_key):
        self.spoonacular_key = spoonacular_key
        self.api = sp.API(spoonacular_key)
        
    def recipes_search(self,ingredients):
        data_dict = self.api.search_recipes_by_ingredients(ingredients).json()
        #NOTE ingredients is a string data type with ingredients listed as csv.
        #Returns a dictionary containing id,title,image,usedIngredientCount, missedIngredientCount,missedIngredientCount,missedIngredients,usedIngredients,unusedIngredients,likes
        return data_dict
    
    def recipe_instruction(self,dish_id):
        dish_data = self.api.get_recipe_information(dish_id).json()
        #dish_data has the following keys: # vegetarian vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular, sustainable, lowFodmap, weightWatcherSmartPoints, gaps, preparationMinutes, cookingMinutes, aggregateLikes, healthScore, creditsText, license, sourceName, pricePerServing, extendedIngredients, id, title, readyInMinutes, servings, sourceUrl, image, imageType, summary, cuisines, dishTypes, diets, occasions, winePairing, instructions, analyzedInstructions, originalId, spoonacularSourceUrl
        return dish_data["analyzedInstructions"]

ob = recipe_parser("fbb7be320f9842a9ad38be90a1e8e288")

k= ob.recipe_instruction("716429")

# print(k)

for i in k:
    print(i)