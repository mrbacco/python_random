# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:54:52 2020

@author: mrbacco
"""

###################### imports START ######################

import csv
import random
import time
from datetime import datetime
import tweepy
import logging

###################### imports END ######################

###################### logger setup START ######################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###################### logger setup END ######################

###################### tw_api func START ######################

auth = tweepy.OAuthHandler("xxxx", 
                           "xxxx")
auth.set_access_token("xxxx",
                          "xxxx")

# API object to use for everything
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    logger.info("logged in, thanks")
except:
    logger.info("errors during authentication, try again")

###################### tw_api func END ######################


###################### Tweet update START ######################

with open('source.csv', "r", errors="ignore", newline='') as f1:
    spamreader = csv.reader(f1, delimiter=',')
    source=[i for row in spamreader for i in row]

with open('adjectives.txt', "r") as f2:
    spamreader = csv.reader(f2, delimiter=',')
    adj=[i for row in spamreader for i in row]

print(len(source))
print(len(adj))

marks = ["!", ".", ".", "?", ".", "!!!", ".", ".", "."]

n = 1
while n >= 0:

    num1 = random.randrange(0,67248)    # source
    num2 = random.randrange(0,9)        # marks
    num3 = random.randrange(0,5301)     # adj
    num4 = random.randrange(0,5301)     # adj2

    x = random.randrange(0,12)

    now = str(datetime.now().replace(microsecond=0))
    
    sentence1 = ("%s %s "%(random.choice(source), random.choice(adj)))
    sentence2 = (adj[num3] + ": " + source[num1] + " " + marks[num2])
    sentence3 = (now + ": thought of the moment ... " + adj[num4])

    #print(sentence1 + "\n")
    #print(sentence2 + "\n")
    #print(sentence3 + "\n")

    if x % 3 ==0:
        print("\n", "1 ... status update with: ", "\n",sentence1)
        api.update_status(sentence1)
        print("x = " + str(x))
        time.sleep(60*11)
    
    elif x % 5 ==0:
        print("\n", "2 ... status update with: ", "\n",sentence2)
        api.update_status(sentence2)
        print("x = " + str(x))
        time.sleep(60*23)

    else:
        print("\n", "3 ... status update with: ", "\n",sentence3)
        api.update_status(sentence3)
        print("x = " + str(x))
        time.sleep(60*74)

###################### Tweet update END ######################

