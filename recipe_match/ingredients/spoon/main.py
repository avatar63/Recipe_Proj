import spoonacular as sp

class recipe_parser:
    api=''
    def __init__(self, spoonacular_key):
        self.spoonacular_key = spoonacular_key
        self.api = sp.API(spoonacular_key)
        
    def recipes_search(self,ingredients,minimum_recipes):
        data_dict = self.api.search_recipes_by_ingredients(ingredients,number=minimum_recipes).json()
        #NOTE ingredients is a string data type with ingredients listed as csv.
        #Returns a dictionary containing id,title,image,usedIngredientCount, missedIngredientCount,missedIngredientCount,missedIngredients,usedIngredients,unusedIngredients,likes
        return data_dict #a list of dictionaries
    
    def dish_id(self,data_dict):
        id_list=[]
        id_dict={}
        for i in data_dict:
            id = i["id"]
            id_dict.update({"id":id})
            id_list.append(id_dict)
            id_dict={}
        return id_list #a list of dictionaries with key id
    def recipeinformation(self,dish_id):
        dish_data = self.api.get_recipe_information(dish_id).json()
        #dish_data has the following keys: # vegetarian vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular, sustainable, lowFodmap, weightWatcherSmartPoints, gaps, preparationMinutes, cookingMinutes, aggregateLikes, healthScore, creditsText, license, sourceName, pricePerServing, extendedIngredients, id, title, readyInMinutes, servings, sourceUrl, image, imageType, summary, cuisines, dishTypes, diets, occasions, winePairing, instructions, analyzedInstructions, originalId, spoonacularSourceUrl
        # print(dish_data)
        analInstructions=dish_data["analyzedInstructions"][0]["steps"]   
        # print(analyzedInstructions)
        analyzedInstructions=[]
        for i in analInstructions:
            analyzedInstructions.append(i["step"])
        dish_data.update({"analyzedInstructions":analyzedInstructions})        
        return dish_data# a single dictionary
   
    def final_data(self, data_dict):
        
        format=[]
        missedIngredients=[]
        for i in data_dict:
            data = i["missedIngredients"]
            for k in data:
                format.append(k["name"])
            print(format)
            temp = ", ".join(format)
            missedIngredients.append(temp)
            format=[]
            temp=[]

        usedIngredients=[]
        for i in data_dict:
            data = i["usedIngredients"]
            for k in data:
                format.append(k["name"])
            temp = ", ".join(format)
            usedIngredients.append(temp)
            format=[]
            unusedIngredients=[]
            temp=[]
        for i in data_dict:
            data = i["unusedIngredients"]
            for k in data:
                format.append(k["name"])
            temp = ", ".join(format)
            unusedIngredients.append(temp)
            format=[]
            temp=[]
        count=0
        for k in data_dict:
            k.update({"missedIngredients":missedIngredients[count], "usedIngredients":usedIngredients[count],"unusedIngredients":unusedIngredients[count]})
            count+=1
            


        return data_dict
    
    def instructions(self,dish_data):
        return dish_data["analyzedInstructions"] #simple data
    def sourceUrl(self,dish_data):
        return dish_data["sourceUrl"] #url data
    

    
# ob=recipe_parser("fbb7be320f9842a9ad38be90a1e8e288")


# ob.recipeinformation("649184")




#Data required: recipe name, recipe source url, mentioned ingredients being used(usedIngredients), unusedIngredients, additional/missedIngredients