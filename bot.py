from telegram import Update  # this means every message that 
                             # user sends 

 #### a very simple Telegram bot to get your name and say hi ###

from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# you literally get the Libraries inside the telegram to be able to build 
# your bot 

BOT_TOKEN = #personal "You have to insert your own TOKEN here"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): 

    user = update.message.from_user 
    
    name = user.first_name

    user_id = user.id

    text = update.message.text
    
    print(f"📩 ID:{user_id} | {name}: {text}")

    await update.message.reply_text(f"Your ID is: {user_id}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Your BOT runs now! . . .")

app.run_polling()