# -*- coding: utf-8 -*-

# Dirty hack to get emails of members out of Yahoo Groups
#
# Written to get the B3ta newsletter out of Yahoo Groups
# by http://twitter.com/robmanuel
#
# It uses Python to spin up Chrome,
# logs in and then calls the internal API that 
# makes the members page and then spits out a load
# of json files which you can fiddle with or grep.
#
# As I said, this aint pretty but it got a job done
# and might be useful to someone with same problem.
# 
# grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" *txt | uniq | sort
# useful grep to get the emails out
#
# and another to count them as a bit of a sanity check
# grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" *txt | uniq | sort | wc -l
#


group="b3ta"
size_of_group=72299
username="b3ta_collective"
password="********"

# You're going to have to download Chromedriver
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# and stick full path and file name here:

location_of_cromedriver="/Users/robmanuel/yahoo/yahoogroups-members-downloader/chromedriver"

############
# Nothing to see below here except dragons
############

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, random

browser = webdriver.Chrome(location_of_cromedriver)

browser.get('https://login.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(username)
emailElem.submit()

passwordElem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "login-passwd"))
)
passwordElem.send_keys(password)
passwordElem.send_keys(Keys.ENTER)

print "WE'RE IN, I THINK - GOOD LUCK!"

start=0
count=100
end=size_of_group+100

while start <= end:
	browser.get("https://groups.yahoo.com/api/v1/groups/"+group+"/members/confirmed?start="+str(start)+"&count="+str(count)+"&sortBy=name&sortOrder=asc&chrome=raw&tz=America%2FLos_Angeles&ts=1525273459549")
	elem = browser.find_element_by_xpath("//*")
	source_code = elem.get_attribute("outerHTML")
	start+=count
	
	print group,start, end
	
	file = open(group+"_"+str(start)+".txt","w") 

	# This is a horrible hack because I couldn't remember how unicode works
	
	source_code = source_code.encode('ascii', 'ignore').decode('ascii')

	try:
	 	file.write (source_code.decode("UTF-8"))
	except:
		print "nope"
		
 	time.sleep(random.randrange(10,15))
 	file.close() 

print "HOORAY! I'VE SAVED YOU - SUPPORT THE B3TA PATREON - https://www.patreon.com/b3ta"
