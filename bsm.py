#!/usr/bin/env python3
# bsm.py
# Simple browser simulation

import webbrowser as wb
import sys, os

def cl():
    os.system('cls'if os.name=='nt'else'clear')

def validator(func):
    def wrapper(url):
        while True:
            
            # HTTPS_CHECK
            if 'https://' in url and '.' in url:
                func(url)
                break
            
            # HTTP_WARNING
            elif 'http://' in url and '.' in url:
                usr = input('This is a HTTP. Do YOU want to continue? <Y/n> ').lower().strip()
                if usr == 'n':
                    print(f'\nBROWSER has been stopped... \n')
                    sys.exit()
                else:
                    func(url)
                    break
            
            # TRY_AGAIN_OR_QUIT
            else:
                usr = input('URL is INCORRECT! Try again? <Y/n> ').lower().strip()
                if usr == 'n':
                    print(f'\nBROWSER has been stopped... \n')
                    sys.exit()
                else:
                    url = input('Enter the URL YOU want to visit: ').lower().strip()
    return wrapper


@validator
def open_url(url):
    cl()
    wb.open(url)

# MAIN_LOOP
def main():
    cl()
    url = input('Enter the URL YOU want to visit: ').lower().strip()
    open_url(url)

# STARTING_MAIN_LOOP

try:
    while True:
        main()
except KeyboardInterrupt:
    print(f'\nBROWSER has been stopped... \n')
    sys.exit()
