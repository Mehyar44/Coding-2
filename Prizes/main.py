#part1
l=["a laptop","a kitkat","a bear","a yacht","a million dollars","a private island","nothing","a spaceship", "a race car", "a mansion"]
n=int(input("Part 1:\nPick a number from one to ten for a prize: "))
if 0<n<11:
  print("You won "+l[n-1]+"!")
else:
  print("That is an invalid number.")

#part2
n1=int(input("\nPart 2:\nPick a starting number:"))
if 0<n1<11:
  n2=int(input("Pick an ending number: "))
  if 0<n2<11:
    if n2>n1:
      p=l[n1-1:n2]
      print("Here are you prizes; {}.".format(p))
    else:
      print("The ending number has to be bigger than the starting number.")
  else:
    print("This is an invalid number.")
else:
  print("This is an invalid number.")
