import os
import subprocess
import sys
import argparse
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
    parser = argparse.ArgumentParser(description="Manage Git global user configuration.")
    parser.add_argument("--set", nargs=2, metavar=("username", "email"), help="Set Git global user. If no arguments are provided, the tool will prompt for username and email.")
    parser.add_argument("--view", action="store_true", help="View Git global user configuration.")

    args = parser.parse_args()

    show_logo()

    if args.set:
        username, email = args.set
        set_git_user(username, email)
        print("Git global user configuration has been set.")
    elif args.view:
        view_git_config()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
