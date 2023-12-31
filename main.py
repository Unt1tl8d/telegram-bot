import ptbot
from pytimeparse import parse
import os
from dotenv import load_dotenv, find_dotenv
import time


def timer(chat_id, question, bot):
    delay = parse(question)
    message_id = bot.send_message(chat_id, "Таймер запущен!!!")
    bot.create_countdown(delay, counting, chat_id=chat_id, message_id=message_id, delay=delay, bot=bot)
    time.sleep(delay+0.5)
    bot.send_message(chat_id, 'Время вышло!!!')


def counting(second_left, chat_id, message_id, delay, bot):
    bot.update_message(chat_id, message_id, "Осталось секунд: {}\n ".format(second_left) + render_progressbar(delay, delay - second_left))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(iteration, total)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    load_dotenv(find_dotenv())
    bot = ptbot.Bot(os.getenv('TG_TOKEN'))
    bot.reply_on_message(timer, bot=bot)
    bot.run_bot()


if __name__ == '__main__':
    main()
