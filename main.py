import instaloader, configparser, time, os, shutil

from instaloader.lateststamps import LatestStamps
from instaloader.structures import Post

#читает конфиг
config = configparser.ConfigParser()
config.read('config.ini')

#instaloader
ig = instaloader.Instaloader()

#пользователь
username = config['User']['username']
profile = instaloader.Profile.from_username(context = ig.context, username = username)
posts = profile.get_posts()

#настраивание скачивания
folder = config['Download']['folder']
cache_folder = config['Download']['cache_folder']

#скачивание последнего поста
old_last_post = Post
last_post = Post
while True:
    for old_last_post in posts:
        break
    posts = profile.get_posts()
    for last_post in posts:
        break  
    last_post.caption_hashtags
    if True:#last_post != old_last_post:
        ig.download_post(post = last_post, target = cache_folder)
        for file in os.listdir(cache_folder):
            if file.endswith(".json.xz"):
                filename = file.split('.')[0]
                break
            elif file.startswith(filename) and file.endswith('.jpg'):
                newfilename = str(last_post.date.year.zfill(4)) + str(last_post.date.month.zfill(2)) + str(last_post.date.day.zfill(2)) + str(last_post.date.hour.zfill(2)) + str(last_post.date.minute.zfill(2)) + str(last_post.date.second.zfill(2)) + '['
                for tag in last_post.caption_hashtags:
                    newfilename += tag + ','
                newfilename = newfilename[:1] + ']'
                try:
                    shutil.move(file, folder + '\\' + newfilename + '.jpg')
                except:


        #print(filename)
    time.sleep(3000)