#!/usr/bin/env python
#
# 
#
# extract-m3u.py - Extracts usernames and passwords from get.php?username=test&password=test links.
#
# By @RandomRobbie
# 
#

import sys
import argparse
import os.path
import re



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="",required=True, help="File of urls")


args = parser.parse_args()
urls = args.file



def extract_it(url):
	try:
		username = re.compile("username=(.+?)&").findall(url)[0]
		password = re.compile("password=(.+?)&").findall(url)[0]
		text_file1 = open("usernames.txt", "a")
		text_file1.write(""+username+"\n")
		text_file1.close()
		text_file2 = open("passwords.txt", "a")
		text_file2.write(""+password+"\n")
		text_file2.close()
		text_file3 = open("combo.txt", "a")
		text_file3.write(""+username+":"+password+"\n")
		text_file3.close()

	except Exception as e:
		print('Error: %s' % e)


if os.path.exists(urls):
		with open(urls, 'r') as f:
			for line in f:
				url = line.replace("\n","")
				try:
					print("Extracting Creds "+url+"")
					extract_it(url)
				except KeyboardInterrupt:
					print ("Ctrl-c pressed ...")
					sys.exit(1)
				except Exception as e:
					print('Error: %s' % e)
					pass
		f.close()
	