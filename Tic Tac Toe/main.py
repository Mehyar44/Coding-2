b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = "\033[0;31mX\033[0m"
o = "\033[1;36mO\033[0m"

def print_board():
  print(*b[0:3], sep="|")
  print(*b[3:6], sep="|")
  print(*b[6:9], sep="|")

def check_winner(p):
  wc = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ]

  for c in wc:
    if b[c[0]] == b[c[1]] == b[c[2]] == p:
      return True
  return False

print_board()

for turn in range(9):
  if turn % 2 == 0:
    print(f"\n\033[0;31mX\033[0m's turn")
    p = x
    
  else:
    print(f"\n\033[1;36mO\033[0m's turn")
    p = o

  n = int(input("Pick a number from 1-9: ")) - 1

  while not 0 <= n < 9 or b[n] in [x, o]:
    n = int(input("This number is invalid, pick again: ")) - 1

  b[n] = p

  print_board()

  if check_winner(p):
    print(f"\n{p} wins!")
    break

else:
  print("\nIt's a draw!")
