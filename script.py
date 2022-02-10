from urllib import request
import requests
from bs4 import BeautifulSoup
import os

def imageDownload(url):

    #removing the unnecessary texts from the site name which will later be used to create a folder for this part download instance
    folder = url.replace('https://www.', '').replace('.com', '_')
    try:
        #creattion of the download directory || inside the project folder
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    #changing the current working directory 
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        if image.has_attr('data-src'):
            link = image['data-src']

            #to replace a directory name in the path of the image. Not applicable any other site but might be useful when the webpage displays low res versions of images
            link = link.replace('/460/', '/1280/')
            name = image['alt']
            with open(name + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('Writing:', name)


imageDownload('Your url here')