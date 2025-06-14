'''   
    Copyright (C) 2025  Akrit Behera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import random
import string
import os
from urllib.parse import urlparse
from time import sleep


"""-----------STORAGE FILES-----------"""
#Storage file for the names which are automatically generated
STORAGE_FILE = "logs/shorturls.txt"
LOG_FILE ="logs/links.txt"

""" ------------FUNCTIONS------------ """
#Function to Generate random names
#Oprating on the Storage File
def load_generated_strings():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE) as f:
            return set(line.strip() for line in f)
    return set()

def save_generated_string(string):
    with open(STORAGE_FILE, 'a') as f:
        f.write(string + '\n')

def generate_unique_string(length=6):
    #Generate a unique random string of letters with file storage
    existing = load_generated_strings()
    while True:
        candidate = ''.join(random.choices(string.ascii_letters, k=length))
        if candidate not in existing:
            save_generated_string(candidate)
            return candidate


#Function to add names to the existing list
def add_cutom_name_to_lits(candidate):
    existing = load_generated_strings()
    if candidate not in existing:
        save_generated_string(candidate)
    else:
        print("-------- This name has alredy been used.....-------- \nPlease Choose another name.")
        exit()

# Function to Check URL Validity
def check_website(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])


def run_AddMe():
    '''============= Main Code ==========='''

    """ ------------INPUT------------ """
    print("\033c", end="")
    print("This Program is made to add the url pages.\n")


    #Getting the URL
    url_to_shorten=str(input("Enter The URL Your Want to Shorten \nEx. https://google.com : "))

    #Checking if the url input it empty
    if len(url_to_shorten)==0:
        print("-------- Please Provide a URL ! --------")
        exit()
    elif url_to_shorten=='0':
        exit()
    #Checkign if the url is valid
    elif check_website(url_to_shorten):
        pass
    else:
        print(f"-------- Invalid URL : {url_to_shorten} --------")
        exit()


    # Getting the Short Name
    url_shortened_name=str(input("\nEnter The Name For Your Shortned URL \nEx. mygoole, Leave Empty for Automatic : "))

    #Checking for names,
    if len(url_shortened_name)==0:
        #Automatic URl Name..
        url_shortened_name=generate_unique_string()
    elif url_shortened_name=='0':
        exit()
    else:
        #Adding the short name to the available list
        add_cutom_name_to_lits(url_shortened_name)


    with open(LOG_FILE, 'a') as f:
        string=f"{url_shortened_name} : {url_to_shorten}"
        f.write(string + '\n')



    """ -------------FILE GENERATION------------- """

    html_file = f"public/{url_shortened_name}.html"
    base_html_file = "template.html"

    # Writing Content in the files
    with open(html_file, 'a') as file:
        with open(base_html_file, 'r') as base_file:
            base_code = base_file.read()
            replaced_code = base_code.replace("REDIRECTIONLINK", f"{url_to_shorten}")
            file.write(replaced_code)

    print(f"\n\n\nForm now on you can visit {url_to_shorten}\n at https://yourdomain.com/{url_shortened_name}")

if __name__=='__main__':
    Welcome_message=r'''
    ----------------------------------------------------------------------------------

                                     _     _ _             
                            /\      | |   | (_)            
                           /  \   __| | __| |_ _ __   __ _ 
                          / /\ \ / _` |/ _` | | '_ \ / _` |
                         / ____ \ (_| | (_| | | | | | (_| |
                        /_/    \_\__,_|\__,_|_|_| |_|\__, |
                                                      __/ |
                                                     |___/ 

    ----------------------------------------------------------------------------------
                            Copyright (C) 2025 Akrit Behera
    '''
    print("\033c", end="")
    print(Welcome_message)
    sleep(2)
    run_AddMe()