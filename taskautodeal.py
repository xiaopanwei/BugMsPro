from apscheduler.schedulers.blocking import BlockingScheduler

from dbutil.mybug_util import getUnResultEmail
from remind import email_send

def init_setting():
    scheduler = BlockingScheduler()
    scheduler.add_job(email_job, "interval", seconds=10800)
    scheduler.start()
