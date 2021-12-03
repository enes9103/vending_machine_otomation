money1 = float(input("Please upload money: "))

print("Hello welcome. Your current balance: ", money1)

if money1 >= 1.50:
  question = input("Do you want tea or coffee?: ").lower().strip()
  
  if question == "tea":
    print("Your tea is being prepared. Here's your change: ", money1 - 1, "Euro")

  elif question == "coffee":
    print("Your coffee is being prepared. Here's your change: ", money1 - 1.50, "Euro")

  else:
    print("Sorry, here's your change: ", money1, "Euro")

elif 1 <= money1 < 1.50:
  question = input("You can only receive tea with your balance. Would you like tea?: ").lower()

  if question == "yes":
    print("Your tea is being prepared. Here's your change: ", money1 - 1, "Euro")

  elif question == "no":
    print("We thank you. Here's your change: ", money1, "Euro")

  else:
    print("Sorry, here's your change: ", money1, "Euro")

elif money1 < 1:
  question = input("Do you want to add money? Your balance is insufficient.: ").lower()

  if question == "no":
    print("We thank you. Here's your change: ", money1, "Euro")

  elif question == "yes":
    money2 = float(input("Please add money: "))

    if money1 + money2 >= 1.50:
      question = input("Do you want tea or coffee?: ").lower().strip()
      
      if question == "coffee":
        print("Your coffee is being prepared. Here's your change: ", money1 + money2 - 1.50, "Euro")

      elif question == "tea":
        print("Your tea is being prepared. Here's your change: ", money1 + money2 - 1, "Euro")

      else:
        print("Sorry, here's your change:: ", money1 + money2, "Euro")

    elif money1 + money2 < 1:
      print("Sorry, here's your change:: ", money1 + money2, "Euro")

    elif 1 <= money1 + money2 < 1.50:
      question = input("You can only receive tea with your balance. Would you like tea?: ").lower()

      if question == "no":
        print("We thank you. Here's your change: ", money1 + money2, "Euro")

      elif question == "yes":
        print("Your tea is being prepared. Here's your change: ", money1 + money2 - 1, "Euro")

      else:
        print("Sorry, here's your change: ", money1 + money2, "Euro")
  else:
    print("Sorry, here's your change: ", money1, "Euro")
else:
  print("Sorry, here's your change: ", money1, "Euro") 
  
