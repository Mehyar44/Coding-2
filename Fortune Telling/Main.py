#Function 1
def f1(n):
  print(f'\033[0;35m{n}\033[0m, your lucky number is 9 and your lucky color is red.')
print("\033[0;35mFunction 1:\033[0m")
f1("Lin")
f1("Olivia")
f1("Mariam")

#Function 2
def f2(num):
  print(f'Lin, your lucky number is \033[1;34m{num}\033[0m and your lucky color is red.')
print("\033[1;34m\nFunction 2:\033[0m")
f2(9)
f2(3)
f2(1)

#Function 3
def f3(c):
  print(f'Lin, your lucky number is 9 and your lucky color is \033[1;32m{c}\033[0m.')
print("\033[1;32m\nFunction 3:\033[0m")
f3("red")
f3("yellow")
f3("blue")

#Function 4
def f4(n,num,c):
  print(f'\033[0;35m{n}\033[0m, your lucky number is \033[1;34m{num}\033[0m and your lucky color is \033[1;32m{c}\033[0m.')
print("\033[1;33m\nFunction 4:\033[0m")
f4("Mehyar",4,"orange")
f4("Nancy",13,"geen")
f4("John",7,"purple")
