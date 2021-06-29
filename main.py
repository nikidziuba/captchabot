from captcha.image import ImageCaptcha
import cv2
import requests
import time
import os


quit = False
image = ImageCaptcha(width=500, height=187)
start = True
while start:
    print('Wybierz: ')
    print('1.MeKa')
    print('2.MaKo')
    print('3.MSTFW')
    print('4. Własne')
    inp = input()
    if inp == '1':
        pcode = 'zuJWX5kr'
        start = False1
    else:
        if inp == '2':
            pcode = 'MvnJsmAD'
            start = False
        else:
            if inp == '3':
                pcode = 'S94NTVsK'
                start = False
            else:
                if inp == '4':
                    pcode = input('Podaj kod: ')
                    start = False
                else:
                    print('Nie poprawny kod')




i = 0
f = open("temp.txt", "w")
f.write(requests.get('https://pastebin.com/raw/' + pcode).text)
with open('temp.txt','r') as f:

    for line in f:
        if quit:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit = True
            break
        for word in line.split():

            data = image.generate(word)
            if word == ' ':
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                quit = True
                break
            if i == 0:
                image.write(word, 'temp2.png')
                im = cv2.imread('temp2.png')
                cv2.imshow('Captcha', im)
                time.sleep(1)
                cv2.waitKey(1)
                if os.path.isfile('temp1.png'):
                    os.remove('temp1.png')
                i = 1
            else:
                if i == 1:
                    image.write(word, 'temp1.png')
                    im = cv2.imread('temp1.png')
                    cv2.imshow('Captcha', im)
                    time.sleep(1)
                    cv2.waitKey(1)
                    if os.path.isfile('temp2.png'):
                        os.remove('temp2.png')
                    i = 0


if os.path.isfile('temp1.png'):
    os.remove('temp1.png')
if os.path.isfile('temp2.png'):
    os.remove('temp2.png')
os.remove('temp.txt')
cv2.waitKey(0)
cv2.destroyWindow('Captcha')