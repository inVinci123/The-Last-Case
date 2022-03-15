class Overhead: # This class contains all overhead in the game (the map and the notepad) as well as other functions.
    m_suspects: list # This is a list of suspects where possible suspects can be added as the story progresses. Note that the underscore (_) is implies that this property/method is private and is meant to be used in this class only. Only used as a convention.
    m_notes: list # This list will contain important notes that the player can refer to while playing the game
    m_locations = [" ", " ", " ", " ", " ", " ", " ", " "] # These is a list of possible locations the player wants to be on the map. Limited to 8 locations, 4 in the house and 4 in the workplace.
    def _houseMap(self, _locations) -> list[str]: # A private function that returns the house map with the player at the desired location. While I used this function as a temporary fix since I was unable to implement it in my intended way, I did decided to leave it since it served the functional purpose.
        return [
        "        CRIME SCENE              Neighbour's ",
        " ____________ __________        ____________ ",
        "|  husband   |     bin  |      |            |",
        f"|     {_locations[1]}      |      {_locations[3]}   |      |            |",
        "|            |          |      |            |",
        "|      body  |          |      |            |",
        f"|     {_locations[0]}       _         |      |            |",
        "|  HALL      |          |      |  neighbour |",
        f"|            |          |      |  {_locations[2]}         |",
        " ‾‾‾‾\ ‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾\‾‾‾‾‾‾‾ ",
        "                                             "
    ]
    def _workMap(self, _locations) -> list[str]: # A private function similar to the house map function. It returns the workmap with the player at the desired location.
        return [
            "  Work Place             ",
            " ____________ __________ ",
            "|  desk      |     Boss |",
        f"|     {_locations[5]}      |      {_locations[6]}   |",
            "|             _         |",
        f"|     worker |     / {_locations[7]}  |",
        f"|     {_locations[4]}      |‾‾‾‾‾  ‾‾‾|",
            "| OFFICE     |          |",
        f"|            |STOREROOM |",
            " ‾‾‾‾\ ‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾‾ ",
            "                         "
        ]
    
    def __init__(self): # The class constructor. It was intiially meant to initialise all class properties, however, it ended up being an uneccesary intialiser
        self.m_suspects = []
        self.m_notes = []

    def addNote(self, note): # A simple "setter" function that adds a note to the _notes property. While it is possible to directly access the _notes property and append the note from outside the class, I went with the convention. 
        self.m_notes.append(note)

    def addSuspect(self, suspect): # A "setter" function that adds a suspect to the "_suspects" property. Similar to the addNote function.
        self.m_suspects.append(suspect)

    def printOverhead(self, location: int = 1) -> None: # An essential function that will create, evaluate and print the overhead on the user screen. Takes in the self parameter (provided by python) and a location parameter, which is used to display the player at a specific location.
        map: list[str] # A scope property initialised a list of strings that will serve as a handler for the map in the overhead.
        for i in range(8): self.m_locations[i] = " " # A simple for loop which makes all locations in the _locations property to a string containing a space " " the space represents absence of the player on the map.
        self.m_locations[location] = "@" # Sets the desired location to the player character symbolised by the "@" character
        if(location < 4): # an if-else statement that assigns the scope variable map to a suitable map determined by the location
            map = self._houseMap(self.m_locations)
        else:
            map = self._workMap(self.m_locations)
        overhead: str = "" # Initialising a string scope variable: This will be whats printed in the end
        notepad: list[str] = ["______________________________", # a list of notepad lines. (Could've initialised this in the class to improve performance)
                              "| NOTEPAD:                   |",
                              "|                            |",
                              "| Notes:                     |"
                              ]

        for i in self.m_notes: # a for loop that goes through all the notes and adds them to the notepad lines. It also determines how many spaces are required between each note to make an even notepad.
            spaces = 27 - len(i)
            note = f"| {i}"
            if(spaces > 0):
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

        spaces = "               " # a scope string that physically represents the amount of space between the notepad and the map in the overhead.
        for i in range(max(len(notepad), len(map))): # a final for loop that loops for the greater of the notepad and map times. It checks whether either notepad or map still have more lines and add them to the overhead variable.
            if(len(notepad) > i and len(map)) > i:
                overhead = f"{overhead}{map[i]}{spaces}{notepad[i]}\n"
            elif(len(notepad) > i):
                overhead = f"{overhead}{map[-1]}{spaces}{notepad[i]}\n"
            else:
                overhead = f"{overhead}{map[i]}\n"
        
        print(overhead) # print the overhead string
