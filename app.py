import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
import string
import random
from users import *
def end_gen(length):
    letters = string.ascii_lowercase+string.digits+string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def start(update,context):
    keyboard = [
                [InlineKeyboardButton("Sign Up", url="https://tgshortener.com/auth/signup")],
                
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = '''😋This bot will help you to Short Links from your TGshortener Account.

If you don't have an active TGshortener.com Account then Please register your account here tgshortener.com/auth/signup
 
2️⃣How to Short Links? 
👉 After Logging in , Send any link which you want to Short. 
👉 You will get your Shortned Link immediately.

3️⃣How to Short Bulk links at a time? 
👉Send All the links which you want to short in below format 👇
https://youtube.co
https://google.com
https://tgshortener.com
👉 Boom 💥 ! You will get all link shorten.

⚡️Still Have Doubts?
⚡️Want to Report Any Bug?
😌Send Here @TGshortener_support'''
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)

def API_Login(update, context):
    user_rsp=update.message.text.split(" ")
    user = update.message.from_user
    username = user.username
    if len(user_rsp)==1:
        update.message.reply_text("Please send token in format /token 12590xxxxxxxx")
    elif len(user_rsp)==2:
        ser_rsp=login(username, user_rsp[1])
        if ser_rsp == True:
            update.message.reply_text(f"Welcome {username}, Now You Can Short Your Links")
        elif ser_rsp == False:
            update.message.reply_text("You are already logged in.")
        else:
            update.message.reply_text("Something Went Wrong")
    else:
        update.message.reply_text("Please send token in format /token 12590xxxxxxxx")

def help(update,context):
    keyboard = [
                [InlineKeyboardButton("Get Help", url="https://tgshortener.com/member/forms/support")],
                
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = 'Click on button to get help'
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)

def feature(update, context):
    update.message.reply_text("""💠 Features Of TGshortener bot 💠

❤️ It's AN AI Based User Friendly Bot ❤️

➡️ Use Can Short Bulk Links Into Your TGshortener Account With This Bot""")

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message
    r_message=message.text
    user = update.message.from_user
    username = user.username
    if message.photo:
        # Get the latest photo and its caption
        photo_file_id = message.photo[-1].file_id
        caption = message.caption
        links = re.findall(r'(https?://\S+)', caption)
        filtered_list = [link for link in links if "t.me" not in link]
        short_link=[]
        L=0
        for link in filtered_list:
            short_link.append(link_gen(username, link))
            caption = caption.replace(link, f"{short_link[L]}")
            L=L+1
        context.bot.send_photo(chat_id=message.chat_id, photo=photo_file_id, caption=caption)
    elif message.text:
        if "https//" in message.text or "http" in message.text:
            caption = message.text
            links = re.findall(r'(https?://\S+)', caption)
            filtered_list = [link for link in links if "t.me" not in link]
            short_link=[]
            L=0
            for link in filtered_list:
                short_link.append(link_gen(username, link))
                caption = caption.replace(link, f"{short_link[L]} ")
                L=L+1
            update.message.reply_text(caption)
        else:
            update.message.reply_text("Please Send me any link or Forward Whole Post")
    else:
        update.message.reply_text("Please Send me any link or Forward Whole Post")

def get_api(update,context):
    keyboard = [
                [InlineKeyboardButton("Get Token", url="TGshortener.com/member/tools/api")],
                
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = """• First Visit TGshortener.com/member/tools/api
• Copy the API TOKEN and come back to Bot.
• Input  /token and Paste The token Copied from TGshortener.com/member/tools/api
• Now bot will successfully connected to your  vnshortener account."""
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)

def API_Logout(update, context):
    user = update.message.from_user
    username = user.username
    resp=logout(username)
    if resp == True:
        update.message.reply_text("You are Logged Out SuccessFully")
    elif resp == False:
        update.message.reply_text("Please Login First")
    else:
        update.message.reply_text("Something Went Wrong")
# Set up the bot and its message handler
def main():
    bot = telegram.Bot("5875483341:AAG-cMVgEqYN3NkPnClUb5mRRJ9s-LKFs2o")
    updater = telegram.ext.Updater(bot.token, use_context=True)
    disp = updater.dispatcher
    disp.add_handler(telegram.ext.CommandHandler('start',start))
    disp.add_handler(telegram.ext.CommandHandler('help',help))
    disp.add_handler(telegram.ext.CommandHandler('token',API_Login))
    disp.add_handler(telegram.ext.CommandHandler('get_api',get_api))
    disp.add_handler(telegram.ext.CommandHandler('logout',API_Logout))
    disp.add_handler(telegram.ext.CommandHandler('features',feature))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.all, handle_message))
    updater.start_polling()

if __name__ == "__main__":
    main()
