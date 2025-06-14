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

import DeleatMe
import AddMe
from time import sleep

Welcome_message=r'''
----------------------------------------------------------------------------------
         _    _      _    _____ _                _                       
        | |  | |    | |  / ____| |              | |                      
        | |  | |_ __| | | (___ | |__   ___  _ __| |_ ___ _ __   ___ _ __ 
        | |  | | '__| |  \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
        | |__| | |  | |  ____) | | | | (_) | |  | ||  __/ | | |  __/ |   
         \____/|_|  |_| |_____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|   


----------------------------------------------------------------------------------
                        Copyright (C) 2025 Akrit Behera

            This program comes with ABSOLUTELY NO WARRANTY; This is free 
            software and you are welcome to redistribute it under certain 
                    conditions; for details look into LICENSE.
'''

print("\033c", end="")
print(Welcome_message)
sleep(2)

print("\033c", end="")
print("\n[0] Exit Anywhere\n[1] Add URLS (Default) \n[2] Deleate URLS")
mode=str(input("\n : "))

if mode=='1':
    AddMe.run_AddMe()
elif mode=='2':
    DeleatMe.run_DeleatMe()
elif mode=='0':
    exit()
elif len(mode)==0:
    AddMe.run_AddMe()
else:
    print("Enter a Valid Opton....")