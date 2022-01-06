# nus graduation photos scrap
import math
import csv
import requests
import shutil


def getimage(url, filename):
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ', filename)
            return True
        else:
            return False
    except:
        pass


# ceremony num and position num may not zfill
def c(nusnetid):
    '''baseurl = https://www.werkzgallery.com/nus//ind_images/'''
    '''endpoint = A*******X/Z_C**-**.jpg'''

    # all ceremonies
    for num in range(1, 100):
        num = str(num).zfill(2)
        for ceremony in range(1, 90):  # there are only 89 ceremonies
            ceremony = 'C' + str(ceremony).zfill(2)
            endpoint = f"Z_{ceremony}-{num}.jpg"
            filename = endpoint
            url = f"https://www.werkzgallery.com/nus//ind_images/{nusnetid}/{endpoint}"
            if getimage(url, filename):
                break


# ceremony 29 burteforce
# for num in range(1,100):
##        num = str(num).zfill(2)
##        ceremony = 'C29'
##        endpoint = f"Z_{ceremony}-{num}.jpg"
##        filename = endpoint
##        url = f"http://www.werkzgallery.com/nus//ind_images/{nusnetid}/{endpoint}"
##        e = f"{nusnetid}/{endpoint}"
# with open('store.txt','a',encoding='utf-8') as g:
# g.write(e)
# g.write('\n')


def teo(nusnetid):
    '''baseurl = https://www.werkzgallery.com/nus//ind_images/'''
    '''endpoint = A*******X/***_TEO_****.jpg'''
##    two = 77
##    four = 7287

    for i in range(1, 251):  # guess that each ceremony only got 250 students
        diff = abs(77 - 1)
        num = 7287 - diff
        num = str(num)
        i = str(i).zfill(3)

        endpoint = f"{i}_TEO_{num}.jpg"
        url = f"https://www.werkzgallery.com/nus//ind_images/{nusnetid}/{endpoint}"
        print(url)
        filename = endpoint
        if getimage(url, filename):
            break


def dsc(nusnetid):
    '''baseurl = https://www.werkzgallery.com/nus//ind_images/'''
    '''endpoint = "A*******X/0**L_DSC_****.jpg'''
##    two = 77
##    four = 3683

    for i in range(1, 251):  # guess that each ceremony only got 250 students

        diff = abs(77 - 1)
        num = 3683 - diff
        num = str(num)
        i = str(i).zfill(3)

        endpoint = f"{i}L_DSC_{num}.jpg"
        url = f"https://www.werkzgallery.com/nus//ind_images/{nusnetid}/{endpoint}"
        print(url)
        filename = endpoint
        if getimage(url, filename):
            break


# open a text file with list of ids
with open('nusnetidsA.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        c(line.strip('\n'))
