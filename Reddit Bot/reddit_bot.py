
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 
import time

class reddit_bot:

    def __init__(self):
        global keyword
        keyword = input("enter key: ")
        print("intialized")  
        # self.username=username
        # self.password=password
        self.bot=webdriver.Firefox() 


    # def get_keyword(self):
    #     # keyword = raw_input("What is your name? ")
    #     keyword = input("Enter keyword")


    def open_and_login(self):
        bot=self.bot
        #url='https://www.reddit.com/r/FashionRepsBST/search/?q=' +keyword+ '&restrict_sr=1'
        url = 'https://www.reddit.com/r/FashionRepsBST/search/?q='+ keyword +'&restrict_sr=1&sort=new'
        # bot=webdriver.Firefox() 
        bot.get(url)
        time.sleep(5)
        # email=bot.find_element_by_name('username')
        # password=bot.find_element_by_name('password')

        # try:
        #     div=bot.find_elements_by_class_name('s60uip8-0 dlqFPG')
        #     time.sleep(10)
        #     rel = [el.find_element_by_class_name('johij4-4 kfkmvh').click() for el in div]
        # except Exception as ex:
        #     print("error")


obj = reddit_bot()
# obj.get_keyword()       
obj.open_and_login()
