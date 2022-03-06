import telegram
# from telegram.ext.updater import Updater
from telegram.ext import (Updater, Filters, CommandHandler, MessageHandler, ConversationHandler, RegexHandler)
import logging
from conf import settings
from utils import request
# import pprint
# import os


logger = logging.getLogger(__name__)


def start(update: telegram.update.Update, context):
    logger.info(update.message.from_user)

    tests = [
        "/help - 顯示所有指令",
        "/hello - 我是誰",
        "/binduser <token> - 綁定帳戶",
        "/favor - 收藏清單",
    ]

    update.message.reply_text("\n".join(tests))


# 查看用戶資訊
def hello(update, context):
    ret = []

    if update.message['chat']['type'] == 'group' or update.message['chat']['type'] == 'supergroup':
        ret.append("群組ID: %s" % update.message['chat']['id'])

    ret.append("個人ID: %s" % update.message.from_user.id)

    context.bot.send_message(chat_id=update.message.chat.id, text="\n".join(ret))


# 綁定帳戶
def binduser(update: telegram.update.Update, content):
    logger.info(update.message.from_user)

    if content.args:
        ret = request.post("telegram-registrations",json={"tgid": str(update.message.from_user.id), "token": "".join(content.args)})
        update.message.reply_text(ret['message'])
    else:
        update.message.reply_text("未輸入Token")



def echo(update: telegram.update.Update, content):
    logger.info(update.message.from_user)


def foo(update: telegram.update.Update, content):
    update.message.forward('183009981')


def bot():
    # MarioNews_bot
    request.appRegistration('bot')
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', start))
    updater.dispatcher.add_handler(CommandHandler('echo', echo))
    updater.dispatcher.add_handler(CommandHandler('binduser', binduser))
    # updater.dispatcher.add_handler(MessageHandler(Filters.all, foo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    bot()
