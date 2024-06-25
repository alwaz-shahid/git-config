import os
import subprocess
import sys
import pyfiglet

def set_git_user(username, email):
    subprocess.run(["git", "config", "--global", "user.name", username])
    subprocess.run(["git", "config", "--global", "user.email", email])

def view_git_config():
    try:
        result = subprocess.run(["git", "config", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except FileNotFoundError:
        print("Git is not installed. Please install Git and run this tool again.")
        sys.exit(1)

def show_logo():
    ascii_art = pyfiglet.figlet_format("Git Config Tool", font="slant")
    print(ascii_art)

def main():
    show_logo()

    # Prompting for username and email
    username = input("Enter your Git username: ")
    email = input("Enter your Git email: ")

    set_git_user(username, email)
    print("Git global user configuration has been set.")

    # Optionally, you can add a menu or another option here to allow the user to perform other actions like viewing the config

if __name__ == "__main__":
    main()
