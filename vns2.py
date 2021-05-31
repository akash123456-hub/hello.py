'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
'''
'''
class Dog:
   
    # Class Variable
    animal = 'dog'            
   
    # The init method or constructor
    def __init__(self, breed, color):
     
        # Instance Variable    
        self.breed = breed
        self.color = color       
    
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
 
print('Rodger details:')  
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
'''
#change list items
thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)
 
