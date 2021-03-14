from apscheduler.schedulers.blocking import BlockingScheduler

from remind import email_send


def email_job():


    email_send.sendemail("我<949888408@qq.com>","bugid:1 内容：bug 已经超过一个小时没有处理了")


def init_setting():
    scheduler = BlockingScheduler()
    scheduler.add_job(email_job, "interval", seconds=360000)
    scheduler.start()
