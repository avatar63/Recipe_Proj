from recipes import *



class data_cleanser():
    def __init__(self,data):
        self.data = data
        return "DATA TO BE CLEANED AND PROCESSED: " , data
    
    def clean(self):
        #dirty_data=["chopped", "diced", "parmesan", "bow tie", "penne", "boneless, skinless", "dried", "freshly", "cracked", "crushed", "minced", ]

        #NOTE1 parantheses, commas and 'or' statements need to be addressed after this buzzword search.
        #NOTE2 buzzword search might be irrelevant. First we'll work on note 1. 

        for dish in range(len(self.data)):
            for i in range(len(self.data[dish])):
                food=self.data[dish].lower() # for simpler referencing.
                food[i]