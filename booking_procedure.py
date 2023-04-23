import random
class Train:
  def __init__(self,Train_no,Train_name,Seating_Capacity,Booked_Seats=0,Availability="None"):
    self.Train_no=Train_no
    self.Train_name=Train_name
    self.Seating_Capacity=Seating_Capacity
    self.Booked_Seats=Booked_Seats
    self.Availability=Availability
    
  #check whether train seats are available to book
  def Booking_Status(self):
    if self.Seating_Capacity==self.Booked_Seats:
      self.Availability="No seats available for booking"
    else:
      self.Availability="Booking available."
    print(self.Availability)
  
  #to book a seat by entering name and age if the persons age is more than 55 he will be automatically alloted lower birth seats
  def Book(self,Passenger_name,Passenger_age,Passenger_Dict):
    lower_berth=[1,3]
    seat_nos=[2,4,3,1]
    if (self.Booked_Seats<self.Seating_Capacity):
      if int(Passenger_age)>55:
        print("{} your Booking is done!! Lower Birth alloted and seat number {}".format(Passenger_name,random.sample(lower_berth,1)))
        self.Booked_Seats+=1
        print(self.Booked_Seats)
        Passenger_Dict.update({Passenger_name:Passenger_age})
      else:
        print("{} your Booking is done!! and seat number is {}".format(Passenger_name,random.sample(seat_nos,1)))
        self.Booked_Seats+=1
        print(self.Booked_Seats)
        Passenger_Dict.update({Passenger_name:Passenger_age})

    else:
      print("Booking full!!")
  
  
#to cancel any reservation done against any persons name
  def Cancel(self,Passenger_name,Passenger_Dict):
    if Passenger_name in Passenger_Dict:
      Passenger_Dict.pop(Passenger_name,[Passenger_name])
      print("Booking Cancelled")
      self.Booked_Seats-=1
      print(self.Booked_Seats)

      
#to see the passenger list of the train      
  def PassengerList(self,Passenger_Dict):
    print(Passenger_Dict) 

#to check the status of booking of any person 
  def CheckStatus(self,Passenger_name,Passenger_Dict):
    if Passenger_name in Passenger_Dict:
      print("{}.....your booking is done in {} {}".format(Passenger_name,self.Train_no,self.Train_name))
    else:
      print("Not a valid name!!Please check your name")

    
    
#enter the details of train 
if __name__=="__main__":
  a=[]
  Train_no=int(input("Enter train number: "))
  Train_name=input("Enter the train name: ")
  Seating_Capacity=int(input("Enter maximum seating capacity: "))
  a.append(Train(Train_no, Train_name, Seating_Capacity))

  Passenger_Dict={}
