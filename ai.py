from twill.commands import *

#ai = your course full page path


def __login__():
	try:
		print("trying  to login!")
		go('your_university_lms_platform_path')
		showforms()
		fv('1', 'username', 'yourusername')
		fv('1', 'password', 'yourpassword')
		submit('0')
	except Exception as e:
		exit()


__login__()

try:
	go(ai)
	showforms()
except Exception as e:
	exit()
	

