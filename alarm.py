import time 
from datetime import datetime 
from plyer import notification 
import winsound 


def set_alarm(hour, minute):
    now = datetime.now()
    alarm_time = datetime(now.year, now.month, now.day, hour, minute)

    time_difference = alarm_time - now 

    time.sleep(time_difference.total_seconds())

    notification.notify(
        title="Alarm",
        message="Wake Up! It's Time!",
        app_icon=None,
        timeout=20
    )


    winsound.Beep(1000, 1000)



set_alarm(9, 28)









