l = []
a = ""

print("Hello, welcome to your to-do list!")
while not a == "exit":
  a = input("What would you like to do? (add, remove, show, exit): ").lower()

#show
  if a == "show":
    print("\nHere is your list: {}\n".format(l))

#add
  elif a == "add":
    aa = input("\nWhat would you like to add? ").lower()
    while aa in l:
      aa = input("\n" + aa + " is already in the list, you can't add it again.\nPick another item:").lower()
    else:
      l.append(aa)
      print("\n" + aa + " added successfully.\n")

#remove
  elif a == "remove":
    if len(l) == 0:
      print("The list is empty, there is nothing to remove.\n")
    else:
      r = input("\nWhat would you like to remove? ").lower()
      while not r in l:
        r = input("\n" + r + " is not in the list, you can't remove it.\nPick another item:").lower()
      else:
        l.remove(r)
        print("\n" + r + " removed successfully.\n")
 
#exit  
  elif a == "exit":
    print("\nThank you for using this program. See you next time. :D")

#error    
  else:
    print("Your answer is invalid. Enter a valid answer.\n")
