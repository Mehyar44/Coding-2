g1=int(input('What is your grade for math? '))
g2=int(input('What is your grade for science? '))
g3=int(input('What is your grade for history? '))
g4=int(input('What is your grade for english? '))
g5=int(input('What is your grade for coding? '))

average=(g1+g2+g3+g4+g5)/5
print("\nYour average is {}" .format(average))

if average>90:
  print("This is an A+.")
elif average>85:
  print("This is an A.")
elif average>80:
  print("This is an A-.")
elif average>77:
  print("This is a B+.")
elif average>73:
  print("This is a B.")
elif average>70:
  print("This is a B-.")
elif average>65:
  print("This is a C+.")
elif average>60:
  print("This is a C.")
elif average>55:
  print("This is a C-.")
elif average>50:
  print("This is a D.")
else:
  print("This is an F.")
