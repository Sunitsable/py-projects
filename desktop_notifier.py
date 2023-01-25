import time
from plyer import notification

if __name__=="__main__":
    while(True):
        notification.notify(
            title="Hello, I think you should take a break",
            message="please take a break of 10 mins",
            
            timeout=1000
            

        )
        time.sleep(1000)
        break
    