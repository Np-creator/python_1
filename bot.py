from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = #personal 

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    
    name = user.first_name
    user_id = user.id
    text = update.message.text
    
    print(f"📩 ID:{user_id} | {name}: {text}")
    await update.message.reply_text(f"Your ID is: {user_id}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot is running...")
app.run_polling()