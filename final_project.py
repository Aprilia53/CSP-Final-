#setting up story for game and ask a name - everyone
print("Welcome to our game! What is your name?")
name = input()
print("Hello, " +name+ "! you are on a mission to climb the tallest mountain in your small town! first youll need supplise.")

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

print("Oh no! you only have enough room to take one thing!") 
print("Pick on thing to take.")

n = int(input('How many things would you like to take?:'))

for i in range(0,n):

    print("Pick what you want to take\n")

    print('Enter 1 for water bottle\n')

    print('Enter 2 for shoes\n')

    print('Enter 3 for food\n')

    print('Enter 4 for warmth\n')

    print('Enter 5 for tent\n')

    choice = int(input('Enter your choice:'))

    if choice == 1:
        print("You chose water bottle")
    elif choice == 2:
        print("You chose shoes")   
    elif choice == 3:
        print("You chose food")
    elif choice == 4:
        print("You chose warmth")
    elif choice == 5:
        print("You chose a tent")
    else:
        print("Invalid choice") 
    

#ask user where they would like to go next  - (stop and eat, go into cave, keep going) Lola  (conditional)
print("You made it half way up!")
print("What do you want to do now?")
print("1. keep going up the mountain")
print("2. take a break to eat")
print("3. go into the cave")
picked = input("Pick a thing to do: ")
if picked == 1:
    print("You picked keep going up")
elif picked == 3:
    print("You picked go into the cave")
else:
    print("Game Over! Your food is stale.")


#User runs in with yeti (yeti gives options to get food, shelter or a (better) map-Franco-(function)
def scnd(choice):
    return f"{choice},"

if picked == 1.:
    yetiplace = "up the mountain"
elif picked == 3.:
    yetiplace = "through the forest"
else:
    yetiplace = "The game is still over"
print("you walk", yetiplace)
print("When, GRAHHHHHHHHHHHHHH I'mm the yeti, do you want 1.food, 2.shelter, or a 3.TREASURE mapU")
print(scnd("1."))
print(scnd("2."))
print(scnd("3."))
#user makes it to the top and plants flag (it you wanna stay, eat something, plant a flag) - Tara (loop)
print("Yay!! You made it to the top!")
print("1. plant a flag , 2. stay at the top , 3. eat a snack. ")
course = int(input("What do you want to do (only enter number):"))
if course == 1:
    print("Yay! You plant a bright green flag!")
elif course == 2:
    print("You stay at the top, enjoying the gorgeous view!")
elif course == 3:
    print("You grab a slice of cheese, but oopsies, it's moldy and you die. boo hoo")
else:
    print("You chill for a while on the montain, yay. Your mother would be so proud of you.")
    

#User goes back down (deciding wheather they want to live there, go back down, or go on another adventure)- (everyone)
print("After a while, you get bored and decide to do something else.")
print("Would you like to, a. live there forever, b. go straight home")