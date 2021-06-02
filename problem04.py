class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getstatus(self):
        print(f"The name of the train is{self.name}") 
        print(f"The seats available in the train are{self.seats}") 
    def fareInfo(self):
        print(f"The price of the ticket is:Rs{self.fare}")
    def bookTicket(self):
        if(self.seats>0):
           print("your ticket has been booked! your seat number is{self.seat}") 
           self.seats = self.seats-1
        else:
           print("sorry this train is full! kindly try in tatkal")
intercity = Train("Intercity Express:14015", 90, 300)   
intercity.getstatus() 
intercity.bookTicket() 
intercity.getstatus()    

