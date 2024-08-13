l1 = ['dog','berry','bear','bay','loaf','life','dress',]
l2 = []

for x in range (len(l1)):
  w = l1[x]
  if w[-1] == "y":
    if w[-2] in "aeoui":
     l2.append(w + 's')
    else:
      l2.append(w[:-1] + 'ies')
  elif w[-1] == "o" or w[-1] == "s":
    l2.append(w + 'es')
  elif w[-1] == "f":
    l2.append(w[:-1] + "ves")
  elif w[-2:] == ("fe"):
    l2.append(w[:-2] + "ves")
  else:
    l2.append(w + "s")
    
print("Orginal:\n{}\n".format(l1))
print("Pluralized:\n{}\n".format(l2))
