import numpy as np 
import requests
import twitter_bot_utils as tbu
import os 


def tweet_image(url, message):
    filename = '/tmp/temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        twitter.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

if __name__ == '__main__':
    r = requests.get('https://oss.weathershare.org/data/CCTV/OSS_cctv.json')
    data = r.json()[0]
    data = [d for d in data if 'url' in d]
    data = [d for d in data if d['url'] != []]
    random_camera = np.random.choice(data)
    tweet_image(random_camera['url'][0], random_camera['location'])

    # Automatically check for a config file in the above-named directories
    twitter = tbu.API(screen_name='botUGS')