userput = int(input("How many"))
print(userput)
weight = 100


# ground shipping
print("For premium give 12,500 points")
if weight > 0 and weight <= 2:
  gcost = (weight * 1.5 + 20)
  print("Ground price: ", gcost)
elif (weight > 2) and (weight <= 6):
  gcost = (weight * 3 + 20)
  print("Ground price: ", gcost)
elif (weight > 6) and (weight <= 10):
  gcost = (weight * 4 + 20)
  print("Ground price: ", gcost)
elif weight > 10:
  gcost = (weight * 4.75 + 20)
  print("Ground price: ", gcost)
else:
  print("Negatively weighted packages are shipped through Gersh Device.")

#Drone shipping

if weight > 0 and weight <= 2:
  dcost = (weight * 4.5)
  print("Drone price: ", dcost)
elif (weight > 2) and (weight <= 6):
  dcost = (weight * 9)
  print("Drone price: ", dcost)
elif (weight > 6) and (weight <= 10):
  dcost = (weight * 12)
  print("Drone price: ", dcost)
elif weight > 10:
  dcost = (weight * 14.25)
  print("Drone price: ", dcost)
else:
  print("Negatively weighted packages are unable to be shipped by normal drone, see MPD MAXIS DRONE USAGE manual for instructions.")
