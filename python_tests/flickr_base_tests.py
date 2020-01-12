import flickrapi
import random
import requests
from PIL import Image
from IPython import display
import os
from flikr_api_keys import api_key,api_secret

flickr = flickrapi.FlickrAPI(api_key, api_secret)
try:
    os.mkdir('flickr_photo')
except OSError:
    pass 

photos = flickr.photos.search(
    page=random.randint(0, 100),
    tags='red',
    width=1920,
    orientation='landscape',
    content_type=1,
    sort='relevance',
    license='9,10',
    format='parsed-json')
print(photos)

for i,photo in enumerate(photos['photos']['photo']):
    print(i)
    finded_photo = flickr.photos.getSizes(photo_id=photo['id'], format='parsed-json')['sizes']['size'][0]
    if finded_photo['label'] == "Square":
        print(finded_photo['source'])
        img = requests.get(finded_photo['source'])
        img_file = open(f'flickr_photo/{i}.jpg', 'wb')
        img_file.write(img.content)
        img_file.close() 
print("ok")

for i in range(100):
    image = Image.open(f'flickr_photo/{i}.jpg')

    w, h = image.size
    rr, gg, bb = 0, 0, 0

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            rr += r
            gg += g
            bb += b

    cnt = w * h
    print(rr//cnt, gg//cnt, bb//cnt)
    awg_color=Image.new('RGB', (150,75), color=(rr//cnt, gg//cnt, bb//cnt))
    awg_color.paste(image,(0,0,75,75))
    awg_color.save(f'flickr_photo/awg_{i}.jpg', "JPEG")
    image = display.Image(f'flickr_photo/{i}.jpg')
    awg_color= display.Image(f'flickr_photo/awg_{i}.jpg')
    display.display_jpeg(awg_color)