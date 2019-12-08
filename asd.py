import re #allows program to use regular expressions
import json
foundemail = []
#this is an empty list

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
for line in open("lists/list.txt"):
    foundemail.extend(mailsrch.findall(line))
for isi in foundemail[0:1]:
      to1 = (isi)
      #to = 'Bcc: ' + to1
      #print 'Successfully sent ' + ' ' + to1
      print to1

with open('lists/list.txt') as f:
    print sum(1 for _ in f)