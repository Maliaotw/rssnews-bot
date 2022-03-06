"""
Command-line tool using fire
"""
import logging

from flask import Flask

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

from app import bot
from app import refresh, push
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

logger = logging.getLogger(__name__)

refresh()
scheduler = BackgroundScheduler()
scheduler.add_job(bot, id='bot')
scheduler.add_job(refresh, CronTrigger.from_crontab('*/15 * * * *'), id='refresh')
scheduler.add_job(push, CronTrigger.from_crontab('*/15 * * * *'), id='push')
scheduler.start()


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()
