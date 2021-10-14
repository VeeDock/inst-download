import instaloader, configparser, time

from instaloader.lateststamps import LatestStamps

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

#скачивание последнего поста
while True:
    for old_last_post in posts:
        break
    posts = profile.get_posts()
    for last_post in posts:
        break
    if last_post != old_last_post:
        ig.download_post(post = last_post, target = config['Download']['folder'])
    time.sleep(3000)