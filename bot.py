from telegram import Bot, InputMediaDocument, InputMediaPhoto
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Using environment variables
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

# File paths
ipa_path = "file.ipa"  # Change to your IPA file path
icon_path = "icon.png"  # Change to your icon file path

# Send icon first
bot.send_photo(chat_id=CHAT_ID, photo=open(icon_path, "rb"))

# Send IPA file with caption
bot.send_document(
    chat_id=CHAT_ID,
    document=open(ipa_path, "rb"),
    caption="**Name:** Your App Name\n**Tweak:** Subscription Unlocked\n**Version:** 1.0.0\n**Made by:** YourName",
    parse_mode="Markdown"
)

print("File uploaded successfully!")
