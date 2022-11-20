#instagram:codeworld_11 lütfen takip edermisiniz?
#github:codeworld_11

import turtle
import time
import random

hız = 0.15#yılanın hızı

pencere = turtle.Screen()#oyun ekranı
pencere.title("Yılan Oyunu")#ekran başlığı
pencere.bgcolor('lightgreen')#ekran rengi
pencere.setup(width=600, height=600)#ekran büyüklükleri
pencere.tracer(0)#ekranın yenilenmemesi için

kafa = turtle.Turtle()#yılanın kafası
kafa.speed(0)#yılanın kafasını hızı
kafa.shape('square')#yılanın şekli
kafa.color('black')#yılanın rengi
kafa.penup()#yılan ekrana çizgi bırakmaması için
kafa.goto(0, 100)#yılanın başlayacağı yer
kafa.direction = 'stop'#yılana dur komutu

yemek = turtle.Turtle()#yılanının yiyeceği yemek
yemek.speed(0)#yemeğin hızı
yemek.shape('circle')#yemeğin şekli
yemek.color('red')#yemeğin rengi
yemek.penup()#yemek iz bırakmaması için
yemek.goto(0, 0)#yemeğin başlayacağı yer
yemek.shapesize(0.80, 0.80)#yemeğin ölçüleri

#instagram:codeworld_11 emeklerim lütfen takip edermisiniz 

kuyruklar = []#kuruklar için boş bi liste
puan = 0#puan durumu

#ekrana puanı yazdırma
yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Puan: {}'.format(puan), align='center', font=('Courier',24,'normal'))



def move():#yılanın kafasının koordinatları
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20)

def goUp():#yılanın lkafasının kontrol edebilmek için
    if kafa.direction != 'down':
        kafa.direction = 'up'
def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'
def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'
def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

#klavyeyi dinlemek için
pencere.listen()
pencere.onkey(goUp,'Up')
pencere.onkey(goDown,'Down')
pencere.onkey(goRight,'Right')
pencere.onkey(goLeft,'Left')


while True:
    pencere.update()#pencere güncelleme
    
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction = 'stop'

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)

        kuyruklar = []
        puan = 0
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier',24,'normal'))
        
        #instagram:codeworld_11


    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x,y)

        puan = puan + 10
        yaz.clear()
        yaz.write('Puan:{}'.format(puan), align='center', font=('Courier',24,'normal'))
        
        #kafanın arkasına eklenen kuruk kodları
        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x,y)
    
    move()
    time.sleep(hız)