import re

#Here the input is going to be a nested list of ingredients.
#Example: 
# data=[['chicken thighs', 'lemon pepper seasoning', 'cooking oil', 'garlic', 'chicken broth', 'chopped parsley', 'orzo', 'feta, crumbled'], ['boneless, skinless chicken breasts (about 1.3 lb. total)', 'Italian seasoning', 'cooking oil', 'butter', 'garlic, minced', 'heavy cream', 'grated Parmesan', 'salt', 'pepper', 'chopped parsley (optional garnish)', 'fettuccine'], ['bow tie pasta', 'frozen broccoli florets', 'olive oil', 'boneless, skinless chicken breast', 'basil pesto', 'chicken broth', 'cream cheese'], ['breadcrumbs', 'grated Parmesan', 'garlic powder', 'dried basil', 'dried oregano', 'salt', 'freshly cracked black pepper', 'ground chicken', 'egg', 'cooking oil'], ['boneless, skinless chicken breast', 'butter', 'garlic', 'penne pasta', 'chicken broth', 'milk', 'cream cheese', 'basil pesto', 'grated Parmesan', 'freshly cracked pepper', 'crushed red pepper'], ['orecchiette', 'olive oil', 'chicken sausage', 'butter', 'garlic, minced', 'chopped kale', 'grated Parmesan', 'crushed red pepper', 'salt', 'freshly cracked pepper to taste'], ['smoked paprika', 'oregano', 'thyme', 'garlic powder', 'onion powder', 'cayenne pepper', 'black pepper', 'salt'], ['pasta (any short shape)', 'frozen broccoli florets', 'boneless, skinless chicken breast (about 2/3 lb.)', 'salt and pepper', 'cooking oil', 'butter', 'evaporated milk', 'garlic powder', 'smoked paprika', 'salt', 'extra sharp white cheddar, shredded'], ['frozen broccoli florets', 'rotini pasta', 'boneless, skinless chicken thighs (about 2/3 lb. total)', 'salt and peppers', 'olive oil', 'garlic', 'fresh lemon', 'chicken broth', 'heavy cream'], ['chili powder', 'smoked paprika', 'onion powder', 'garlic powder', 'cumin', 'cayenne', 'sugar', 'salt'], ['lemon', 'olive oil', 'garlic, divided', 'dried oregano', 'salt ', 'Freshly cracked pepper'], ['garlic ', 'butter ', 'pumpkin purée ', 'chicken broth ', 'nutmeg ', 'chili powder ', 'cayenne pepper ', 'Freshly cracked black pepper ', 'half & half or cream ', 'pasta ']]

class Cleaner():
    def __init__(self):
        return None
    def brackets_or(food):
        temp=[]
        main=[]
        t_list=[]
        print("cleaning data...")
        for j in food:
            for k in j:
                k=re.sub("[\(\[].*?[\)\]]", "", k).strip().lower()
                if k.split("or"): 
                    or_list=k.split(" or ")
                    for j in or_list:
                        t_list.append(j.strip())
                        temp=temp+t_list
                        t_list=[]
                else:
                    temp.append(k)
            main.append(temp)
            temp=[]
        return main
    
    # def clean(self):
        # clean_data=[]
        # temp=[]
        # dirty_data=["chopped", "diced", "parmesan", "bow tie", "penne", "boneless, skinless", "dried", "freshly", "cracked", "crushed", "minced", ]
# 
        # NOTE1 parantheses, commas and 'or' statements need to be addressed after this buzzword search.
        # NOTE2 buzzword search might be irrelevant. First we'll work on note 1. 
# 
        # for dish in range(len(self.data)):
            # for i in range(len(self.data[dish])):
                # food=self.data[dish][i].lower().strip() # for simpler referencing.
                # temp.append(food)
            # clean_data.append(temp)
            # temp=[]
        # return clean_data
#data=[["Food1","Food2"]]
# print(ob.brackets_or(data))

# list="half & half cream".split("or")
# print(list)