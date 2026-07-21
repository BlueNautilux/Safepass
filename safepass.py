import time, datetime, random, sys, os, pickle, pickletools, logging
from cryptography import fernet
from pyfiglet import Figlet
from colorama import Fore, init

init()

figlet_title = Figlet(font= 'nancyj-fancy')

def clear_terminal():
    sys.stdout.write("\033[3J\033[H\033[2J") #shortcut for clearing the terminal with scrollback (this will be changed)
    sys.stdout.flush()

def check_for_file():
    if not os.path.exists("passwords.txt"):
        with open ("passwords.txt", "x") as f:
            pass

def check_if_empty():
    if os.path.getsize("passwords.txt") == (0):
        print('this file is empty')

def passwordmanager():
    clear_terminal()
    check_for_file()
    print(figlet_title.renderText('safepass'))
    print('=======================================================================')
    def optionselectionui():
        readmetxt = (Fore.LIGHTBLACK_EX + '(Views the contents of README.txt)' + Fore.RESET)
        readtxt = (Fore.LIGHTBLACK_EX + '(Lists all passwords inside the .txt file)' + Fore.RESET)
        writetxt = (Fore.LIGHTBLACK_EX + '(Appends new text to the .txt file)' + Fore.RESET)
        deletealltxt = (Fore.LIGHTBLACK_EX + '(it deletes the contents of the .txt file)' + Fore.RESET)
        writetxt = (Fore.LIGHTBLACK_EX + '(Appends new text to the .txt file)' + Fore.RESET)
        exittxt = (Fore.LIGHTBLACK_EX + '(Closes the application)' + Fore.RESET)
        print(f'[1.] [ Open README.txt ] {readmetxt}')
        print(f'[2.] [       Read      ] {readtxt}')
        print(f'[3.] [     Add new     ] {writetxt}')
        print(f'[4.] [    Delete All   ] {deletealltxt}')
        print(f'[5.] [       Exit      ] {exittxt}')
    
    optionselectionui()
    print('=======================================================================')    
    uichoice = input('[1-5]: ').strip()
    
    match uichoice:
        case "1":
            def openreadme():
                clear_terminal()
                print()
                with open ("README.txt") as f:
                    print(f.read())
                    readmechoice = input('Would you like to go back (Y) or (N):').strip().lower()
                    match readmechoice:
                        case "y":
                            passwordmanager()

                        case "n":
                            openreadme()
                        
                        case _:
                            print("Invalid input, Try again!")
                            time.sleep(1)
                            clear_terminal()
                            openreadme()
            openreadme()

        case "2":
            def openpasswords():
                with open ("passwords.txt") as f:
                    print(f.read())
                    readmechoice = input('Would you like to go back (Y) or (N):').strip().lower()
                    
                    match readmechoice:
                        
                        case "y":
                            passwordmanager()

                        case "n":
                            openpasswords()

                        case _:
                            print("Invalid input, Try again!")
                            time.sleep(1)
                            clear_terminal()
                            openreadme()
            openpasswords()
        
        case "3":
            clear_terminal()
            inputanewpasswordname = input('Label: ')
            clear_terminal()
            inputanewpassword = input('Password: ')
            clear_terminal()
            newpassword = {f"{inputanewpasswordname}: {inputanewpassword}"}
            
            if not os.path.getsize("passwords.txt") == (0):
                with open ("passwords.txt", "a") as f:
                    f.write(f"{newpassword}\n\n")
                    f = open("passwords.txt")
                    print(f.read())
                    time.sleep(3)
                    clear_terminal()
                    passwordmanager()

            elif os.path.getsize("passwords.txt") == (0):
                with open ("passwords.txt", "w") as f:
                    f.write(f"{newpassword}")
                    f = open("passwords.txt")
                    print(f.read())
                    time.sleep(3)
                    clear_terminal()
                    passwordmanager()
            
            else: 
                print('error returning to main_menu')
            
        case "4":
            with open ("passwords.txt", "w") as f:
                pass
            passwordmanager()

        case "5":
            sys.exit()

        case _:
            print('Invalid input, Try again!')
            time.sleep(1)
            clear_terminal()
            passwordmanager()

passwordmanager()