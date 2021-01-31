
name = input("Please enter your name: ")

print(f"Welcome to {name}'s Choose Your Own Adventure game! As you follow the story, you will be presented with that decide your fate. Take care and choose wisely! Let's begin.")
print("You find yourself in a dark room with 2 doors. The first door is red, the second door is green!")
door_choice = input("Wich door do you want to choose youngling? red=red door or green=green door: ")
if door_choice == "red":
    print("Great, you walk in a pit full of pugs. One of them asks you to find Harvey (A black pug).")
    
    choice_one = input("What do you want to do? 1=accept or 2=decline: ")
    if choice_one=="1":
        print("""________________SUCCESS________________
You helped the pugs and they lick you and show you the passage!""")
        print("You walk out the pug pit and see something black rustling in the bushes")
        choice_two = input("What do you want to do? 1=check or 2=pick up: ")
        if choice_two=="1":
            print("""________________GAME_OVER________________
You check to see if its Harvey (A black pug). Then she starts attacking you.""")
        else:
            print("""________________SUCCESS________________
You pick her up. She starts nibbling you. You get back to the pug pit and you give them Harvey (A black pug). Harvey has a happy face and licks you and tells you to go and get her the golden biscuit""")
            choice_three = input("What do you want to do? 1=accept or 2=run away: ")
            if choice_three=="1":
                print("She tells you where to go but you don't understand. She gives you a map and now you understand.")
                choice_four = input("What do you want to do? 1=left or 2=right: ")
                if choice_four=="1":
                    print("You go left of the mountain")
                    choice_six = input("You walk in front of the mountain entrance and you see the golden biscuit and you wonder how are you going to get it. What do you want to do? 1=climb or 2=fight the guards: ")
                    if choice_six=="1":
                        print("""________________SUCCESS________________
You climb the mountain and get the golden biscuit and then you reppel down and go to the pug pit. You give her the golden biscuit. She eats it and a door forms. You open the door and wake up from this dream""")
                    else:
                        print("""________________GAME_OVER_________________
You try to fight the guards and then they pick you up. They shock you and you wake up from this dream.""")
                else:
                    print("You go right of the mountain. Oh No A pug monster sees you.")
                    choice_five = input("What do you want to do? 1=attack or 2=run away: ")
                    if choice_five=="1":
                        print("""________________GAME_OVER________________
you fight it. You get killed from it.""") 
                    else:print("""_______________GAME_OVER________________
you run back to the pug pit and they are confused.""")
            else:
                print("""________________GAME_OVER________________
You run away because you are scared and you become a pug.""")
    else:
         print("""________________GAME_OVER_________________
Too bad! They start attacking you and one of them pull a lever so you fall into a pit of snakes.""")
else:
    print("Great you walk in it and you fall and land on a mountain.")
    choice_seven = input("What do you want to do? 1=ski down or 2=parachute down or 3=reppel down: ")
    if choice_seven == "3":
        print("""________________GAME_OVER________________
You start reppeling down until you hook a loose rock and you fall till your death.""")
    else:
        if choice_seven=="1":
            print("""________________SUCCESS________________
Yaaaaaaaaaaaaaay. You ski down your way the mountain and stop at a camp.""")
        else: 
            print("""________________SUCCESS________________
You jump and know your way down the mountain and stop at a camp.""")
        
        choice_eight = input("You stop by a camp and ask them where to go. What do you want to do? 1=ski left or 2=ski right: ")
        if choice_eight=="1":
            print("""________________SUCCESS________________
You don't hurt yourself. You do a jump that is high and...
                      ...you land it. You see something shiny in the sky while skiing and stop to see what it is with binoculars. HOLY COW, it's a meteor falling to destroy the planet.""")
            choice_nine = input("What do you want to do? 1=ski towards it or 2=dig a hole and try to survive or 3=climb back up the hill: ")
            if choice_nine=="1":
                print("""________________GAME_OVER________________
You ski towards it and realise the you did a bad choice and your skin and flesh start melting off of you.""")
            elif choice_nine=="2":
                print("""________________SUCCESS________________
Yah you dug a hole just in time when the meteor hit, the planet exploded.""")
                choice_ten = input("You feel that like your dead but you just look up and realise that your alive still. What do you want to do 1 = ski left or 2 = ski to the remains or 3 = ski right or 4 = panic: ")
                if choice_ten=="1":
                    print("""________________GAME_OVER________________
Ahhhhhhhh. You died of radiation by it going to your heart and stoping it.""")
                elif choice_ten=="2"
                    print("""_______________GAME_OVER________________
""")
            else:
                print("""________________GAME_OVER________________
You don't have enough time to get to the top and your skin and flesh start melting off.""")
        else:       
            print("""________________GAME_OVER________________
You jump to high and fly off the edge and fall to your death.""")
            