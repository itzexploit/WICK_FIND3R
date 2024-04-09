from requests import get
from colorama import Fore , init
from pystyle import Colorate , Colors 
from os import name , system
from threading import Thread as thr

init()

system('cls' if name == 'nt' else 'clear')

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

banner = f'''
   {yellow}_   _   _   _     _   _   _   _   _   _  
  {yellow}/ \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
 {yellow}( {green}W {yellow}|{green} I {yellow}|{green} C {yellow}|{green} K {yellow}) ( {red}F {yellow}|{red} I {yellow}|{red} N {yellow}|{red} D {yellow}| {red}3 {yellow}|{red} R {yellow})
  {yellow}\_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ 
'''

print(banner)
print(Colorate.Horizontal(Colors.red_to_blue,'									Created By John Wick',2))
print(Colorate.Horizontal(Colors.red_to_purple,'	  					  	Team Pytho Learn',1))

target = input(f'\n{red}[{yellow}+{red}] {cyan}Enter Your Target Ip Addres {red}:{green} ')

def main():
    response = get(f"http://ip-api.com/json/{target}")
    response.raise_for_status()
    data = response.json()
    isp = data['as']
    city = data['city']
    zone = data['timezone']
    rgname = data['regionName']
    country = data['country']
    print(f'{cyan}\n {red}[{yellow}+{red}]{cyan} ISP {red}:{green} {isp}\n{cyan} {red}[{yellow}+{red}]{cyan} CITY {red}:{green} {city}/{rgname}\n {red}[{yellow}+{red}]{cyan} TIME_ZONE {red}:{green} {zone} \n{cyan} {red}[{yellow}+{red}]{cyan} COUNTRY {red}:{green} {country}')
    print(f'\n  {red}[{yellow}+{red}] {blue}x{red}D {yellow}Bye {cyan}Bye')
        
thr(target=main).start()