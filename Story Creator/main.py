print("Let's make a story!\n")

place1 = input("Where does this story happen? ")
adjective = input("How would you describe the place? ")
name1 = input("Who is the main character? ")
adverb = input("What adverb describes how the character is walking? ")
place2 = input("Where is the character walking to? ")
noun1 = input("Who or what attacks the main character? ")
group = input("What group helps the main character? ")
noun2 = input("What is a gift does the group give the main character? ")
number = input("What number do you want to pick? ")
name2 = input("Who should another character be? ")

print("\nIt is a {} day in {}. {} is {} walking down the street to {} \033[0;31mwhen suddenly an {} attacks.\033[0m {} decides to call for backup. The {} show up. Together, they destroy the {}. As a thank you the {} give {} a {}. The {} blows up by accident and {} dies. It turns out the {} were also {}. They take over the world. \033[0;32m{} days later {} comes from an alternate {} and defeats the {}.\033[0m" .format(adjective,place1,name1,adverb,place2,noun1,name1,group,noun1,group,name1,noun2,noun2,name1,group,noun1,number,name2,place1,noun1))
