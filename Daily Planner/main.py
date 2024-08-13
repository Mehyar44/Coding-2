p = ['_'] * 24

def show():
    print(p[0:4])
    print(p[4:8])
    print(p[8:12])
    print(p[12:16])
    print(p[16:20])
    print(p[20:24])

def add(e, t, c):
    if not 0 <= t < 24:
        print('The time is out of range.\n')
    elif c == 'yes':
        if p[t] == '_':
            p[t] = e
            print(f'Added {e} to planner.\n')
        else:
            print(f'Replaced {p[t]} with {e}.\n')
            p[t] = e
    elif c == 'no':
        if p[t] == '_':
            p[t] = e
            print(f'Added {e} to planner.\n')
        else:
            print(f'{e} conflicts with {p[t]}\n')
    else:
        print('Only yes or no.\n')

def clear(x1, x2):
    if not 0 <= x1 < 24:
        print('The starting time is out of range\n')
    elif not 0 <= x2 < 24:
        print('The ending time is out of range\n')
    elif x2 < x1:
        print('The ending time has to be more than the starting time.\n')
    else: 
        p[x1:x2+1] = ['_'] * (x2 - x1 + 1)
        print('Successfully cleared.\n')

a = ''
while a != 'exit':
    a = input("What do you want to do (show/add/clear/exit)? ").lower()
    if a == 'add':
        event = input('What event do you want to add? ')
        time = int(input('What time (0 to 24)? '))
        conflict = input('Is the event critical (yes or no)? ').lower()
        add(event, time, conflict)
        print()
    elif a == 'show':
        show()
        print()
    elif a == 'clear':
        x1 = int(input('Where do you want to start clearing? '))
        x2 = int(input('Where do you want to end clearing? '))
        clear(x1, x2)
    elif a == 'exit':
        print('\nThank you for using this planner.')
    else:
        print('Invalid answer.')
