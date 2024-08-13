items = ['apple','pear','candy','boy','berry','strawberry','cranberry','tomato','loaf','knife','dress']

def rl (l1):
  print(f'\033[0m\033[1;34mHere is your original list:\033[0m\n{l1}')
  l2 = []
  for x in range (len(l1)):
    l2.append(l1[-x-1])
  print(f'\n\033[1;34mHere is your list reversed:\033[0m\n{l2}')
  
def rw (l1):
  print(f'\033[0m\033[1;34mHere is your original list:\033[0m\n{l1}')
  l2 = []
  w = ''
  for x in range (len(l1)):
    for y in range (len(l1[x])):
      w += l1[x][-y-1]
    l2.append(w)
    w = ''
  print(f'\n\033[1;34mHere is your list with reversed words:\033[0m\n{l2}')
  
rl(items)
print("\n\033[0;31m--------------------------------\n")
rw(items)
