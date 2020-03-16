from telegram.ext import Updater,CommandHandler
def welcome(update, context):
    message = 'Olá, ' + update.message.from_user.username + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
def main():
    token = '981518741:AAGWaG1nx07DfnvsJSSsTO-a35e1QPXp6ac'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print(str(updater))
    updater.idle()

if __name__ == "__main__":
    main()