#!/usr/bin/python
# -*- coding: utf-8 -*-
import thread
import smtplib
import time
import os
import getpass
import sys
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
foundemail = []



class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''
***************************************************
***************************************************
***            ################    ###
***            ###############    ####
***            ##############    #####
***            ####             ######
***            ####            #######
***            ###########    #### ###
***            ###########   ####  ###
***            ####          ####  ###
***            ####    ###    ########
***            ####    ####    ##  ###
***            ####    #####    #  ###
***            #######################
***            #######################
***            #######################
***************************************************
***************************************************
''' + bcolors.ENDC

os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('Banner File not found')

#Input
print(bcolors.WARNING + '''
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:

	from1 = raw_input(bcolors.OKGREEN + 'From: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + 'Subject (Optional): ' + bcolors.ENDC)
	#body = raw_input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	#nomes = input(bcolors.OKGREEN + 'Jumlah List: ' + bcolors.ENDC)
	
	#setup smtp
	user = 'Applelm9y0xljl353_deaktivierteskonto0@dekativerenkonbestellunto.services'
	pwd = '@@Kontol123'
	server = '1'
	no = 0
	no2 = 1
	isi = 0
	body = 'Apple Support'

	#setup list
	with open('lists/list.txt') as f:
  	  print sum(1 for _ in f)


	#setup from name
	asd = """
	Dear Customer
	"""
	seko = from1 + '<' + user + '>'
	message = 'From: ' + seko + '\nSubject: ' + subject + '\n' + body + 'Content-Type: text/html' + '\n' + asd


except KeyboardInterrupt:
	print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
	sys.exit()

	#fungsi send
if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()

	#perulangan send
	while no != 'NULL':
		try:
			mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
			for line in open("lists/list.txt"):
				foundemail.extend(mailsrch.findall(line))
				#for isi in foundemail[(no2+1):(no+1)]:
				for isi in foundemail[(no2+1):(no+1)]:
					to1 = (isi)
			to = 'Bcc: ' + isi
	  		server.sendmail(user, to, message)
	  		print bcolors.WARNING + 'Successfully sent ' + str(no+1) + ' ' + to1 + bcolors.OKGREEN
			no += 1
			no2 +=1
			time.sleep(0)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send "
	server.close()