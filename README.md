# SanTelegram Bot

## installation

```
pip install python-telegram-bot
pip install telethon
pip install configparser logging
git clone https://github.com/RduMarais/santelegram.git
```

## usage : 

> I did a *huge* tutorial for beginners (in French) on my personal blog and here : https://github.com/RduMarais/santelegram/blob/master/Tutoriel.md

 * Change the **config_example.ini** file name to **config.ini**
 * Write in it the Advent Calendar you want, with the usernames you want to be able to open.
 * get the usernames with telethon_get_users.py
 * put your API token in the config.ini
 * run 


```bash
python santabot.py
```
Stop it with Ctrl+C

Enjoy


# documentation : 

 * API python : https://python-telegram-bot.readthedocs.io/en/stable/telegram.chat.html#telegram.Chat
 * get chat ID : https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android
 	 * mieux https://www.wikihow.com/Know-a-Chat-ID-on-Telegram-on-PC-or-Mac
