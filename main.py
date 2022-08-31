"""
This is the main loop file for our AutoTube Bot!

Quick notes!
- Currently it's set to try and post a video then sleep for a day.
- You can change the size of the video currently it's set to post shorts.
    * Do this by adding a parameter of scale to the image_save function.
    * scale=(width,height)
"""

from datetime import date
import time
import random
from utils.CreateMovie import CreateMovie, GetDaySuffix
from utils.RedditBot import RedditBot
#from utils.upload_video import upload_video
import upload_file

#Create Reddit Data Bot
redditbot = RedditBot()

# Leave if you want to run it 24/7
while True:

    # Gets our new posts pass if image related subs. Default is memes
    posts = redditbot.get_posts("memes")

    # Create folder if it doesn't exist
    redditbot.create_data_folder()

    # Go through posts and find 5 that will work for us.
    for post in posts:
        redditbot.save_image(post)

    # Wanted a date in my titles so added this helper
    # DAY = date.today().strftime("%d")
    # DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
    # dt_string = date.today().strftime("%A %B") + f" {DAY}"

    # Create the movie itself!
    #CreateMovie.CreateMP4(redditbot.post_data)

    # Video info for YouTube.
    # This example uses the first post title.
    # video_data = {
    #         "file": "video.mp4",
    #         "title": "Here is the meme of the day. Have fun and enjoy your time",
    #         "description": "#shorts\n Have fun and live a happy life",
    #         "keywords":"meme,daily memes,Dankestmemes,reddit memes,funny memes",
    #         "privacyStatus":"public"
    # }

    
    print("Posting picture in 10 Seconds ...")
    time.sleep(10)
    #upload_video(video_data)
    #exit()
    # Sleep until ready to post another video!
    sleep_num = random.randint(0,9)
    upload_file.upload_picture()
    print("Next will post in "+int(sleep_num)+" minutes.")
    time.sleep(60*sleep_num - 1)
