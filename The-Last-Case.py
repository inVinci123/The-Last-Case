import os
from random import randint

class Hud: # This class contains all Hud in the game (the map and the notepad) as well as other functions.
    m_suspects: list # This is a list of suspects where possible suspects can be added as the story progresses. Note that the underscore (_) is implies that this property/method is private and is meant to be used in this class only. Only used as a convention.
    m_notes: list # This list will contain important notes that the player can refer to while playing the game
    m_locations = [" ", " ", " ", " ", " ", " ", " ", " "] # These is a list of possible locations the player wants to be on the map. Limited to 8 locations, 4 in the house and 4 in the workplace.
    def HouseMap(self, locations) -> list[str]: # A private function that returns the house map with the player at the desired location. While I used this function as a temporary fix since I was unable to implement it in my intended way, I did decided to leave it since it served the functional purpose.
        return [
        "        CRIME SCENE              Neighbour's ",
        " ____________ __________        ____________ ",
        "|  husband   |     bin  |      |            |",
        f"|     {locations[1]}      |      {locations[2]}   |      |            |",
        "|            |          |      |            |",
        "|      body  |          |      |  neighbour |",
        f"|     {locations[0]}       _         |      |     {locations[3]}      |",
        "|  HALL      |          |      |            |",
        "|            |          |      |            |",
        " ‾‾‾‾\ ‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾\‾‾‾‾‾‾‾ ",
        "                                             "
    ]

    def WorkMap(self, locations) -> list[str]: # A private function similar to the house map function. It returns the workmap with the player at the desired location.
        return [
         "  Work Place             ",
         " ____________ __________ ",
         "|  desk      |     Boss |",
        f"|     {locations[5]}      |      {locations[6]}   |",
         "|             _         |",
         "|     worker |     /    |",
        f"|     {locations[4]}      |‾‾‾‾‾  ‾‾‾|",
        f"| OFFICE     |    {locations[7]}     |",
        f"|            |STOREROOM |",
         " ‾‾‾‾\ ‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾‾ ",
         "                         "
        ]
    
    def __init__(self): # The class constructor. It was intiially meant to initialise all class properties, however, it ended up being an uneccesary intialiser
        self.m_suspects = []
        self.m_notes = []

    def AddNote(self, note): # A simple "setter" function that adds a note to the m_notes property if the note doesn't already exist. While it is possible to directly access the _notes property and append the note from outside the class, I went with the convention. 
        try:
            self.m_notes.index(note)
        except ValueError:
            self.m_notes.append(note)

    def AddSuspect(self, suspect): # A "setter" function that adds a suspect to the m_suspects property. Similar to the addNote function.
        try:
            self.m_suspects.index(suspect)
        except ValueError:
            self.m_suspects.append(suspect)

    def PrintHud(self, location: int = 1) -> None: # An essential function that will create, evaluate and print the Hud on the user screen. Takes in the self parameter (provided by python) and a location parameter, which is used to display the player at a specific location.
        map: list[str] # A scope property initialised a list of strings that will serve as a handler for the map in the Hud.
        for i in range(8): self.m_locations[i] = " " # A simple for loop which makes all locations in the _locations property to a string containing a space " " the space represents absence of the player on the map.
        self.m_locations[location] = "@" # Sets the desired location to the player character symbolised by the "@" character
        if(location < 4): # an if-else statement that assigns the scope variable map to a suitable map determined by the location
            map = self.HouseMap(self.m_locations)
        else:
            map = self.WorkMap(self.m_locations)
        hud: str = "" # Initialising a string scope variable: This will be whats printed in the end
        notepad: list[str] = ["______________________________", # a list of notepad lines. (Could've initialised this in the class to improve performance)
                              "| NOTEPAD:                   |",
                              "|                            |",
                              "| Notes:                     |"
                              ]

        for i in self.m_notes: # a for loop that goes through all the notes and adds them to the notepad lines. It also determines how many spaces are required between each note to make an even notepad.
            spaces = 27 - len(i)
            note = f"| {i}"
            if(spaces >= 0):
                for i in range(spaces):
                    note = f"{note} "
                note = f"{note}|"
            notepad.append(note)
        notepad.append("|                            |") # Appends a blank line to signify the the notes have ended and the next line will be a different section
        notepad.append("| Suspects:                  |") # Header showing that the next lines will display a list of suspects

        for i in self.m_suspects: # a for loop similar to the notes for loop - loops through all suspects and appends them to the notepad.
            spaces = 27 - len(i)
            suspect = f"| {i}"
            for i in range(spaces):
                suspect = f"{suspect} "
            suspect = f"{suspect}|"
            notepad.append(suspect)
        notepad.append("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾") # appends a overline to close the notepad

        spaces = "               " # a scope string that physically represents the amount of space between the notepad and the map in the Hud.
        for i in range(max(len(notepad), len(map))): # a final for loop that loops for the greater of the notepad and map times. It checks whether either notepad or map still have more lines and add them to the Hud variable.
            if(len(notepad) > i and len(map)) > i:
                hud = f"{hud}{map[i]}{spaces}{notepad[i]}\n"
            elif(len(notepad) > i):
                hud = f"{hud}{map[-1]}{spaces}{notepad[i]}\n"
            else:
                hud = f"{hud}{map[i]}\n"
        
        hud = f"{hud} Health remaining = {health}\n"
        hud = f"{hud}""Legend:\n""@ is your position\n" # Add a small legend indicating that the @ symbol is the detectives current location
        print(hud) # print the Hud string


def clear() -> None:  # A function that clears the terminal using a command relevant to both windows and unix based systems
    if(os.name == "nt"):    # check if the os is windows
        os.system("cls") # uses the command cls for windows systems
    else:
        os.system("clear") # uses the command clear for unix (macOS and linux) systems

health: int # a global variable that keeps track of the score
playerName: str # a global variable that stores the players name
Hud: Hud # a global hud object that displays the map and thje notepad
birthdate: str # a global variable that stores the victim's birthdate, randomly generated
knowsAboutWork: bool # a global variable that is set to True if the player has been to scene 2
safeUnlocked: bool # a global variable that is set to True once the victim's secret safe has been unlocked
beenToScene8: bool # a global variable that is set to True once the player visits scene 8

def askQuestion(prompt: str, options: list[str], counter: int = 5) -> str:
    """
    This function will frequently be used to ask the user a question. It returns the index (starting from 1, not 0) of the option that is picked by the user.
    It takes two positional parameters (prompt and options) and one optional parameter (counter)
    prompt is a question prompt that is first displayed.
    options is a list of all options that the user can pick from. Displayed below the prompt.
    counter is an optional parameter that is initialised to the maximum tries the user has to correctly answer the question. It then keeps track of how many tries that person has.
    """
    print(prompt) # prints the prompt
    global health
    health -= 1 # subtracts 1 from the score everytime this function is called

    if(health < 0): # checks whether the school is less than 0. If it is, it will terminate the game saying the detective took too long and the culprit fled
        end(2)
    
    for index, option in enumerate(options, start=1): # prints all the options in this format: [OptionNumber] Option 
        print(f"[{index}] {option}")
    
    answer: int = 0 # answer will be the selected OptionNumber and will be returned at the end.
    while(answer <= 0): # A while loop that checks whether the answer is valid. If it is, it will return the answer, if it isn't it will subtract one from the counter and ask the question again. If the counter runs out, it terminates the program. 
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
    """
    This function takes in the end status (0 is the victory status, 1 is defeat by arresting the wrong person, 2 is defeat by taking too long)
    """
    clear()
    if(status == 0):
        print("Congrats, you won!")
        print("Terry was the murderer. His motive was that Ms Jackson held a lot of evidence against him when she was investigating his corrupt cases.\n"
        "Yesterday at around 4.15 pm, he wore gloves, snuck into the old lady's apartment, which was left open by the drunk lady, and stole her knife. He then climbed through the vent that connected the two houses.\n"
        "Then he waited for her to enter her home, slit her throat before she could scream, and then stabbed her back to prevent her from moving.\n"
        "He then gently lay her down so she wouldn't make a sound when she fell down. He then went back through the vents, exit the house, and disposed the gloves and the murder weapon.")
        print(f"You had {health} health remaining.")
        input("Press Enter/Return to exit")
        clear()
        exit(0)
    elif(status == 1):
        print("You arrested the wrong person! Better luck next time")
        print(f"You had {health} health remaining")
        input("Press Enter/Return to exit")
        clear()
        exit(0)
    elif(status == 2):
        print("You spent too much time on the case, and cancer got better of you.")
        print(f"You had 0 health remaining")
        input("Press Enter/Return to exit")
        clear()
        exit(0)
    else: # This shouldn't ideally run, however it is a last resort if something went terribly wrong.
        print("ERROR, function end() received an invalid status. Exiting...")
        input("Press Enter/Return to exit")
        clear()
        exit(1)

def scene1() -> None: # Opening Scene
    """
    All scenes follow a pattern similar to this one: prompts, hud (map + notepad), and askQuestion for where they want to go next or if they want to arrest the person they're talking to (where relevant)
    """
    validResponse = False
    input("You reach the crime scene, a small well maintained cityside apartment where a young lady of 24 is lying in a pool of blood. Her husband is talking to the police, answering their questions.\n")
    while(not validResponse):
        Hud.PrintHud(0)
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
                validResponse = True
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


def scene2() -> None: # Enquire the husband
    print(f"{playerName}: Hello sir, I am detective {playerName}, the lead investigator on this case. Could you please describe everything that happened? Leave no detail out.\n")
    input("Husband: Thank you for investigating sir. So I was out on a week long trip from the 27th till yesterday.")
    input("The last I talked to my wife was at 4 pm, when I asked her whether she wanted me to take away some food. She said \"No, I got something special planned for you.\" When I reached home at 6, I rang the doorbell, but no one answered.")
    print("I grabbed the spare keys from underneath the decor and opened the door to see this scene. I immediately called the police.")
    input()
    print("Other police officer: We have enquired other neighbours. Since they live in the heart of the city, no one is usually home before 6 pm on a working day. Thus, no one around apart from an old lady next door was at home in this building at the time of this incident.")
    input()
    print("You write down notes in your notebook.")
    Hud.AddNote("Husband was out.")
    input()
    print(f"{playerName}: Do you know anyone that may have the motive to kill your wife?")
    input()
    print("Husband: Not really. Well, the old lady next door is always complaining about how loud our TV is in the evenings. Don't let her age fool you, detective.\n"
    "Despite being a 62 year old woman she smokes and gets wasted all the time." 
    " My wife also worked as a lawyer, so a lot of criminals she put away may have a good reason.")
    input()
    global knowsAboutWork
    knowsAboutWork = True
    Hud.AddNote("Worked as a lawyer.")
    validResponse = False
    while(not validResponse):
        Hud.PrintHud(1)
        a = askQuestion("Do you ", ["Look around the room", "Investigate the body", "Investigate the neighbour", "Go to her workplace", "Arrest the Husband"])

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
            scene6() # Go to her workplace
            validResponse = True
        elif(a==5):
            if(askQuestion("Are you sure you want to arrest the husband?", ["Yes", "No"]) == 1):
                end(1)
                break
            

def scene3() -> None: # Look around the house
    print("You proceed to have a look around the house. Nothing is out of the ordinary.")
    input()
    print("You head over to the second room which appears to be normal too. You look inside a bin. There was a packet of prescription pills with a purchase receipt of yesterday.")
    input()
    print("You also find a document that was mostly illegible since there was yogurt spilt all over it. However, you could make out the words: \n"
    "\"Thank you for purchasing LIVELONG life insurance, Mr and Mrs Jackson.\" and the date, which was only 3 days ago.")
    input()
    print(f"{playerName}: Oh, so the couple purchased a life insurance policy 3 days ago. The husband said he was outside for the past week, but perhaps he was plotting her murder.\n")
    print("You write down notes in your notepad.")
    input()
    Hud.AddNote("Victim had life insurance.")
    print("You add husband as a suspect.\n")
    input()
    Hud.AddSuspect("Husband")
    Hud.PrintHud(2)
    if(knowsAboutWork):
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Investigate the body", "Go to her workplace"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene4() # Investigate the body
        if(a==4):
            scene6() # Go to her workplace
    else:
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Investigate the body"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene4() # Investigate the body

def scene4() -> None: # Investigate the body
    print("You look at the body closely and find that she had been stabbed around the waist, and her throat had been slit.")
    input()
    print("Other police officer: The forensic report states that the time of death was around 4:30 pm. Her throat was most likely slit first to ensure she wouldn't be able to scream.\n"
    "She was next stabbed around her lower spine to make her unable to move. She was then slowly layed down by the murderer to not make a sound. She must have died within 5 minutes of the stabbing.")
    input()
    print("There are no CCTVs in the building, and their apartment was on the tenth floor, so the murderer should've used the door to make his entrance and exit. There are no fingerprints around, and the murder weapon isn't found")
    input()
    print("You take down notes\n")
    Hud.AddNote("Time of death: 4:30 pm.")
    Hud.AddNote("No fingerprints.")
    Hud.AddNote("No murder weapon found.")
    input()
    Hud.PrintHud(0)
    if(knowsAboutWork):
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Look around the room", "Go to her workplace"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene3() # Look around the room
        if(a==4):
            scene6() # Go to her workplace
    else:
        a = askQuestion("Do you: ", ["Enquire the husband", "Investigate the neighbour", "Look around the room"])
        if(a==1):
            scene2() # Enquire the husband
        if(a==2):
            scene5() # Investigate the neighbour
        if(a==3):
            scene3() # Look around the room

def scene5() -> None: # Investigate the neighbour
    print("You head over to the next door. You find the door open. You enter to find an old lady nearly wasted on her couch. She notices you and attempts to stand up.")
    print("You gesture her to stay sitting. You signal the other police officer to search her apartment. He leaves to do so.")
    input()
    print(f"{playerName}: Evening lady! So you must have heard of the murder next door. Could you tell us anything you know about it?")
    input()
    print("Old lady: Yes I heard that annoying kid next door died. Pretty brutal to be honest. They blast their speakers every night.\n"
    "I always complain and wonder why am I the only one who can hear their TV so loud. Turns out there is a vent that connects our living rooms.")
    input()
    print(f"{playerName}: So where were you yesterday afternoon at 4 pm.")
    input()
    print("Old lady: I ran outta booz, so I went to the store a few blocks away to get more. I might have accidentally left the door open.\n"
    "She walks to a drawer, opens it to reveal a mess of papers. After a minute of searching. she hands over a crumpled receipt stating the purchase of some liquor at 4.35 pm.")
    print("Old lady: Here is the receipt.")
    input()
    print("The officer returns saying he couldn't find the murder weapon, however he found a knife holder for two knives with a missing knife. The knife matched the description of the murder weapon.")
    input()
    print("You take down notes.")
    Hud.AddNote("Old lady was out at 4:30")
    Hud.AddNote("Missing knife at neighbour.")
    Hud.AddNote("Vent connects the 2 houses.")
    input()
    print("You add Old Lady as a suspect.")
    input()
    Hud.AddSuspect("Old Lady")
    validResponse: bool = False
    while(not validResponse):
        Hud.PrintHud(3)
        a = askQuestion("Do you ", ["Look around the room", "Investigate the body", "Enquire the husband", "Go to her workplace", "Arrest the Old Lady"])

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
            scene6() # Go to her workplace
            validResponse = True
        elif(a==5):
            if(askQuestion("Are you sure you want to arrest the old lady?", ["Yes", "No"]) == 1):
                end(1)
                break


def scene6() -> None: # Go to her workplace
    print("You reach a busy law firm where the victim used to work. You decide to explore the place.\n")
    input()
    Hud.PrintHud(4)
    a = askQuestion("Do you: ", ["Visit the Victim's desk", "Enquire her co-worker", "Enquire her boss", "Look around the workplace", "Return to the crime scene"])
    if(a==1):
        scene7() # Visit the Victim's desk
    elif(a==2):
        scene8() # Enquire her co-worker
    elif(a==3):
        scene9() # Enquire her Boss
    elif(a==4):
        scene10() # Look around the workplace
    elif(a==5):
        scene1() # Return to the crime scene

def scene7() -> None: # Visit the desk
    print("You walk to the victims desk. You notice that it had been cleaned up. You check out the first 3 drawers. All of them contained nothing. You open the last drawer")
    input()
    print("It is empty")
    input()
    if(not safeUnlocked):
        print("You notice that the fourth drawer was half the length of others. You lift the false end to reveal a mini safe. It required a 4 digit PIN. Next to the safe is a note.")
        input()
        print("It reads \"My special day\"")
        input()
        pin = "" # scope variable that will be passed to the EnterPIN function as the correctPIN
        temp = 0 # temporary variable that keeps track of the amount of slashes encountered in the upcoming for loop

        for i in range(5): # a for loop that appends the digits of the victim's birth date and month
            if(birthdate[i] == '/'):
                temp += 1
                if(temp == 2): break
                if(birthdate[i+1] != "1"):
                    pin += '0'
                continue
            pin += birthdate[i]
        Hud.PrintHud(5)
        EnterPIN(pin) # a function where the player will attempt to crack the PIN of the secret safe
        
    if(safeUnlocked):
        input("You open the secret safe. It reveals some irrelevant private documents. It also reveals a something of interest...")
        input()
        print("You read an anonymous letter addressed to the victim.")
        input()
        print("\"Delete all the evidence you gathered about my corrupt cases before I delete you.\"")
        input()
        print("You have a close look at the letter on the scribbled handwriting.\n"
        "You recognise a familiar fragrance. The ink on the letter had the scent of a special edition PYLOT pen, the one that you used to possess")
        input()
        print("You take notes")
        input()
        Hud.AddNote("Death threats to victim")
        Hud.AddNote("about internal corruption")
        if(beenToScene8):
            print("You add Terry (Co-worker) as a suspect.")
            Hud.AddSuspect("Terry (Co-worker)")
            input()
    
    Hud.PrintHud(5)
    a = askQuestion("Do you: ", ["Visit the Victim's desk again", "Enquire her coworker", "Enquire her boss", "Look around the workplace", "Return to the crime scene"])
    if(a==1):
        scene7() # Visit the desk again
    elif(a==2):
        scene8() # Enquire her co-worker
    elif(a==3):
        scene9() # Enquire her Boss
    elif(a==4):
        scene10() # Look around the workplace
    elif(a==5):
        scene1() # Return to the crime scene
    

def EnterPIN(PIN: str, counter: int = 3) -> None: # this function will give the player 3 attempts to unlock the safe. If they fail to do so, it will simply give them a hint and allow them to retry
    while counter > 0: # loop while the victim still has tries left
        answer: int
        try:
            answer = int(input("Enter PIN: ").strip()) # declare and set answer to the input of the player prompted with "Enter PIN: "
        except ValueError:
            counter -= 1
            print(f"The PIN is wrong. You have {counter} {'tries' if counter != 1 else 'try'} remaining.")
            continue
        if answer == int(PIN): # if the answer is correct, set global variable safeUnlocked to True and return from the function
            global safeUnlocked
            safeUnlocked = True
            return
        else: # The PIN is wrong, so user has one less try
            counter -= 1
            print(f"The PIN is wrong. You have {counter} {'tries' if counter != 1 else 'try'} remaining.")
    else: # If the user runs out of tries, they recieve a hint and are allowed to retry
        print("You run out of tries and fail to open the safe. TIP: the safe pin is the victim's birthday and month, Eg: 0301 for 3rd January")
        return

def scene8() -> None: # Enquire her co-worker
    global beenToScene8
    beenToScene8 = True
    print("You walk to her co worker, Terry.")
    input()
    print(f"{playerName}: Hello sir, you must know about the murder of your co-worker.")
    input()
    print("Co-worker: Yes I do. It was extremely unfortunate. Could you give me a second, I need to sign a document.")
    input()
    print("Terry signs a lengthy document with his special edition PYLOT pen.")
    input()
    print("Terry: Yes officer, so you were saying... ")
    input()
    print(f"{playerName}: I'd like to ask you some questions. Where were you at 4 pm yesterday?")
    input()
    print("Terry: If I remember correctly, I was picking up my children from their school.")
    input()
    print(f"{playerName}: I see. What was your relationship with Ms Jackson like?")
    input()
    print("Terry: Well we were simply co-workers. She often asked me for help on her cases since I am a senior to her.")
    input()
    print(f"{playerName}: Thank you for your time. We shall reach back to you if we need to.")
    input()
    if(safeUnlocked):
        print("You add Terry as a suspect\n")
        Hud.AddSuspect("Terry (Co-worker)")
        input()
    validResponse: bool = False
    while(not validResponse):
        Hud.PrintHud(4)
        a = askQuestion("Do you: ", ["Visit the Victim's desk", "Enquire her boss", "Look around the workplace", "Return to the crime scene", "Arrest the coworker"])
        if(a==1):
            validResponse = True
            scene7() # Visit the desk
        elif(a==2):
            validResponse = True
            scene9() # Enquire her Boss
        elif(a==3):
            validResponse = True
            scene10() # Look around the workplace
        elif(a==4):
            validResponse = True
            scene1() # Return to the crime scene
        elif(a==5):
            if(askQuestion("Are you sure you want to arrest the co-worker?", ["Yes", "No"]) == 1):
                end(0)
    
def scene9() -> None: # Enquire her boss
    print("You visit the victim's boss. As you are about to enter his office, you hear him talking on a call. You decide to eavesdrop.")
    input()
    print("Boss: Yeah, I know there's a lot of corruption in our firm. Frankly, I was afraid she would catch me too.")
    input()
    print("Boss: No no no, it was inevitable. She had poked in too close. If she wasn't murdered, I would have made sure to shush her. Thank god the co-worker...")
    input()
    print("He looks in your direction.\nBoss: I'll talk to you later.")
    input()
    print("Boss (to you): Hey there, who are you?")
    input()
    print(f"{playerName}: Hello there, I am detective {playerName}, the lead investigator in Ms Jackson's murder case. I have some questions for you.")
    input()
    print("Boss: Oh they sent you! Sure detective. Go ahead.")
    input()
    print(f"{playerName}: So sir, I have heard about some corruption business going on here. Could you tell me more about that.")
    input()
    print("Boss: Oh haha well, our firm was being investigated for corruption related offenses. It was mainly some associates that were involved.")
    input()
    print(f"{playerName}: So what was Ms Jackson's role in this.")
    input()
    print("Boss: Miss Jackson was the one who initiated the corruption investigation. She claimed that she had evidence against one of her co-workers, Terry.")
    input()
    print(f"{playerName}: So where was Terry yesterday at 4pm?")
    input()
    print("Boss: He said he had to leave early for some business. He isn't married or has any kids, so he often hangs out at bars with his mates.")
    input()
    print(f"{playerName}: I see. Thank you a lot for your time.")
    input()
    print("You add Boss as a suspect")
    Hud.AddSuspect("Boss")
    input()
    print("You add Terry (Co-worker) as a suspect")
    Hud.AddSuspect("Terry (Co-worker)")
    input()

    validResponse: bool = False
    while(not validResponse):
        Hud.PrintHud(6)
        a = askQuestion("Do you: ", ["Visit the Victim's desk", "Enquire her co-worker", "Look around the workplace", "Return to the crime scene", "Arrest the boss"])
        if(a==1):
            validResponse = True
            scene7() # Visit the desk
        elif(a==2):
            validResponse = True
            scene8() # Enquire her co-worker
        elif(a==3):
            validResponse = True
            scene10() # Look around the workplace
        elif(a==4):
            validResponse = True
            scene1() # Return to the crime scene
        elif(a==5):
            if(askQuestion("Are you sure you want to arrest the boss?", ["Yes", "No"]) == 1):
                end(1)

def scene10() -> None: # Look around the workpalce (and locate the storeroom)
    print("You have a look around the workplace and stumble upon an open storage room. It was filed with files of all sorts.")
    input()
    print("You locate a hidden section beneath an old pile, which interests you. It read 43.6F.72.72.75.70.74 20.43.61.73.65.73")
    input()
    print("You decode the hexadecimal to ASCII. It reads: \"CORRUPT Cases\"")
    input()
    print("It contains a pile of case documents with several notes and highlights. They were all seemed to be about corruption caused by a lawyer called Terry")
    input()
    print("You take notes")
    input()
    Hud.AddNote("Victim had")
    Hud.AddNote("Evidence against Terry")

    Hud.PrintHud(7)
    a = askQuestion("Do you: ", ["Visit the Victim's desk", "Enquire her coworker", "Enquire her boss", "Return to the crime scene"])
    if(a==1):
        scene7() # Visit the desk
    elif(a==2):
        scene8() # Enquire her co-worker
    elif(a==3):
        scene9() # Enquire her Boss
    elif(a==4):
        scene1() # Return to the crime scene

def game(): # the game function that starts from scene 1
    print(f"You find out that you have cancer, and you have {health} health points remaining.")
    input("[Press Enter/Return to continue...]")
    print("Everytime you make a decision, you lose 1 health point.")
    input()
    print("You must solve your final case before you lose all your health points.")
    input()
    clear()
    scene1()
    
if(__name__ == "__main__"): # main function that is executed to start the game

    clear()
    print("Hello Detective, welcome to New York Police Department's 21st Precinct. Please Enter your name and press Enter/return to proceed: ")
    playerName = str(input()) # global variable playerName is set to input
    clear()
    print(f"Hello {playerName}, we have heard great stories about you, and we require your help to solve a recent case. Let's head to the crime scene.\n\n...\n")
    input()
    clear()

    # variable intialisations
    health = 50
    birthdate = f"{randint(1, 28)}/{randint(2, 12)}/{randint(1980, 2000)}"
    knowsAboutWork = False
    safeUnlocked = False
    beenToScene8 = False
    Hud = Hud()
    Hud.AddNote(f"Victim born on {birthdate}")

    # start the game
    game()
