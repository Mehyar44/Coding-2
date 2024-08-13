print("Let's make a triangle!\n")
a=int(input("What should the \033[0;31mfirst side\033[0m be? " ))
b=int(input("What should the \033[0;32msecond side\033[0m be? " ))
c=int(input("What should the \033[0;36mthird side\033[0m be? " ))
perimeter=a+b+c

if a+b>c and b+c>a and c+a>b:
  print("\nThese sides make up a correct triangle. The \033[0;35mperimeter\033[0m is {}" .format(perimeter))

  #right
  if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+b**2==a**2:
    print("\nThis is a \033[1;33mright\033[0m triangle.")

  #equalateral
  if a==b==c:
    print("\nThis is an \033[1;33mequalateral\033[0m tringle")

  #isosceles
  elif a==b or a==c or b==c:
    print("\nThis is an \033[1;33misosceles\033[0m triangle.")

  #scalene
  else:
    print("\nThis is a \033[1;33mscalene\033[0m triangle")
  
else:
  print("\nThese sides \033[0;35mdont make a triangle.\033[0m")
