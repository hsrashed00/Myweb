from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

CHANNEL = "@Hs_ShadowX"  # এখানে তোমার চ্যানেলের username দাও

def start(update, context):
    user = update.effective_user
    try:
        member = context.bot.get_chat_member(CHANNEL, user.id)
        if member.status in ["left", "kicked"]:
            keyboard = [[InlineKeyboardButton("🔥 Subscribe And Verify ⚡", url=f"https://t.me/{CHANNEL[1:]}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text("👉 আগে চ্যানেলে Join করো, তারপর আবার /start দাও", reply_markup=reply_markup)
        else:
            update.message.reply_text("✅ ধন্যবাদ! তুমি ভেরিফাই হয়ে গেছো।")
    except Exception as e:
        update.message.reply_text("❌ Error: বটকে আগে তোমার চ্যানেলে admin করে দাও।")

updater = Updater("7623246491:AAFMYq6RfjBZdCN-a6ZWn8248HA5weAqDlw")
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()