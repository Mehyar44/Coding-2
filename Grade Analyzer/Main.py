l = []
l2 = []
x = ""

while x != -1:
  x = int(input("Enter a grade too add to the list or enter -1 to stop: "))
  if -1 < x < 101:
    l.append(x)
  elif x == -1:
    print("\nHere is your list: {}.".format(l)) 
  else:
    print("Inavlid grade\n")

#sum and average
s = 0
for a in range (len(l)):
  s += l[a]
ave = int(s / len(l))
print("The sum of all grades is {}.\nThe average is {}.".format(s,ave))

#min
min = l[0]
for b in range (len(l)):
  if min > l[b]:
    min = l[b]
print("The lowest grade is {}.".format(min))

#max
max = l[0]
for c in range (len(l)):
  if max < l[c]:
    max = l[c]
print("The highest grade is is {}.".format(max))

#sort
l2 = []
while len(l) != 0:
  min = l[0]
  for d in range (len(l)):
    if min > l[d]:
      min = l[d]
  l2.append(min)
  l.remove(min)
print("The sorted list is {}.".format(l2))

#median
if len(l2) % 2 == 1:
  x = int(len(l2) / 2)
  print("The median is {}.".format(l2[x]))
else:
  x = int(len(l2) / 2)
  m = int(((l2[x-1]) + (l2[x])) / 2)
  print("The median is {}.".format(m))
