import requests, sys, getopt
from bs4 import BeautifulSoup

website = None;
element = None;
help = """
📜 Web Scrapper Help :
===================

Flags :
-------

-h | --help       Help  
-w | --website    Website url without protocol
-e | --element    Element to be recovered
"""
warning = """
⚠️  Warning
==========

This website doesn\'t exist !
"""

try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        'hw:e:',
        ['website=', 'element=', 'help']
    )
except getopt.GetoptError:
    print(help)
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print(help)
        sys.exit()
    elif opt in ('-w', '--website'):
        website = arg
    elif opt in ('-e', '--element'):
        element = arg

if website != None and element != None:
    try:
        requests = requests.get('https://' + website)
        page = requests.content
        soup = BeautifulSoup(page, 'html.parser')
        for target in soup.find_all(element):
            print(target)
    except Exception:
        print(warning)
else:
    print(help)
