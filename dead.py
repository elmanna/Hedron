import psutil
import sys
from time import sleep
import os
import requests

hedron_pid = None

def _sendMsg_(msg):
    #here you can do what ever action you want in my case 
    #i want to send a notification msg to a telegram group
    pass
    """url = f"https://api.telegram.org/bot<yourTelegramBotToken>/sendMessage?chat_id=<chatIDyouwantToSendTheMsgInto>&text=%s" %msg
    requests.get(url)"""



def _check_pidName(pid):
    try:
        process = psutil.Process(pid)
        hedron = process.name()
        if checkIfProcessRunning(hedron):
            pass
          #  print('Yes a hedron process was running')
           # sleep(2)
    except Exception as e:
        #>>>>>>>>>>>>>>Here you can execute your when  
        #>>>>>>>>>>>>>>the hedron main process dies
        print('No hedron process was running notify group & self-destruction')
        sleep(2)
        _sendMsg_(">>>>>>>Hedron was shutted-down")
        exit()

        
    

#this function was brought from stackoverflow thread
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;



def main(pid):
    global hedron_pid
    hedron_pid = int(pid[0])
    print(hedron_pid)
    while True:
        sleep(5)
        _check_pidName(hedron_pid)
        
            


if  __name__ == "__main__":
    main(sys.argv[1:])