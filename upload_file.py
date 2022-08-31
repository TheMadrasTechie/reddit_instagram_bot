from instabot import Bot
# import os 
# import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])
bot = Bot()
bot.login(username = "your_username",
          password = "password")
def upload_picture():
    bot.upload_photo("image.jpeg",
                 caption ="Sourced from Reddit Memes.. !!! Do follow for more such memes !!!                                   -@drakemeemer                           -@drakemeemer                                            -@drakemeemer                                  #funny #funnymemes #dankmemes #memer #funnyphotos #laugh #lol #smile #fun #funnyvideos #trending #redditmemes #drakememes #drakememer")