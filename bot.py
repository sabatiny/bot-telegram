import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = 'Olá, ' + update.message.from_user.username + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '981518741:AAGWaG1nx07DfnvsJSSsTO-a35e1QPXp6ac'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('feedback', feedback)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    print("Updater no ar1: " + str(updater))
    updater.start_polling()
    updater.idle()

def feedback(update, context):
    try:
        message = 'Por favor, digite um feedback para o nosso tutorial:'
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))
        
def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = """Seu feedback foi muito curtinho... 
                        \nInforma mais pra gente, por favor?"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigada pelo seu feedback!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def inputFeedback2(update, context):
    feedback = update.message.text
    message = "Muito obrigada pelo seu feedback!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

if __name__ == "__main__":
    main()