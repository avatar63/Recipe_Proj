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
        return data_dict #a list of dictionaries
    def dish_id(self,data_dict):
        id_list=[]
        for i in data_dict:
            id_list.append(i["id"])
        return id_list #a list of ids
    def recipeinformation(self,dish_id):
        dish_data = self.api.get_recipe_information(dish_id).json()
        #dish_data has the following keys: # vegetarian vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular, sustainable, lowFodmap, weightWatcherSmartPoints, gaps, preparationMinutes, cookingMinutes, aggregateLikes, healthScore, creditsText, license, sourceName, pricePerServing, extendedIngredients, id, title, readyInMinutes, servings, sourceUrl, image, imageType, summary, cuisines, dishTypes, diets, occasions, winePairing, instructions, analyzedInstructions, originalId, spoonacularSourceUrl
        return dish_data# a single dictionary
    def instructions(self,dish_data):
        return dish_data["analyzedInstructions"] #simple data
    def sourceUrl(self,dish_data):
        return dish_data["sourceUrl"] #url data
    

    
ob=recipe_parser("fbb7be320f9842a9ad38be90a1e8e288")


print(type(ob.recipes_search("milk,peanut butter,sugar,chocos")))

#Data required: recipe name, recipe source url, mentioned ingredients being used(usedIngredients), unusedIngredients, additional/missedIngredients