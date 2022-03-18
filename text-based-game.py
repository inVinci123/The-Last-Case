import os
from overhead import Overhead
from player import Player
from random import randint

def clear() -> None:
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clear()
score = 0
overhead: Overhead
player: Player
birthdate: str
knowsAboutWork: bool

def askQuestion(prompt: str, options: list[str], counter: int = 5) -> str:

    print(prompt)

    for index, option in enumerate(options, start=1):
        print(f"[{index}] {option}")
    answer = 0
    while(answer <= 0):
        try:
            answer = int(input("Please enter a number: ").strip())
            if(answer < 1 or answer > len(options)):
                answer = 0
                raise ValueError()
        except ValueError:
            if(counter > 0):
                print(f"Not a valid number. Please enter a valid number that is one of the options, eg: 1. You have {counter} {'tries' if counter > 1 else 'try'} remaining.")
                counter -= 1
            else:
                print("Too many invalid tries. Terminating... (Press Enter/Return to proceed)")
                input()
                clear()
                exit(1)


        except KeyboardInterrupt:
            clear()
            print("Keyboard Interrupt recieved. Terminating... (Press Enter/Return to proceed)")
            input()
            clear()
            exit(1)
            
    clear()
    return answer

def end(status: int) -> None:
    clear()
    if(status == 0):
        print("Congrats, you won!")
        print(f"You final score was {score}")
        exit(0)
    elif(status == 1):
        print("You arrested the wrong person! Better luck next time")
        print(f"Your final score was 0")
        exit(0)
    else:
        print("ERROR, function end() received an invalid status")

def scene1():
    validResponse = False
    while(not validResponse):
        input("You reach the crime scene, a small well maintained cityside apartment where a young lady of 24 is lying in a pool of blood. Her husband was talking to the police, answering their questions.\n")
        overhead.printOverhead(0)
        if(knowsAboutWork):
            a = askQuestion("Do you:", ["Enquire the husband", "Look around the room", "Investigate the body", "Go to the work place"])
            if(a==1):
                scene2() # Enquire the husband
                validResponse = True
            elif(a==2):
                scene3() # Look around the house
                validResponse = True
            elif(a==3):
                scene4() # Investigate the body
                validResponse = True
            elif(a==4):
                scene6() # Go to work
        else:
            a = askQuestion("Do you:", ["Enquire the husband", "Look around the room", "Investigate the body"])
            if(a==1):
                scene2() # Enquire the husband
                validResponse = True
            elif(a==2):
                scene3() # Look around the house
                validResponse = True
            elif(a==3):
                scene4() # Investigate the body
                validResponse = True


def scene2(): # Enquire the husband
    input(f"{player.name}: Hello sir, I am detective {player.name} from the police. Could you please describe everything that happened? Leave no detail out.")
    
    input("\nHusband: Thank you for investigating sir. So I was out on a week long trip from the 27th till yesterday.\n"
    "The last I talked to my wife was at 4 pm, when I asked her whether she wanted me to get some food from outside. She said no, I have something special planned for you. When I reached home at 6, I rang the doorbell, but no-one answered.\n")
    input("I grabbed the spare keys from underneath the decor and opened the door to see this scene. I immediately called the police.")
    input("\nOther police officer: We have enquired other neighbours. Since they live in the heart of the city, no one is usually home before 6pm on a working day. Thus, no one around apart from an old lady next door was at home in this building at the time of this incident.\n")
    print("You write down notes in your notebook.\n")
    overhead.addNote("Husband was out.")
    input(f"{player.name}: Who else could’ve had access to your apartment? Anyone that may have had a motive to kill your wife?")
    input("\nHusband: Well, the old lady next door is always complaining about how loud our TV is in the evenings. Don't let her age fool you, detective.\n"
    "Despite being a 62 year old woman she smokes and has alocohol all the time." 
    "\My wife also worked as a lawyer, so a lot of bad guys she put away could've had a motive.")
    global knowsAboutWork
    knowsAboutWork = True
    overhead.addNote("Worked as a lawyer.")
    validResponse = False
    while(not validResponse):
        overhead.printOverhead(1)
        a = askQuestion("Do you ", ["Look around the room", "Investigate the body", "Investigate the neighbour", "Go to the workplace", "Arrest the Husband"])

        if(a==1):
            scene3() # look around the house
            validResponse = True
        elif(a==2):
            scene4() # Investigate the body
            validResponse = True
        elif(a==3):
            scene5() # Investigate the neighbour
            validResponse = True
        elif(a==4):
            scene6() # Go to the workplace
            validResponse = True
        elif(a==5):
            if(askQuestion("Are you sure you want to arrest the husband?", ["Yes", "No"]) == 1):
                end(1)
                break
            

def scene3(): # Look around the house
    print("You proceed to have a look around the house. Nothing is out of the ordinary.")
    input("You head over to the second room which appears to be normal too. You look inside the bin. There was a packet of pills with a purchase receipt of yesterday.")
    print("You also find a document that was mostly illegible due to yogurt spilt all over it. However, you could make out the words: \n"
    "\"Thank you for purchasing LIVELONG life insurance, Mr and Mrs Jackson.\" and the date, which was 3 days earlier.")
    print("You write down notes in your notepad.\n")
    overhead.addNote("Victim had life insurance.")
    input("You add husband as a suspect.")
    overhead.addSuspect("Husband")
    overhead.printOverhead(2)
    if(knowsAboutWork):
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Investigate the body", "Go to the work place"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene4() # Investigate the body
        if(a==4):
            scene6() # Go to workplace
    else:
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Investigate the body"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene4() # Investigate the body

def scene4(): # Investigate the body
    input("You look at the body closely and find that she had been stabbed around the waist, and her throat had been slit.\n")
    print("Other police officer: The forensic report states that the time of death was around 4:30 pm. Her throat was most likely slit first to ensure she wouldn't be able to scream.\n"
    "She was next stabbed around her lower spine to make her unable to move. She was then slowly layed down by the murderer to not make a sound. She must have died within 5 minutes of the stabbing.\n"\
    "There are no CCTVs in the building, and their apartment was on the tenth floor, so the murderer should've used the door to make his entrance and exit. There are no fingerprints around, and the murder weapon isn't found")
    input()
    print("You take down notes\n")
    overhead.addNote("Time of death: 4:30 pm.")
    overhead.addNote("No fingerprints.")
    overhead.addNote("No murder weapon found.")
    overhead.printOverhead(1)
    if(knowsAboutWork):
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Look around the room", "Go to the work place"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene3() # Look around the room
        if(a==4):
            scene6() # Go to workplace
    else:
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Look around the room"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene3() # Look around the room

def scene5(): # Investigate the neighbour
    print("You head over to the next door. You find the door open. You enter to find an old lady nearly wasted on her couch. She notices you and attempts to stand up.")
    input("You gesture her to stay sitting. You signal the other police officer to search her apartment. He leaves to do so.\n")
    input(f"{player.name}: Evening lady! So you must have heard of the murder next door. Could you tell us anything you know about it?\n")
    input("Old lady: Yes I heard that annoying kid next door died. Pretty brutal to be honest. They blast their speakers every night.\n"
    "I always complain and wonder why am I the only one who can hear their TV so loud. Turns out there is a vent connects our living rooms.\n")
    print(f"{player.name}: So where were you yesterday afternoon at 4 pm.\n")
    print("Old lady: I ran outta booz, so I went to the store a few blocks away to get more.\n"
    "She walks to a drawer, opens it to reveal a mess of papers. After a minute of searching. she hands over a crumpled receipt stating the purchase of some liquor at 4.35 pm.")
    input("Old lady: Here is the receipt.")
    print("The officer returns saying he couldn't find the murder weapon, however he found a knife holder for two knives with a missing knife. The knife matched the description of the murder weapon.\n")
    input("You take down notes.\n")
    overhead.addNote("Old lady was out at 4:30")
    overhead.addNote("Missing knife at neighbour.")
    overhead.addNote("Vent connects the 2 houses.")
    input("You add Old Lady as a suspect.\n")
    overhead.addSuspect("Old Lady")
    validResponse: bool = False
    while(not validResponse):
        overhead.printOverhead(3)
        a = askQuestion("Do you ", ["Look around the room", "Investigate the body", "Enquire the husband", "Go to the workplace", "Arrest the Old Lady"])

        if(a==1):
            scene3() # look around the house
            validResponse = True
        elif(a==2):
            scene4() # Investigate the body
            validResponse = True
        elif(a==3):
            scene2() # Enquire the husband
            validResponse = True
        elif(a==4):
            scene6() # Go to the workplace
            validResponse = True
        elif(a==5):
            if(askQuestion("Are you sure you want to arrest the old lady?", ["Yes", "No"]) == 1):
                end(1)
                break


def scene6(): # Go to workplace
    pass

def game():
    scene1()
    
if(__name__ == "__main__"):
    print("Hello Detective, welcome to New York Police Department's 21st Precinct. Please Enter your name and press Enter/return to proceed: ")
    playerName = str(input())
    clear()
    print(f"Hello {playerName}, we have heard great stories about you, and we require your help to solve a recent case. Let's head to the crime scene.\n\n...\n")
    while True:
        player = Player(playerName, score, 0)
        birthdate = f"{randint(1, 28)}/{randint(1, 12)}/{randint(1980, 2000)}"
        knowsAboutWork = False
        overhead = Overhead()
        overhead.addNote(f"Victim born on {birthdate}")
        game()
        break