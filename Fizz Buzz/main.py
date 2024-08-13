n = int(input("How long do you want this to loop for? "))

print()
for x in range(1, n + 1):
  if x % 15 == 0:
    print("Fizz Buzz")
  elif x % 3 == 0:
    print("Fizz")
  elif x % 5 == 0:
    print("Buzz")
  else:
    print(x)
