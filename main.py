# List of available exits
available_exit = ['UpRight']

# Initializing the chosen exit variable
chosen_exit = ''

# Loop until a valid exit is chosen
while chosen_exit not in available_exit:
    # Prompt the user for their location
    chosen_exit = input('Where are you? ')
    
    # If the chosen exit is the correct one, print victory messages and break the loop
    if chosen_exit == 'UpRight':
        print('You are saved')
        print('You win')
        break
else:
    # If the loop completes without a valid exit, print a consolation message
    print('You got out on first try')
