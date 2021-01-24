import requests, sys, getopt
from bs4 import BeautifulSoup

website = None;
element = None;
try:
  opts, args = getopt.getopt(sys.argv[1:],'hw:e:',['website=','element='])
except getopt.GetoptError:
  print('app.py -w <website> -e <element>')
  sys.exit(2)

for opt, arg in opts:
  if opt == '-h':
     print('app.py -w <website> -e <element>')
     sys.exit()
  elif opt in ('-w', '--website'):
     website = arg
  elif opt in ('-e', '--element'):
     element = arg

if website != None and element != None:
	requests = requests.get('https://' + website)
	page = requests.content
	soup = BeautifulSoup(page, 'html.parser')
	for target in soup.find_all(element):
	    print(target)
else:
	print('app.py -w <website> -e <element>')
