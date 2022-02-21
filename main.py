from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *



class twitter_bot:
	def __init__(self,username,password):
		self.username=username
		self.password=password
		self.bot=webdriver.Firefox()


	def login(self):
		bot=self.bot
		bot.get('https://www.facebook.com/login/')
		time.sleep(5)
		email=bot.find_element_by_id('email')

		password=bot.find_element_by_id('pass')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(10)


	def like_tweet(self,entry3):
		bot=self.bot
		bot.get('https://www.facebook.com/search/posts/?q='+str(entry3))
		while True:

			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)
			pyautogui.click(pyautogui.locateCenterOnScreen('2.png'),duration=2);
            
			time.sleep(3)







def execute():
	log=twitter_bot(str(entry1.get()),str(entry2.get()))
	log.login()
	log.like_tweet(entry3.get())



window=Tk()
window.geometry("700x600")
emails=Label(window,text="enter your email/phone here",font='times 24 bold',fg="#9933ff")
emails.grid(row=0,column=0)
entry1=Entry(window)
entry1.grid(row=0,column=6)


password=Label(window,text="enter your password here",font='times 24 bold',fg="#9933ff")
password.grid(row=2,column=0)
entry2=Entry(window)
entry2.grid(row=2,column=6)


hashtag=Label(window,text="enter your Hashtag here",font='times 24 bold',fg="#9933ff")
hashtag.grid(row=3,column=0)
entry3=Entry(window)
entry3.grid(row=3,column=6)

b1=Button(window,text=" GO ",command=execute,width=12,bg='#bfff00')
b1.grid(row=7,column=4)
window.mainloop()







