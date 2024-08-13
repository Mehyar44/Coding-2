print("Hello! I'm the email making robot. To make your email I will need to ask you some questions.\n")
r=input("Are you a student or a teacher? ").lower()
fn=input("What is your first name? ").lower()
ln=input("What is your last name? ").lower()
n=input("What is your 6 digit id? ")
if r=="teacher":
  g=input("What is your gender? ").lower()
if len(n)==6:
  if r=="student":
    email=fn+ln[0]+n[4:]+'@nycstudents.net' 
    print("\nHello {} {}. Your email is {}".format(fn,ln,email))
  else:
    email=fn[0]+ln+n[4:]+'@schools.nyc.gov'
    if g=='male':
     print("\nHello Mr {}. Your email is {}".format(ln,email))
    elif g=='female':
      print("\nHello Ms {}. Your email is {}".format(ln,email))
    else:
      print("\nHello {} {}. Your email is {}".format(fn,ln,email))
else:
  print("\nYour id is supposed to have 6 digits. Please try again.")
