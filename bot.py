import os
import telebot

# Replace with your bot token and chat ID
BOT_TOKEN = "YOUR_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

# Define the path for the icon
icon_path = "/telegram-bot-uploader/icon.png"  # Update the path if needed

# Function to send icon
def send_icon():
    if os.path.exists(icon_path):
        with open(icon_path, "rb") as photo:
            bot.send_photo(chat_id=CHAT_ID, photo=photo)
    else:
        bot.send_message(chat_id=CHAT_ID, text="⚠️ Icon not found. Please upload 'icon.png'.")

# Start command
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "🤖 Bot is online!")
    send_icon()

# Run the bot
bot.polling()
