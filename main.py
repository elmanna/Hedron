"""
Developed By © Ahmad  Almnna {{Aka JasonDz}}
Hedron V1.0
"""


from datetime import datetime
import requests
import sys
import os
from twill.commands import *
from time import sleep


first_run = False

#error list for different errors that can face u during connecting to
#the course site, if the code found any error
#in the secondary course file it will avoid it & will cancel 
#the operation and continue to the next course checking
_errors_list = ["Connection aborted", "cannot go to"]


#here you have to rename this dictionary according to your courses
#mine were 

##Ai
##web_tech
##multimedia
##javafx
##softeng2
##database_apps
##mod_sim

courses_files_names = {
	"ai_main": r"Main\ai_main.txt",
	"ai_second": r"Secondary\ai_second.txt",
	"web_main": r"Main\web_main.txt",
	"web_second": r"Secondary\web_second.txt",
	"multimedia_main": r"Main\multimedia_main.txt",
	"multimedia_second": r"Secondary\multimedia_second.txt",
	"javafx_main": r"Main\javafx_main.txt",
	"javafx_second": r"Secondary\javafx_second.txt",
	"softeng2_main": r"Main\softeng2_main.txt",
	"softeng2_second": r"Secondary\softeng2_second.txt",
	"database_apps_main": r"Main\database_apps_main.txt",
	"database_apps_second": r"Secondary\database_apps_second.txt",
	"mod_sim_main": r"Main\mod_sim_main.txt",
	"mod_sim_second": r"Secondary\mod_sim_second.txt"
}


def clear_window():
	os.system("cls")

def __login__():
	print("trying  to login!")
	go('https://lms.ust.edu.sd/')
	output = showforms()
	fv('1', 'username', 'yourusername')
	fv('1', 'password', 'yourpassword')
	submit('0')


def __touch__(name):
	#making initializing empty main files according to the list above
	os.system("call > %s"%(name))


def __check__main_files__():
	global first_run
	if not os.path.isfile(courses_files_names["ai_main"]):
			print("initializing main files!")
			try:
				os.system("md Main && md Secondary")
			except:
				pass
			
			first_run = True
			sleep(2)
			#initialize main files
			__touch__(courses_files_names["ai_main"])
			__touch__(courses_files_names["web_main"])
			__touch__(courses_files_names["multimedia_main"])
			__touch__(courses_files_names["javafx_main"])
			__touch__(courses_files_names["softeng2_main"])
			__touch__(courses_files_names["database_apps_main"])
			__touch__(courses_files_names["mod_sim_main"])



__check__main_files__()


def _sendMsg_(msg):
    #here you can do what ever action you want in my case 
    #i want to send a notification msg to a telegram group
    pass
    """url = f"https://api.telegram.org/bot<yourTelegramBotToken>/sendMessage?chat_id=<chatIDyouwantToSendTheMsgTo>&text=%s" %msg
    requests.get(url)"""


def _errors_(filename):
	global _errors_list
	with open(filename) as f:
		datafile = f.readlines()
		print("read data from %s"%filename)
		for line in datafile:
			print("line ------> %s"%line)
			for _error in _errors_list:
				if _error in line:
					print("error ----> %s"%_error)
					return True
		return False 


############################
#m : main  txt file size, s : secondary txt file size
#m_path : main file txt path, s_path : second file txt path
#main_name : main file name


def _CourseCheck_(m, s, m_path, s_path, main_name, coursename):
	global first_run

	print("m: %s s: %s"%(m, s))

	#if the secondary file size is less than the main & there is no errors in the
	#secondary file then there is a new lecture or an new activity happend to the 
	#course page
	#then the script will rename the secondary file as the main & it will replace it 
	#as the new main file, so its the latest update
	if ((s > m) and not _errors_(s_path)):
				if not first_run:
					sleep(2)
					os.system("del %s"%(m_path))
					print("renaming Secondary to Main...")
					sleep(1)
					os.system("ren %s %s "%(s_path, main_name))
					print("Done renaming ...")
					sleep(1)
					print("moving to Main folder")
					sleep(1)
					os.system(r"move Secondary\%s %s"%(main_name, "Main/"))
					sleep(3)
					return True
				else:
					print("First Run Skip Alert Moving File to Main")
					sleep(2)
					os.system("del %s"%(m_path))
					print("renaming Secondary to Main...")
					sleep(1)
					os.system("ren %s %s "%(s_path, main_name))
					print("Done renaming ...")
					sleep(1)
					print("moving to Main folder")
					sleep(1)
					os.system(r"move Secondary\%s %s"%(main_name, "Main/"))
					sleep(3)
					return False	
				
	else:
		print ("||||>>>>nothing new in %s course<<<<||||"%(coursename))
		sleep(2)
		os.system("del %s"%(s_path))
		return False





def _main_():
	global courses_files_names, first_run, destination_channel_username
	#global client, phone, token, api_hash, api_id, chat
	_sendMsg_(">>>>>Started....")
	while True:
		try:

			"""Ai"""
			clear_window()
			print("|||||>>> Checking Ai Course <<<|||||")
			os.system("python3 ai.py > %s"%(courses_files_names["ai_second"]))
			sleep(7)

			ai_m = os.stat(courses_files_names["ai_main"])
			ai_s = os.stat(courses_files_names["ai_second"])
			
			#check if the courseCheck function returned true, (new update) so execute the blew actions
			if _CourseCheck_(m=ai_m.st_size, s=ai_s.st_size, m_path=courses_files_names["ai_main"], s_path=courses_files_names["ai_second"], main_name="ai_main.txt", coursename="Ai"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New Ai Lecture تحديث او محاضرة جديدة للذكاء الأصطناعي")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Ai lecture is uploaded!")
			else:
				#print("Nothing new")
				pass
					


			#same thing to all other courses below


			"""web_tech"""
			clear_window()
			print("|||||>>> Checking Web Technologies & Services Course <<<|||||")
			os.system("python3 web_tech.py > %s"%(courses_files_names["web_second"]))
			sleep(7)

			web_m = os.stat(courses_files_names["web_main"])
			web_s = os.stat(courses_files_names["web_second"])
			
			if _CourseCheck_(m=web_m.st_size, s=web_s.st_size, m_path=courses_files_names["web_main"], s_path=courses_files_names["web_second"], main_name="web_main.txt", coursename="Web Technologies & Services"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New Web_Tech Lecture   تحديث او محاضرة جديدة لتقنيات وخدمات الويب")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Web Technologies lecture is uploaded!")
			else:
				pass
				
			"""multimedia"""
			clear_window()
			print("|||||>>> Checking Multimedia Course <<<|||||")
			os.system("python3 multimedia.py > %s"%(courses_files_names["multimedia_second"]))
			sleep(7)

			multimedia_m = os.stat(courses_files_names["multimedia_main"])
			multimedia_s = os.stat(courses_files_names["multimedia_second"])
			
			if _CourseCheck_(multimedia_m.st_size, multimedia_s.st_size, courses_files_names["multimedia_main"], courses_files_names["multimedia_second"], "multimedia_main.txt", coursename="Multimedia"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New Multimedia Lecture  تحديث او محاضرة جديدة لتقنيات الوسائط المتعددة ")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Multimedia lecture is uploaded!")
			else:
				pass
				
				
				"""javafx"""
			clear_window()
			print("|||||>>> Checking Advanced OPP Course <<<|||||")
			os.system("python3 javafx.py > %s"%(courses_files_names["javafx_second"]))
			sleep(7)

			javafx_m = os.stat(courses_files_names["javafx_main"])
			javafx_s = os.stat(courses_files_names["javafx_second"])
			
			if _CourseCheck_(javafx_m.st_size, javafx_s.st_size, courses_files_names["javafx_main"], courses_files_names["javafx_second"], "javafx_main.txt", coursename="Advanced OPP"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New JavaFx Lecture  تحديث او محاضرة جديدة للبرمجة الموجهة المتقدمة  ")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Advanced OPP  lecture is uploaded!")
			else:
				pass
					
			"""softeng2"""
			clear_window()
			print("|||||>>> Checking Software Engineering 2 Course <<<|||||")
			os.system("python3 softeng2.py > %s"%(courses_files_names["softeng2_second"]))
			sleep(7)

			softeng2_m = os.stat(courses_files_names["softeng2_main"])
			softeng2_s = os.stat(courses_files_names["softeng2_second"])
			
			if _CourseCheck_(softeng2_m.st_size, softeng2_s.st_size, courses_files_names["softeng2_main"], courses_files_names["softeng2_second"], "softeng2_main.txt", coursename="Software Engineering 2"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New SoftwareEng2 Lecture  تحديث او محاضرة جديدة لهندسة البرمجيات ")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Software Engineering 2  lecture is uploaded!")
			else:
				pass
				

			"""database_apps"""
			clear_window()
			print("|||||>>> Checking Database Apps Development Course <<<|||||")
			os.system("python3 database_apps.py > %s"%(courses_files_names["database_apps_second"]))
			sleep(7)

			database_apps_m = os.stat(courses_files_names["database_apps_main"])
			database_apps_s = os.stat(courses_files_names["database_apps_second"])
			
			if _CourseCheck_(database_apps_m.st_size, database_apps_s.st_size, courses_files_names["database_apps_main"], courses_files_names["database_apps_second"], "database_apps_main.txt", coursename="Database Apps Development"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New DB apps Development Lecture  تحديث او محاضرة جديدة تطوير تطبقيات قواعد البيانات  ")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Database Apps Development  lecture is uploaded!")
			else:
				pass
					

			"""mod_sim"""
			clear_window()
			print("|||||>>> Checking Modeling & Simulation Course <<<|||||")
			os.system("python3 mod_sim.py > %s"%(courses_files_names["mod_sim_second"]))
			sleep(7)

			mod_sim_m = os.stat(courses_files_names["mod_sim_main"])
			mod_sim_s = os.stat(courses_files_names["mod_sim_second"])
			
			if _CourseCheck_(mod_sim_m.st_size, mod_sim_s.st_size, courses_files_names["mod_sim_main"], courses_files_names["mod_sim_second"], "mod_sim_main.txt", coursename="Modeling & Simulation"):
					_sendMsg_(">>>>>>>Hedron_bot<<<<<<<")
					_sendMsg_("--->>>> New Modeling & Simulation Lecture  تحديث او محاضرة جديدة للنمذجة و المحاكاة  ")
					_sendMsg_("Date: %s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					_sendMsg_(">>>>>>>>>Hedron_bot<<<<<<<<<")
					#print("|#|+++++>>>>>> NEW Modeling & Simulation  lecture is uploaded!")
			else:
				first_run = False
				

			clear_window()
			print("|->>>sleeping for 3mins...")
			sleep(180)
		except Exception as e:
			pass


_sendMsg_(">>>>>>>Booting Hedron ")
_sendMsg_(">>>>>>AlmnnaDev © 2021<<<<<<<")
sleep(2)

#here executing dead script which handle the application crash 
#or when u stop it, it receives the process id of the hedron main
#process so when it stopped it detect it and let you to do
#specific action upon that event
os.system("start python3 dead.py %s"%(os.getpid()))

_main_()

