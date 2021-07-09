class India():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("Hindi is the most widely spoken language of india")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")
class Italy():
    def capital(self):
        print("Rome is the capital of Italy")
    def language(self):
        print("English is the primary language of Italy")
    def type(self):
        print("Italy is a developed country")
obj_ind = India()
obj_usa = USA()
obj_italy = Italy()
for country in (obj_ind,obj_usa,obj_italy):
    country.capital()
    country.language()
    country.type()
