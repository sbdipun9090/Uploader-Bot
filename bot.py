


import os
from Uploader.config import Config
from pyrogram import Client as Tellyhub

if __name__ == "__main__" :
    
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="Uploader")
    Tellybots = Tellyhub("@TellyUploaderProBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Tellybots.run()
