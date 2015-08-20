
__author__ = 'fahad'

from bs4 import BeautifulSoup
import urllib2
import re
import threading


def search_headings(url,inp):
    page = urllib2.urlopen(url)  # getting the page
    soup = BeautifulSoup(page.read(), "lxml")  # Reading the Page using XMLX Parser
    store = str(soup.body.find_all(text=re.compile(inp))) # Search string in the BODY of the Page
    st = store.split(',')
    # Split String based on COMMAS
    print "Getting Words Searched from: %r" % url
    print "******* REQUESTED *************"
    if st != '[]':
        for i in range(0, len(st)):
            print(st[i])
            print "\n"

    print"***********************************************************"



def start():
    # URL's from where you want to search your data
    url = "http://www.theguardian.com/uk/technology"
    url1 = "http://www.reddit.com/r/programming"
    url3 = "http://news.ycombinator.com"
    url4 = "http://www.nytimes.com"
    # List of URL's
    u = [url, url1, url3, url4]
    threads = []
    print"***********************************************************"
    print"************ SEARCH WORDS ON WEBSITE **********************"
    print"***********************************************************"
    # Getting words to be searched fom websites
    inp = raw_input("Enter Words to be Searched:")
    for i in range(0, len(u)):
        # Calling function to search Headings
        thread = threading.Thread(target=search_headings, args=[u[i], inp, ])
        thread.start()
        threads.append(thread)

    print "********  WAITING FOR THREADS TO COMPLETE THEIR TASKS  ********"

    for thread in threads:
        thread.join()

    print "***************** THREADS HAVE COMPLETED THEIR TASKS !!! **********************."



start()