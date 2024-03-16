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


# || ACTUAL CODES ||
# - 