cart = ['candy','apple','grape','avocado','milk']
def m (list,letter):  
  c=0
  for x in range (len(list)):
    for y in range (len(list[x])):
      if letter == list[x][y]:
        c+=1
  print(f"There are {c} {letter}'s in this list.")

print(f"The list is {cart}\n")
m(cart,"a")
m(cart,"e")
m(cart,"q")
