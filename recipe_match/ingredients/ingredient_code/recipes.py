from bs4 import BeautifulSoup as bs
import requests
import mysql.connector as sql
from .cleaner import Cleaner


# Rough Mind Map to Follow:

#1. Start with taking user input to get what url to scrape data from.

#1.5 Break down all recipe urls from that main url.

#2. Begin to scrape all recipes in that url and store them in a dictionary.

#3. Comparative analysis of each recipe.

#4. All these 3 major compenents are going to be in a class and have a function dedicated to each of it that may be called individually.

#5. Lets see how it goes.


class recipes:
    links=[]
    ingredients=[]
    key_list=[]
    comp_list=[]


    def __init__(self,url, dish_list):
        self.url = url
        self.dish_list = dish_list
        #self.category = categorwhaty
        #url is the input given by the user
    def dish_gen(self):

        print("generating...")
        data = requests.get(self.url).text
        soup = bs(data,'lxml')
        block = soup.find_all("article")
        
        self.dish_list=[]
        for i in block:
            dish = i.find('h3').text.split()
            name = (' ').join(dish)
            self.dish_list.append(name)
        
        return(self.dish_list)
    
    def url_gen(self):
        data = requests.get(self.url).text
        soup = bs(data,'lxml')
        block = soup.find_all("article")
        
        for i in range(len(block)):
            link = block[i].find('a')
            recipes.links.append(link.get('href'))        
        return recipes.links
    
    def dish_recipe(self,dish_urls):
        ing_list=[]
        temp=[]
        
        for i in dish_urls:
            datasource=requests.get(i).text
            soup = bs(datasource,'lxml')
            data = soup.find('div', class_="wprm-recipe-container")
            final_xml = data.find('ul').find_all("span", class_="wprm-recipe-ingredient-name")
            for p in final_xml: 
                trimmed = p.text.replace('*','') #clearing out all unnecessary stars
                temp.append(trimmed)
            ing_list.append(temp)
            recipes.ingredients.append(temp)
            temp=[]
        print("INGREDIENTS LIST")
        a=recipes.ingredients
        recipes.ingredients=Cleaner.brackets_or(a)
        
        return recipes.ingredients

    def comparison_analysis(self):
        n = len(recipes.ingredients)
        compared_dishes=[]
        
        for i in range(n):
            for k in range(i,n):
                if i==k:
                    continue
                comparison=list(frozenset(recipes.ingredients[i]).intersection(recipes.ingredients[k]))
                compared_dishes.append(self.dish_list[i])
                compared_dishes.append(self.dish_list[k])
                recipes.comp_list.append(comparison)
                recipes.key_list.append(compared_dishes)
                compared_dishes=[]
        return recipes.comp_list


    def compared(self,minimum):
        count=0
        dict={}
        list=[]
        for i in range(len(recipes.key_list)):
            if len(recipes.comp_list[i])>minimum:
                dict.update({"dishes":recipes.key_list[i],"Common_Ingredients" :recipes.comp_list[i]})
                count+=1
            list.append(dict)
            dict={}
        return list
    
    
    def sql_upload(self,host,user,password):
        db=sql.connect(host=host,user=user,password=password)
        
        cursor=db.cursor()
        cursor.execute("SHOW DATABASES;")
        for x in cursor:
            print(x)
        cursor.execute("USE recipe_proj;")        

        for i in range(len(recipes.ingredients)):
            dish=self.dish_list[i]
            dish_url=recipes.links[i]
            ingredients=recipes.ingredients[i]          
            query="""INSERT INTO dishes(dish_name,category, url, ingredients) VALUES("%s", "%s","%s","%s");""" % (dish,dish_url,ingredients)
            print(query)
            cursor.execute(query)
      
        db.commit();        
        cursor.close()
        db.close()
        return "SQL updation successful !!!"

    

# ob = recipes("https://www.budgetbytes.com/category/recipes/pasta/chicken-pasta/","")
# dish_list= ob.dish_gen()

# print("DISH LISTS: ")
# print(dish_list)

# dish_list=ob.url_gen()

# ob.dish_recipe(dish_list)



# ob.comparison_analysis()

# print(ob.ingredients)
