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

import os
from time import sleep

# Other Functions
def deleat_url(value_pair):
    # The 'value_pair' is a string in format [ file_name : link/url ]
    value_pair=str(value_pair)
    file_name=value_pair.partition(':')[0].strip()

    # Deleating The Records from logs/list
    delete_matching_line("logs/links.txt", value_pair)
    delete_matching_line("logs/shorturls.txt", file_name)
    print(f"{file_name} has been deleted form the records....")

    #Deledating The HTML file
    filename=f"public/{file_name}.html"
    try:
        os.remove(filename)
        print(f"Successfully deleted {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except PermissionError:
        print(f"No permission to delete {filename}")
    except Exception as e:
        print(f"Error deleting file: {e}")

def delete_matching_line(filename, line_to_delete):
    #Creating a temporary file
    temp_filename = f"{filename}.tmp"

    #Removing the line
    with open(filename, 'r') as orignal, open(temp_filename, 'w') as temfile:
        for line in orignal:
            if line.strip() != line_to_delete.strip():
                temfile.write(line)

    os.replace(temp_filename, filename)


# For 1st Case
def find_url():
    RECORD="logs/links.txt"

    #Searching for results
    while True:
        print("\033c", end="")
        SEARCH=str(input("\nEnter a Search Query : "))
        MATCHED_RESULTS={}
        INDEXING_RESULTS=0

        #Exit Funtction
        if SEARCH=='0':
            exit()

        with open(RECORD, 'r') as f:
            for line in f:
                if SEARCH.strip().lower() in line.strip().lower():
                    INDEXING_RESULTS += 1
                    MATCHED_RESULTS.update({INDEXING_RESULTS: line.strip()})

        if MATCHED_RESULTS:
            print("Found Some Results....\n")
            for i in MATCHED_RESULTS:
                print(f"[{i}]  {MATCHED_RESULTS[i]}")
            print(f"[0]  None/Exit") 
            print(f"[*]  All") 
            break
        else:
            print("Unable to find any results....")
            print("Exit [0]")
            sleep(2)
            continue
    

    #Selction Menu
    while True:
        TO_DELEAT = input("\nWhat Do You Want to Deleat : ")
        if str(TO_DELEAT)=="*":
            TO_DELEAT=str(TO_DELEAT)
            break
        else:
            try:
                TO_DELEAT=int(TO_DELEAT)
                break
            except:
                print("Enter a Valid option.")
                continue


    if type(TO_DELEAT) == int:
        #Exit Funtction
        if TO_DELEAT==0:
            exit()

        #Getting the Values Pairs
        if TO_DELEAT:
            deleat_url(MATCHED_RESULTS[TO_DELEAT])
    elif type(TO_DELEAT) == str:
        #For deleatign all the entries
        for each_item in MATCHED_RESULTS:
            deleat_url(MATCHED_RESULTS[each_item])
    else:
        print("Error: Unknow variable type....")

#For 2nd Case
def list_all():
    RECORD="logs/links.txt"
    RESULTS={}
    INDEXING_RESULTS=0

    with open(RECORD, 'r') as f:
        for line in f:
            if line.strip().lower():
                INDEXING_RESULTS += 1
                RESULTS.update({INDEXING_RESULTS: line.strip()})

    print("\033c", end="")
    print("Showing All The Records\n")
    if RESULTS:
        NO_RECORD_FOUND=False
        for i in RESULTS:
            print(f"[{i}]  {RESULTS[i]}")
        
        print(f"[*]  All")
    else:
        print("No Records found...")
        print(f"[0]  None/Exit")
        NO_RECORD_FOUND=True

    if NO_RECORD_FOUND:
        while True:
            TO_DELEAT = input("\nWhat Do You Want to Deleat : ")
            if str(TO_DELEAT)=='0':
                exit()
            else:
                print("Enter a valid Option")
                continue
    
    else:
        #Selction Menu
        while True:
            TO_DELEAT = input("\nWhat Do You Want to Deleat : ")
            if str(TO_DELEAT)=="*":
                TO_DELEAT=str(TO_DELEAT)
                break
            else:
                try:
                    TO_DELEAT=int(TO_DELEAT)
                    break
                except:
                    print("Enter a Valid option.")
                    continue


        if type(TO_DELEAT) == int:
            #Exit Funtction
            if TO_DELEAT==0:
                exit()

            #Getting the Values Pairs
            if TO_DELEAT:
                deleat_url(RESULTS[TO_DELEAT])
        elif type(TO_DELEAT) == str:
            #For deleating all the entries
            for each_item in RESULTS:
                deleat_url(RESULTS[each_item])
        else:
            print("Error: Unknow variable type....")


def run_DeleatMe():
    """------------------Main Code------------------"""

    print("\033c", end="")
    print("This Program is made to deleat the url pages.")
    print("\n[0] Exit Anywhere\n[1] Find URL/Page \n[2] List all URLS (Default)")

    mode=str(input("\n : "))

    if mode=='1':
        find_url()
    elif mode=='2':
        list_all()
    elif mode=='0':
        exit()
    elif len(mode)==0:
        list_all()
    else:
        print("Enter a Valid Opton....")

if __name__=='__main__':
    Welcome_message=r'''
    ----------------------------------------------------------------------------------
                                
                     _____       _            _   _             
                    |  __ \     | |          | | (_)            
                    | |  | | ___| | ___  __ _| |_ _ _ __   __ _ 
                    | |  | |/ _ \ |/ _ \/ _` | __| | '_ \ / _` |
                    | |__| |  __/ |  __/ (_| | |_| | | | | (_| |
                    |_____/ \___|_|\___|\__,_|\__|_|_| |_|\__, |
                                                           __/ |
                                                          |___/ 

    ----------------------------------------------------------------------------------
                            Copyright (C) 2025 Akrit Behera
    '''

    print("\033c", end="")
    print(Welcome_message)
    sleep(2)
    run_DeleatMe()