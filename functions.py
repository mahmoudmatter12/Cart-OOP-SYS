from fileinput import filename
from random import randint
from time import time
import os
from colorama import Fore, Back, Style, init
import sys
import tty
import termios
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import json
from datetime import datetime

filename = "Data.json"

#!===========================================================
#! lab 1
def calc_time(inner_time):
    def wrap(*args, **kwargs):
        start = time()
        inner_time(*args, **kwargs)
        end = time()
        print("Function time is", end - start, "s")

    return wrap


#!===========================================================
def clear_file(filename):
    with open(filename, "w") as file:
        file.write("")
        print(f"File {filename} cleared")


def Greeting_Customer(name):
    print(Fore.MAGENTA + f"Hello {name}, Welcome to our store"+ Style.RESET_ALL)
    print("-" * (28 + len(name)))

def Greeting_User(name):
    print(Fore.MAGENTA + f"Hello {name}, Welcome to our System"+ Style.RESET_ALL)
    print("-" * (29 + len(name)))

def Greeting_Admin(name):
    print(Fore.MAGENTA + f"Hello {name}, Welcome to our Admin Panel"+ Style.RESET_ALL)
    print("-" * (30 + len(name)))


def Clean():
    os.system("cls" if os.name == "nt" else "clear")


def input_password(prompt="Enter your password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = read_char()
        if char == "\n":
            break
        elif char == "\r":
            break
        elif char == "\x7f":  # Backspace key
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            password += char
            sys.stdout.write("*")
            sys.stdout.flush()
    print()  # Move to the next line after password input
    return password

def read_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

def load_users(filename):
    try:
        with open(filename, "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file is not found or empty
    return users


def find_user(email):
    users = load_users(filename)
    for user in users:
        if user["email"] == email:
            return user
    return None


def get_emails():
    users = load_users(filename)
    emails = [user["email"] for user in users]
    return emails


