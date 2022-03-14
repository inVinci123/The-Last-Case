import os
from overhead import Overhead
from player import Player

def clear() -> None:
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clear()
score = 0
overhead: Overhead
player: Player

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
                print(f"Not a valid number. Please enter a valid number that is one of the options, eg: 1. You have {counter} tries remaining."
                if counter > 1 else
                f"Not a valid number. Please enter a valid number that is one of the options, eg: 1. You have {counter} try remaining.")
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
def game():
    overhead.addNote("Hello World.")
    overhead.addNote("Random note.")
    overhead.addNote("Another random note.")
    overhead.addSuspect("John Doe")
    overhead.printOverhead(0)
if(__name__ == "__main__"):
    while True:
        player = Player("inVincible", score, 0)
        overhead = Overhead()
        game()