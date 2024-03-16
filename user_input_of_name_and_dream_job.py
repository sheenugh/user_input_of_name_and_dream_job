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
def animate_text(text, color=Fore.WHITE, style=Style.NORMAL, delay=0.002):
    for char in text:
        print(f"{color}{style}{char}", end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)
    
# - Code for the content or asking the user about his name and dream job
def main():
    animate_text("Welcome to the Q and A Chatbox!", Fore.GREEN, Style.BRIGHT)
    print("Data Privacy Act:", end='')
    animate_text("RA 10173, also known as the Data Privacy Act, aims to protect the citizens’ right to their personal, sensitive information. By continuing to fill out this form, you consent to submit your own data, which the data manager promises to not publish or disclose any information without due consent or permission of its owner.", Fore.MAGENTA, Style.BRIGHT)
    print("Would you like to proceed?(Yes/No)") 
    asking_if_proceeding = input("Enter your response:")
    
    if asking_if_proceeding == "Yes":
        animate_text("Please enter your name: ", Fore.YELLOW, Style.DIM)
        name = input()
        animate_text(f"Hello, {name}!", Fore.CYAN, Style.NORMAL, 0.1)
        animate_text("Nice to meet you.", Fore.MAGENTA, Style.BRIGHT)
    
    else:
        asking_if_proceeding == "No"
        print("Thank you for your time.")



if __name__ == "__main__":
    main()

# || ACTUAL CODES ||
# - 