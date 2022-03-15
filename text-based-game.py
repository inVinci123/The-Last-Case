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

def end(status: int):
    clear()
    if(status == 0):
        print("Congrats, you won!")
        print(f"You final score was {score}")
        exit(0)
    elif(status == 1):
        print("Unfortunately, you did not win!")
        print(f"Your final score was {score}")
        exit(0)
    else:
        print("ERROR, function end() received an invalid ")

def scene1():
    input("You reach the crime scene, a small well maintained cityside apartment where a young lady of 24 is lying in a pool of blood. Her husband was talking to the police, answering their questions.\n")
    overhead.printOverhead(0)
    a = askQuestion("Do you:", ["Enquire the husband", "Investigate the body", "Look around the room"])
    if(a==1):
        scene2()
    elif(a==2):
        scene3()
    elif(a==3):
        scene4()

def scene2():
    input(f"{player.name}: Hello sir, I am detective {player.name} from the police. Could you please describe everything that happened? Leave no detail out.")
    
    input("\nHusband: Thank you for investigating sir. So I was out on a week long trip from the 27th till yesterday.\n"
    "The last I talked to my wife was at 4 pm, when I asked her whether she wanted me to get some food from outside. She said no, I have something special planned for you. When I reached home at 6, I rang the doorbell, but no-one answered.\n")
    input("I grabbed the spare keys from underneath the decor and opened the door to see this scene. I immediately called the police.")
    input("\nOther police officer: We have enquired other neighbours. Since they live in the heart of the city, no one is usually home before 6pm on a working day. Thus, no one around apart from an old lady next door was at home in this building at the time of this incident.\n")
    print("You write down notes in your notebook.\n")
    overhead.addNote("Husband was out.")
    input(f"{player.name}: Who else could’ve had access to your apartment? Anyone that may have had a motive to kill your wife?")
    input("\nHusband: Well, the old lady next door is always complaining about how loud our TV is in the evenings. Don't let her age fool you, detective.\n"
    "Despite being a 62 year old woman she smokes and has alocohol all the time.")
    a = askQuestion("Prompt 2", ["opt 2"])
    if(a==1):
        scene1()
    elif(a==2):
        scene3()
    elif(a==3):
        scene4()

def scene3():
    pass

def scene4():
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
        overhead = Overhead()
        overhead.addNote(f"Victim born on {birthdate}")
        game()
        break