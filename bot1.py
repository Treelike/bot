from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters,RegexHandler
from telegram.error import NetworkError,Unauthorized

import telegram
def start(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hi, I'm a bot under construction I have nothing to start.\n")

def ukt(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Pardon me!!! I dont know what you are trying to say. Try greeting hello")

def ukc(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Seems like I don't know this command Sorry ,my Master is still busy Programming me hopefully one day I'll be a fully functional bot ")

def greeting(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="hello , who are you? tell me your full name and i'll tell you my secret !!!")

def greeting1(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="I've heard you ask my master to create you a new bot \nAnswer: Yes or No")

def yesf(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="he's working on it but he's still busy with his college works so he'll finish it as soon as he can :) type No now ")
def nof(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="""okhay , here's how I was made my source code:   
    \n1 from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters,RegexHandler\n
  2 from telegram.error import NetworkError,Unauthorized\n
  3 
  4 import telegram\n
  5 def start(bot,update):\n
  6     chat_id = update.message.chat_id\n
  7     bot.send_message(chat_id=chat_id, text="Hi, I'm a bot under construction I have nothing to start.\n")\n
  8 \n
  9 def ukt(bot,update):\n
 10     chat_id = update.message.chat_id\n
 11     bot.send_message(chat_id=chat_id, text="Pardon me!!! I dont know what you are trying to say.")\n
 12 \n
 13 def ukc(bot,update):\n
 14     chat_id = update.message.chat_id]\n
 15     bot.send_message(chat_id=chat_id, text="Seems like I don't know this command Sorry ,my Master is still busy Programming me hopefully one day I'll be     a fully functional bot ")\n
 16\n 
 17 def greeting(bot,update):\n
 18     chat_id = update.message.chat_id\n
 19     bot.send_message(chat_id=chat_id,text="hello , who are you? tell me your full name and i'll tell you my secret !!!")\n
 20 \n
 21 def greeting1(bot,update):\n
 22     chat_id = update.message.chat_id]\n
 23     bot.send_message(chat_id=chat_id,text="I've heard you ask my master to create you a new bot")\n
 24 \n
 25 def yes(bot,update):\n
 26     chat_id = update.message.chat_id\n
 27     bot.send_message(chat_id=chat_id,text="he is still working on it but he's still busy with his college works he'll finish it as soon as he can")\n
 28 def no(bot,update):\n
 29     chat_id = update.message.chat_id\n
 30     bot.send_message(chat_id=chat_id,text="okhay , here's how I was made my source code: ")\n
 35 \n
 36 def main():\n
 37     ukhandler=RegexHandler(r'/.*',ukc);\n
 38     updater = Updater('716174638:AAE86IhcZOK7IdnGISzD8R51CPtsQ_LyhSk')\n
 39     dp = updater.dispatcher\n
 40     dp.add_handler(CommandHandler('start',start))\n
 41     dp.add_handler(ukhandler)\n
 42     yes=RegexHandler('yes',yes);]\n
 43     no=RegexHandler('no',no);\n
 44     greets1=RegexHandler('^s|^S.....$n',greeting1);\n
 45     greets=RegexHandler('^h|^h...$o',greeting);\n
 46     dp.add_handler(yes)\n
 47     dp.add_handler(no)\n
 48     dp.add_handler(greets1)\n
 49     dp.add_handler(greets)\n
 50     dp.add_handler(MessageHandler(Filters.text,ukt))\n
 51     updater.start_polling()\n
 52     updater.idle()\n
 53 \n
 54 if __name__ == '__main__':\n
 55     main()\n
~                     """)





def main():
    ukhandler=RegexHandler(r'/.*',ukc);
    updater = Updater('716174638:AAE86IhcZOK7IdnGISzD8R51CPtsQ_LyhSk')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(ukhandler)
    yes=RegexHandler('^y|^Yes',yesf);
    no=RegexHandler('^n|^No',nof);
    greets1=RegexHandler('^s|^S.....$n',greeting1);
    greets=RegexHandler('^h|^h...$o',greeting);
    dp.add_handler(yes)
    dp.add_handler(no)
    dp.add_handler(greets1)
    dp.add_handler(greets)
    dp.add_handler(MessageHandler(Filters.text,ukt))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
