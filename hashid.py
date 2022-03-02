#Thanks to hashes.com for web
#Coded by Kenzawa A.K.A Babwa
from colorama import Fore
b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX
import requests, argparse
import bs4
parse = argparse.ArgumentParser()
parse.add_argument('-i', '--hash', help='Input hash')
parse.add_argument('-f', '--file', help='scanning hash in the file')
args = parse.parse_args()

def hashid(hash):
    data = {
        "hashes": hash,
        "submitted": "true"
    }
    a = requests.post('https://hashes.com/en/tools/hash_identifier',data=data)
    soup = bs4.BeautifulSoup(a.content, 'html.parser')
    try:
        result = c + soup.find('div', {'class': 'py-1'}).text
    except:
        result = red + 'Hash Not Found'
    return result

if args.hash:
    print(hashid(args.hash))
if args.file:
    anu = open(args.file, 'r')
    print(hashid(anu))
