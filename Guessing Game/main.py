#name
n = input("What is your name? ")

#min
min = int(input("\nPick a minimum for the range (must be positive): "))
while min < 0:
  min = int(input("This is not a positive number. Pick again: "))

#max
max=int(input("\nPick a maximum for the range (must be greater than minimum): "))
while max <= min:
  max = int(input("This is less than or equal to the minimum. Pick again: "))

#secret number
import random
sn = random.randint(min,max)
c = 0

#guessing
gn = int(input("\nHello {}, guess a number from ({}-{}) or enter -1 for a hint: ".format(n,min,max)))
while not gn == sn:
  if gn != sn:
    
    #hint
    if gn == -1:
      if sn % 2 == 0:
        print("The number is even")
      else:
        print("The number is odd")

    #out of range
    elif gn < min or gn > max:
      print("Sorry {}, your guess is out of range.".format(n))
      
    #too low
    elif gn < sn:
      min = gn
      c += 1
      print("Sorry {}, your guess is too small.".format(n))
      
    #too high
    elif gn > sn:
      max = gn
      c += 1
      print("Sorry {}, your guess is too big.".format(n))
      
    gn = int(input("\nGuess from ({}-{}) or enter -1 for a hint: ".format(min,max)))

#correct
else:
  c += 1
  print("\nGood job {}! You got the number in {} tries. The secret number was {}.".format(n,c,sn))
