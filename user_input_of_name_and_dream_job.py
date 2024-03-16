# Delima, Sheena Mae D.
# BSCPE 1-2
# March 16, 2024

# -----------------------------------------------------------------------------

# # ========= PSEUDO CODE =========
# || LIBRARIES/PACKAGES ||
import time
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform ANSI color support
init()


# || FUNCTIONS ||
# - Code for the animated text
def animate_text(text, color=Fore.WHITE, style=Style.NORMAL, delay=0.05):
    for char in text:
        print(f"{color}{style}{char}", end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)
    
# - Code for the content or asking the user about his name and dream job
def main():
    animate_text("Welcome to the Q and A Chatbox!", Fore.GREEN, Style.BRIGHT)
    print("\n")
    animate_text("Data Privacy Act:", Fore.RED, Style.BRIGHT)
    print("RA 10173, also known as the Data Privacy Act, aims to protect the citizens’ right to their personal, sensitive information. By continuing to fill out this form, you consent to submit your own data, which the data manager promises to not publish or disclose any information without due consent or permission of its owner.")
    print("\n")
    animate_text("Would you like to proceed? (Yes/No)", Fore.CYAN, Style.BRIGHT) 
    print("Enter your response: ")
    response = input()
    
    if response == "Yes":
        animate_text("Please enter your name: ")
        name = input()
        animate_text(f"Hello, {name}!", Fore.MAGENTA, Style.NORMAL, 0.1)
        animate_text("Nice to meet you.", Fore.MAGENTA, Style.BRIGHT, 0.1)
        response2_any_response = input("Type any response:")
        
        print("\n")
        animate_text("What is your dream job?: ")
        response3_dream_job = input()
        
        print("\n")
        animate_text("That's magnificent! Keep pursuing your dream and do not give up. Okay?")
        input("Response: ")
        
        animate_text("Well, then, thank you for your time and have a great day!")
        
        print("\n")
        # - Information of the user
        print("INFORMATION OF THE USER")
        print("Name:", name)
        print("Dream Job:", response3_dream_job)
    
    else:
        if response == "No":
            print("Thank you for your time.")
        else:
            if response != "Yes" and "No":
                print("Please follow the format.")



if __name__ == "__main__":
    main()

# || ACTUAL CODES ||
# - 