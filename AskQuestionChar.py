"""
def askQuestion(prompt, options, counter = 10):
    answer = chr(64) # if answer is 0, the answer is invalid
    print(prompt)
    a = 0
    for i in options:
        print(f"{chr(65+a)}: {i}")
        a+=1
    while(ord(answer)-64) <= 0:
        try:
            answer = str(input("Enter a letter: ").strip()).upper() # set answer to one of the options
            if(ord(answer)-64)> len(options) or (ord(answer)-64) <= 0: # Invalid input check
                raise ValueError # jump to except
        except ValueError:
            if(counter != 0):
                counter -= 1
                print(f"Invalid Value, print one of the options, eg: A. {counter} tries remaining.")
            else:
                break
        except TypeError:
            temp = list(answer.upper())
            answer = chr(0)
            for i in temp:
                for j in range(len(options)):
                    if(i == chr(65+j)):
                        answer = i
                        return(answer)
            
            if(counter != 0):
                counter -= 1
                print(f"Invalid Value, print one of the options, eg: A. {counter} tries remaining.")
            else:
                break

    return(answer)
"""


def askQuestion(prompt, options, response = "Your answer: ", counter = 3) -> str: # prompt is the question prompt, options is a list of all options for the users, response is a response prompt, and a counter is the number of invalid tries the user has before the program terminates
    prompt+="\n" # add a new line to the prompt string so the options can be displayed below the prompt
    for i, option in enumerate(options): # an enumerated for loop that adds all the options to the prompt string so they can be displayed to the user
        prompt += f"{chr(65+i)} {option}\n"
    
    while counter > 0: # while the user has invalid tries remaining
        answer = input((prompt + response)) # the answer is requested as an input. The prompt is a a concatenated string of the question prompt and the response prompt.
        for char in answer.strip().upper():  # a for loop that runs for every character in the requested input
            for i in range(len(options)): # a nested for loop that runs for all possible options, and checks whether the character is a valid answer.
                if char == chr(65+i): # if the character in question is a suitable character,
                    return char # return options[i] # we can return the character OR we can return the option.
        else: # if the for loop fails and there are no suitable characters in the string, the counter goes down and the user is warned that the value is invalid and they have counter tries remaining.
            counter -= 1
            print(f"Invalid Value, enter one of the options. You have {counter} tries remaining.")

    print("Game Over! You ran out of tries!") # if the user runs out of tries, its a game over.
    exit() # terminates the program. (add an input() before terminating so it doesn't terminate quickly and gives time to the user to read the final message)

x = askQuestion("What is 43+12?", ["214521", "5", "235", "598"])
print(x)