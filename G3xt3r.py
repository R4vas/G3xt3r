import os
import time
import requests
from tkinter import messagebox

def function():
    # Simplified wait animation using a loop
    print("Wait", end="")
    for _ in range(10):  # 10 iterations, change as needed
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()  # New line after animation

def get_subdomains_from_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        subdomains = set()  # Using a set to avoid duplicates
        for entry in response.json():
            subdomain = entry['name_value']
            for sub in subdomain.split('\n'):
                if domain in sub:
                    subdomains.add(sub.strip())
        return subdomains
    else:
        print(f"Failed to retrieve data for {domain}")
        return []

def main():
    print("""\033[0;31m                                                                
         ..-'''-.                          ..-'''-.             
         \.-'''\ \                         \.-'''\ \            
  .--./)        | |                               | |           
 /.''\\      __/ /                      .|     __/ /   .-,.--.  
| |  | |    |_  '.   ____     _____   .' |_   |_  '.   |  .-. | 
 \`-' /        `.  \`.   \  .'    / .'     |     `.  \ | |  | | 
 /("'`           \ '. `.  `'    .' '--.  .-'       \ '.| |  | | 
 \ '---.          , |   '.    .'      |  |          , || |  '-  
  /'""'.\         | |   .'     `.     |  |          | || |      
 ||     ||       / ,' .'  .'`.   `.   |  '.'       / ,'| |      
 \'. __//-....--'  /.'   /    `.   `. |   /-....--'  / |_|      
  `'---' `.. __..-''----'       '----'`'-' `.. __..-'           
    """)
    print("\033[0;32m[~] This tool is for BruteForcing subdomains")
    print("[1] Are you interested in knowing my telegram account?")
    choice = input("\033[0;33mY/n==========>> ").strip()

    if choice.lower() == "y":
        print("\033[0;33m==============>> t.me/Xpid3r")
        print("Welcome")
        function()  # Wait animation
    else:
        function()  # Wait animation
    
    # Subdomain enumeration part
    domain = input("Enter the domain (e.g., example.com): ")
    subdomains = get_subdomains_from_crtsh(domain)
    if subdomains:
        for i in range(50):
            print("*",end="",flush=True)
            time.sleep(0.5)
        print(f"Subdomains found for {domain}:")
        for subdomain in subdomains:
            print(subdomain,flush=True)
    else:
        print(f"No subdomains found for {domain}.")

if __name__ == "__main__":
    main()

