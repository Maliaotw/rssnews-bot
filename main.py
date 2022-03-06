import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import Flask

from app import bot
from app import refresh, push, cache

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('apscheduler').setLevel(logging.INFO)

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(bot, id='bot')
scheduler.add_job(cache, CronTrigger.from_crontab('*/15 * * * *'), id='cache')
scheduler.add_job(refresh, CronTrigger.from_crontab('*/15 * * * *'), id='refresh')
scheduler.add_job(push, CronTrigger.from_crontab('*/15 * * * *'), id='push')
scheduler.start()


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
