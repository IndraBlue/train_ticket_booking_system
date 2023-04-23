#menu for booking process
options=0
while(options<6):
  print("press 1 to check availibility")
  print("press 2 to book ticket")
  print("press 3 to cancel booking")
  print("press 4 to view passenger list")
  print("press 5 to check your booking status")
  options=int(input("Enter the option: "))
  if options==1:
    for j in a:
      j.Booking_Status()
  elif options==2:
    Passenger_name=input("Enter passenger name: ")
    Passenger_age=int(input("Enter passenger age: "))
    for j in a:
      j.Book(Passenger_name,Passenger_age,Passenger_Dict)
  elif options==3:
    Passenger_name=input("Enter passenger name: ")
    for j in a:
      j.Cancel(Passenger_name,Passenger_Dict)
  elif options==4:
    for j in a:
      j.PassengerList(Passenger_Dict)
  elif options==5:
    Passenger_name=input("Enter passenger name: ")
    for j in a:
      j.CheckStatus(Passenger_name,Passenger_Dict)
      
  else:
    print("Thank you!!")
    break
