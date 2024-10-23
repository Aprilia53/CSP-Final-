#setting up story for game and ask a name - everyone
print("Welcome to our game! What is your name?")
name = input()
print("Hello, " +name+"! you are on a mission to climb the tallest mountain in your small town! first youll need supplise.")

#get a map and supplies, in village (ask what they want to buy first) - Aprilia (function)
print("You walk to your nearby shops, and your overwhelmed with how many supplies you need.")
print("The shop owner says: Are you "+name+"? I hear you are climbing to the tallest mountain in the city!")
print("You'll need lots of supplies. Starting with a rope, and ")

def need(supplies):
    return f"{supplies},"

print(need("water bottle"))
print(need("shoes"))
print(need("food"))
print(need("warmth"))
print(need("tent"))

print("Oh no! you only have enough room to buy one thing!")
print("Pick on thing to take.")

n = int(input('pick one thing to take:'))

for i in range(0,n):

    print('Enter 1 for water bottle\n')

    print('Enter 2 for shoes\n')

    print('Enter 3 for food\n')

    print('Enter 3 for warmth\n')

    print('Enter 3 for tent\n')

    choice = int(input('Enter your choice:'))

    if (choice == 1):
       
 else
    print('Invalid choice') 


    
       





#ask user where they would like to go next  - (stop and eat, go into cave, keep going) Lola  (conditional)

#User runs in with yeti (yeti gives options to get food, )helte- or a (better) map  Franco (function)

#user makes it to the top and plants flag (it you wanna stay, eat something, plant a flag) - Tara (loop)

#User goes back down (deciding wheather they want to live there, go back down, or go on another adventure)- (everyone)