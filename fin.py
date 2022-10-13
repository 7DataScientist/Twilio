from config import account_sid, auth_token
from tai1 import send_whatsapp_text, set_twilio_connection
from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

cli1 = set_twilio_connection(account_sid,auth_token)


job = scheduler.add_job(send_whatsapp_text, 'cron',[cli1],hour='11',minute='08')
print(job)

while True:
    time.sleep(1)

# pip install apscheduler