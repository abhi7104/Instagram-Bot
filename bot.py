from selenium import webdriver
from time import sleep
from secret import email,pwd
class instabot:
    def __init__(self,username,password):
        self.driver= webdriver.Chrome(executable_path='./driver/chromedriver')
        self.driver.get("https://instagram.com")
        sleep(2)
        #Email field
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
            .send_keys(email)
        #Password field
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pwd)
        #Login
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')\
            .click()
        sleep(5)
        self.driver.get("https://instagram.com")
        #NOT NOW
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
            .click()
        sleep(2)
        #NOT NOW
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
        sleep(2)
        #search for hashtag
    def Hashtag(self):
        hashtag=input("Enter Hashtag to search: ")
        self.driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        sleep(2)
        #top post open
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")\
            .click()
        sleep(2)
    def like_post(self):
        #like the post
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")\
            .click()
        sleep(1)
        #move over to next post
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")\
            .click()
        sleep(1)
        total = int(input("Enter how many post you want to like: "))
        i=0
        while i<total:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")\
                .click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")\
                .click()
            sleep(2)
            i=i+1
    def post_comment(self):
        comment1=input("Enter the comment: ")
        #click on textarea to comment
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")\
            .click()
        sleep(1)
        #enter comment on post
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")\
            .send_keys(comment1)
        sleep(1)
        #post the comment
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button")\
            .click()
        #move over to next post
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")\
            .click()
        sleep(1)
        j=0
        total1=int(input("Enter number of comments to be posted: "))
        while j<total1:
            #click on textarea to comment
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")\
                .click()
            sleep(1)
            #enter comment on post
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")\
                .send_keys(comment1)
            sleep(1)
            #post the comment
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button")\
                .click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")\
                .click()
            sleep(2)
            j=j+1
    def close(self):
        self.driver.close()
while True:
    print('''
    Enter your choice:
    1. To Login and Search HashTag
    2. To Like Post
    3. To Comment on Post
    4. To Close the Browser
    5. To Exit

    ''')   
    choice = int(input(">>>"))

    if(choice==1):
        bot=instabot(email,pwd)
        bot.Hashtag()
    elif(choice==2):
        bot.like_post()
    elif(choice==3):
        bot.post_comment()
    elif(choice==4):
        bot.close()
    elif(choice==5):
        break
    else:
        print("Enter valid choice")