class India():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("Hindi is the most widely spoken language of india ")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is developed country")
class Pakistan():
    def capital(self):
        print("Islamabad is the capital of pakistan")
    def language(self):
        print("Urdu is the primary language of pakistan")
    def type(self):
        print("Pakistan is a developing country")
obj_ind = India()
obj_usa = USA()
obj_pak = Pakistan()
for country in (obj_ind, obj_usa,obj_pak):
    country.capital()
    country.language()
    country.type()    
       

