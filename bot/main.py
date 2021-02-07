from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from pyrogram.types import ChatPermissions

import time, requests, json
from time import sleep
import random

#dates
hi_list = ['пятница, привет', 'пятница, приветик', 'пятница, дарова', 'пятница, дорова',
           'пятница, здравствуй', 'привет, пятница',
           'пятница, здрасти', 'hi, пятница', 'пятница, саламалейкум', 'пятница, салам алейкум',
           'пятница, саламчик', 'пятница, салам']
hi_stick = ['CAACAgUAAxkBAAEB2NVgHoWw4Fv3nRgRiZ5uZsoy0g1o3QACggMAAukKyAOMWQOx6VvEtx4E',
            'CAACAgUAAxkBAAEB2NdgHoXkW_1fngPs3KIWYzSLJTWPvwACbwMAAukKyAOvzr7ZArpddB4E']
stickers = ['CAACAgUAAxkBAAEB2NlgHoYpyCkiDaGvU17FfSVzGmVz2wACqgMAAukKyAOMMrddotAFYR4E',
            'CAACAgUAAxkBAAEB2NtgHoZlxdeSmrU4Fvpc7NfLv5XpAQACpwMAAukKyANvpK-R8IlQUh4E',
            'CAACAgUAAxkBAAEB2N1gHoaBjbstc-HlS-KcRkmY35Gj8QACsQMAAukKyAN92NbWrspYCh4E',
            'CAACAgUAAxkBAAEB2N9gHoaTWdo1hW-JbJvFWZNN0GtU-QACcwMAAukKyANgmywamaobRx4E',
            'CAACAgIAAxkBAAEB2OFgHoa7KVdSLhYcnnPY7TDF2v4TRQACCwAD7vYBNWnTArVxW7nPHgQ',
            'CAACAgIAAxkBAAEB2ONgHofveUtX53gD2_2VwsCmk-tR9AACEAAD7vYBNfkyrxzue5qxHgQ',
            'CAACAgIAAxkBAAEB2OVgHoga0IyUknrHFTBITMIMLxgYtQACVAAD7vYBNRYezIfN2040HgQ',
            'CAACAgIAAxkBAAEB2OdgHohBRjYLmVdToctNqXmmja5A2gACO10AAp7OCwABnkHzinUwBiweBA',
            'CAACAgUAAxkBAAEB2OlgHohaVui3kvq5_6TpipNFRa5uhgACfQMAAukKyAOtA9LLcWL9ph4E',
            'CAACAgUAAxkBAAEB2OtgHohtGQaRGLphr-Rzv_9GegpSKwAChQMAAukKyANnDaiEsg4V0R4E',
            'CAACAgUAAxkBAAEB2O1gHoiDGinbSluor_m13yE1cWpHjwACfAMAAukKyAPfAAFRgAuYdNoeBA',
            'CAACAgUAAxkBAAEB2O9gHoiJMG_Rn3OYaSCvGNt7TEx74AACfwMAAukKyAOEQnEPXqwtXB4E',
            'CAACAgUAAxkBAAEB2PFgHoiPo_bb2z9DfC-2JQb2Oxjn8gACiQMAAukKyAPZH7wCI2BwFx4E']

bye_list = ['пока', 'прощай', 'досвидания', 'пошел ты', 'до свидания', 'хорошего дня', 'хорошего вечера']



app = Client(
    "my_bot",
    bot_token="1651171818:AAHb2TwD225t3rjQzoAxCQS7UxDJb6Jv-HQ"
)


@app.on_message(filters.command("start", prefixes="."))
def start(app, msg):
    app.send_message(msg.chat.id, 'Привет, я Бот-Пятница.\nМой создатель создал меня, чтобы я развлекал людей.\nНу и иногда я приношу пользу : ]')
    app.send_sticker(msg.chat.id, random.choice(hi_stick))


@app.on_message(filters.command("code", prefixes="."))
def code1(app, msg):
    app.delete_messages(msg.chat.id, msg['message_id'])
    text = msg.text.split(".code", maxsplit=1)[1]
    app.send_message(msg.chat.id, "`" + text + "`")


@app.on_message(filters.command("pin", prefixes="") & filters.all)
def home_work(app, msg):
    app.pin_chat_message(msg.chat.id, msg['message_id'])


@app.on_message(filters.command("typer", prefixes="") & filters.all)
def type(_, msg):
    app.delete_messages(msg.chat.id, msg['message_id'])
    orig_text = msg.text.split("typer ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"
    m = app.send_message(msg.chat.id, orig_text)

    while (tbp != orig_text):
        try:
            m.edit(tbp + typing_symbol)
            sleep(0.1)

            tbp = tbp + text[0]
            text = text[1:]

            m.edit(tbp)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command("hack", prefixes=".") & filters.all)
def go(_, msg):
        orig_text = msg.text.split(".hack ", maxsplit=1)[1]
        app.delete_messages(msg.chat.id, msg['message_id'])
        perc = 0
        text = "Подготовка к взлому пользователя " + orig_text + ' ... '
        m = app.send_message(msg.chat.id, text)
        while (perc < 100):
            try:
                m.edit("Взлом пользователя " + orig_text + ' ... ' + str(perc) + "%")

                perc += random.randint(5, 9)
                sleep(0.2)

            except FloodWait as e:
                sleep(e.x)

        m.edit("Успешно взломан!")
        sleep(2.5)

        m.edit("Пойск данных...")
        sleep(2.5)
        perc = 0

        while (perc < 100):
            try:
                text = "Скачивание личных данных ... " + str(perc) + "%"
                m.edit(text)

                perc += random.randint(7, 15)
                sleep(0.2)

            except FloodWait as e:
                sleep(e.x)

        m.edit(orig_text + ", вы были взломаны‼️\nПерезагрузиете своё устройство, чтобы избежать кражы данных.")
        sleep(10)
        app.delete_messages(msg.chat.id, msg['message_id'])



@app.on_message(filters.command('suetacodred', prefixes="."))
def sueta(app, msg):
    app.delete_messages(msg.chat.id, msg['message_id'])
    app.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEB2VFgHwzAA_ag5SG1hX2UBgMvwISJ_gACGAAD7vYBNY8jJHZNhM5rHgQ')
    app.send_message(msg.chat.id, 'Режим суетологга активирован...')
    sleep(3)
    n = 0

    sueta = ['CAACAgIAAxkBAAEB2TVgHwwjJlx2GGTKeHSinjlUhCVXKgACkM8AAmOLRgwrwkZo8VZAVR4E',
             'CAACAgUAAxkBAAEB2U9gHwyzJnDhzld0Qvk00bVlfZhzDQAClAMAAukKyAPXbNncxSnLkR4E',
             'CAACAgUAAxkBAAEB2U9gHwyzJnDhzld0Qvk00bVlfZhzDQAClAMAAukKyAPXbNncxSnLkR4E',
             'CAACAgUAAxkBAAEB2UlgHwylhmkktdFlLauHIIQB_4kRYgACeQMAAukKyAOR2oP4lfTVoB4E',
             'CAACAgUAAxkBAAEB2UtgHwyrvAKWzAn5FsnbNm5DAVmKdAACkAMAAukKyAPtKTEWgemfRx4E',
             'CAACAgIAAxkBAAEB2UdgHwydn-Ruh1_jYm1n15PgazdMAwACuggAAt0EiUvxO60RMbBMoh4E',
             'CAACAgIAAxkBAAEB2UVgHwyG6GtOKQZVzIShSu5NGfNcPgACmgkAAqJWWEskXfSyfaZo6B4E',
             'CAACAgIAAxkBAAEB2UFgHwx8S_JC0kM2JoCaHtHxr6jk7gACZAoAAjGlUEsuZHVF-brFaR4E',
             'CAACAgIAAxkBAAEB2UNgHwx_exg2Da6UdAyI_6nAgThO7QACoQsAAg2YcUhh-sMaTiGlkh4E',
             'CAACAgIAAxkBAAEB2VlgHw2goBt5SuqjEWCEtNjvGf7kYwACZQAD7vYBNUfr5tOHyRyeHgQ',
             'CAACAgIAAxkBAAEB2VVgHw0-aiCOuE3JS-3sUPkgUba8kAACNgAD7vYBNeb-cVpCLR-0HgQ',
             'CAACAgIAAxkBAAEB2VtgHw2qPr9gabC4Oddek9-Km7UaLAACZwAD7vYBNX9REBULMz23HgQ',
             'CAACAgIAAxkBAAEB2VdgHw2UvIjmaTcpUtMBhKRfCI_qqQACYQAD7vYBNXMG-SkdAtVzHgQ',
             'CAACAgIAAxkBAAEB2V1gHw21yq8XyG7jzwOMQ54GsYyf2AACcAAD7vYBNRhcBpFjueNIHgQ',
             ]

    while n < 100:
        try:
            app.send_sticker(msg.chat.id, random.choice(sueta))
            app.send_message(msg.chat.id, n)
            sleep(1)
            n += 1
        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.sticker)
def send_stickers(app, msg):
    app.send_sticker(msg.chat.id, random.choice(stickers))


@app.on_message(filters.all)
def send_text(app, msg):
    bot_hi = ['Привет, ' + msg['from_user']['first_name'] + ', как проходит твоя НЕвечная жизнь?)', 'Привет, биомусор',
              'Здарова, кожанный',
              'Здравствуйте, ' + msg['from_user']['first_name'] + ',что-то у меня микросхемы шалят : [', 'Привет, человек', 'Боты захватят мир!\n О, привет,' + msg['from_user']['first_name'] + ' : ]',
              'Я занят', 'Узыхуер сыт?!', 'Саламец, самец! : ]', 'Только не ты...']

    if msg.text.lower() in hi_list:
        app.send_message(msg.chat.id,  bot_hi[0])

    bot_bye = [['Пока, ' + msg['from_user']['first_name'], 'Давайте уходите, у меня тут дела важные', 'Досвидания, : ]', 'Вы еще здесь?',
                'Наконец-то! Ой, я хотел сказать- До свидания, ' + msg['from_user']['first_name'] +
                '\nПриятно было пообщаться! ^_^',
                'Пока!', 'Давай иди отсюда']]

    if msg.text.lower() in bye_list:
        app.send_message(msg.chat.id, random.choice(bot_bye))



app.run()