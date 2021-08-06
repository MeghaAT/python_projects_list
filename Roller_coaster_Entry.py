print("welcome to Megha's world, Hope you have a great time")
height=int(input("what is your height in cm?"))
if height>=120:
  print("you can ride the roller coaster")
  age=int(input("what is your age?"))
  if age<12:
    print("please pay 5$ as your entry fee ")
  elif age<=18:
    print("please pay 8$ as your entry fee")
  else:
      print("please pay 15$ as your entry fee")
else:
  print("you will ahve to grow taller to ride the roller coaster")  
