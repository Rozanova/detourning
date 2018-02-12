# reading python reviews with Lyrebird
# by katya rozanova (working off of the code of aaron montoya-moraga'a its-ok-to-thank)
# project for detouring the web at itp nyu
# python script to automate pasting strings from json file into Lyrebird and downloading them onto my computer
# february 2018


# instructions

# install virtualenv on the machine
# pip install virtualenv env

# instantiate a virtual environment
# virtualenv env

# activate the instance of the virtual environment
# source env/binc/activate

# install selenium
# pip install selenium

# to deactivate the virtual environment
# deactivate

# import sys, time, string, json modules
import sys
import time
import string
import json

# import selenium module for web automation
# include webdriver for using chrome and eys for using keyboard commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# global variables for waiting time
waitTime = 1
waitTimeLong = 30

# main function declaration

def main():

    json_file = "./" + sys.argv[1]

    print "read json file for mails"

    # read json file
    json_data = open(json_file).read()

    # load json file to data
    data = json.loads(json_data)

    print "parse info from file reviews.json"

    # figure out the length of the data
    print len(data)

    # initalize empty array to hold all the comments
    reviews = []

    # iterate through every element in the data`
    for i in range(len(data)):
        # append to the comments array every commentText from the json file
        reviews.append(data[i]["body"])

    # confirm that the length matches with the length of the json file
    print len(reviews)

    print "number of comments to record: " + str(len(reviews))

    print "open google chrome"

    # new driver using google chrome
    driver = webdriver.Chrome()

    # set the window size of the driver
    driver.set_window_size(900, 600)

    print "go to Lyrebird"

    # url
    url = "https://lyrebird.ai"

    # go to the url
    driver.get(url)

    # wait
    time.sleep(waitTime)

    # wait
    time.sleep(waitTimeLong)

    # go through every comment in comments
    # for comment in comments

    for review in reviews:

        try:
            # wait
            time.sleep(waitTime)

            print "input text"

            # retrieve inputbox
            inputBox = driver.find_element_by_id('text-entry')

            time.sleep(waitTime)

            # input text to the input box
            inputBox.send_keys(review)

            time.sleep(waitTime)

            # hit enter on the input box
            inputBox.send_keys(Keys.ENTER)

            time.sleep(waitTime)
            time.sleep(waitTime)

            audio = driver.find_element_by_tag_name("audio")
            print audio

            # print "trying to load action chains"
            # action = webdriver.common.action_chains.ActionChains(driver)
            #
            # print "trying to move to element with offset"
            # action.move_to_element_with_offset(audio, 280, 16)
            #
            # print "trying to click"
            # action.click()
            #
            # print "perform"
            # action.perform()

        except Exception as e:
                print "this failed:"

# execute main
main()
