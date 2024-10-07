"""CS120, Chris Kenworthy, Dabrion Eversley
Knock knock joke"""

name = input("What is your name? ")
play = input(f"Nice to meet you {name}, do you wanna hear a knock knock joke? ")

play = play.upper()

if play.startswith("Y"):
    knock = input("Alright! Knock knock! ")
    knock = knock.upper()
    
    if knock == "WHO'S THERE?":
        nona = input("Nona. ")
        nona = nona.upper()
        if nona == "NONA WHO?":
            print("That's Nona your business!")
        else:
            print("You just HAD to fumble at the end of the joke, didnt you?")
    else:
        print("You're not who I'm looking for..")
else:
    print("You're so mean to me.") 