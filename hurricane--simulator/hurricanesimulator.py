#To Add: 9/13/2016
#Troughs
#Months
#Season Creator
#Season Generator
#
#
#
#basics
#imports
import sys
#sys.path.append("/Users/tschiminovich/Desktop/stuff/other stuff/Hurricane Simulator.app/Contents/Resources")
import pygame
import math
from math import atan2, degrees, pi, sqrt
import random
from pygame.locals import *
from hurricane import Hurricane
from atlantic import Background
import os
#import numpy
#initialize
pygame.init()
#http://www.d-maps.com/m/world/atlantiquenord/atlantiquenord05.gif
#https://static.nationwide.com/static/icon-opt-link-hurricane-orange.gif?r=52

#screen
main_screen=pygame.display.set_mode((1274, 840), HWSURFACE|DOUBLEBUF|RESIZABLE)
screen=main_screen.copy()
background =  pygame.Surface((1274, 965), 0, screen)
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
size=[1274,840]
mpos=[0,0]
font = pygame.font.SysFont(None, 36)
font2 = pygame.font.SysFont(None, 120)
hurrtime=0
direction = 90
zaa = 0
s=2
souc=0
soucer = 0
carb = 0
mph=35
shearing=0
annular=0
bombo = 0
bombotime = 0
pointsx = [800]
pointsy = [700]
storms = ["0"]
names2017=["Arlene", "Bret", "Cindy", "Don", "Emily", "Franklin", "Gert", "Harvey", "Irma", "Jose", "Katia", "Lee", "Maria", "Nate", "Ophelia", "Philippe", "Rina", "Sean", "Tammy", "Vince", "Whitney"]
names2018=["Alberto", "Beryl", "Chris", "Debby", "Ernesto", "Florence", "Gordon", "Helene", "Isaac", "Joyce", "Kirk", "Leslie", "Michael", "Nadine", "Oscar", "Patty", "Rafael", "Sara", "Tony", "Valerie", "William"]
names2019=["Andrea", "Barry", "Chantal", "Dorian", "Erin", "Fernand", "Gabrielle", "Humberto", "Imelda", "Jerry", "Karen", "Lorenzo", "Melissa", "Nestor", "Olga", "Pablo", "Rebekah", "Sebastien", "Tanya", "Van", "Wendy"]
names2020=["Arthur", "Bertha", "Cristobal", "Dolly", "Edouard", "Fay", "Gonzalo", "Hanna", "Isaias", "Josephine", "Kyle", "Laura", "Marco", "Nana", "Omar", "Paulette", "Rene", "Sally", "Teddy", "Vicky", "Wilfred"]
names2021=["Ana", "Bill", "Claudette", "Danny", "Elsa", "Fred", "Grace", "Henri", "Ida", "Julian", "Kate", "Larry", "Mindy", "Nicholas", "Odette", "Peter", "Rose", "Sam", "Teresa", "Victor", "Wanda"]
names2022=["Alex", "Bonnie", "Colin", "Danielle", "Earl", "Fiona", "Gaston", "Hermine", "Ian", "Julia", "Karl", "Lisa", "Martin", "Nicole", "Owen", "Paula", "Richard", "Shary", "Tobias", "Virginie", "Walter"]
namesseason=["Arlene", "Bret", "Cindy", "Don", "Emily", "Franklin", "Gert", "Harvey", "Irma", "Jose", "Katia", "Lee", "Maria", "Nate", "Ophelia", "Philippe", "Rina", "Sean", "Tammy", "Vince", "Whitney"]
usenames=1
pause = 1
a=0
dd=0
nsub = 0
season = 1
speed = 5
h1x=0
h1y=0
troughx=0
troughy=0
trough2x=0
trough2y=0
h1s=0
jhelper = 0
maxmph = 0
month = 1
stormn=0
namen=0
hhelper=0
nonames=0
highsx=[]
highsy=[]
hurricanex=0.0
hurricaney=0.0
hurricane = Hurricane(random.randint(250,500), random.randint(630,700))
atlantic = Background(0, -150, "images/atlantique.gif")
seasonmenu = Background(0, -150, "images/seasonmenu.gif")
atlanticmenu = Background(0, -150, "images/atlantiquemenu.gif")
loadmenu = Background(0, -150, "images/savemenu.gif")
savemenu = Background(0, -150, "images/loadmenu.gif")

hurricaneimage = pygame.image.load("images/hurric.gif").convert_alpha()

draw_group = pygame.sprite.Group()
front_group = pygame.sprite.Group()
menu_group = pygame.sprite.Group()
season_group = pygame.sprite.Group()
save_group = pygame.sprite.Group()
load_group = pygame.sprite.Group()
draw_group.add(atlantic)
menu_group.add(atlanticmenu)
front_group.add(hurricane)
season_group.add(seasonmenu)
save_group.add(loadmenu)
load_group.add(savemenu)
q=-90
z=0
hurricanemph=[]
mb=0
minmb=10000
seasongenerator=0
pasthurrtime=0
oldhurrtime=0
hurricanetimes=[]
menu=0
savename=""

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))

#def move(o,s,d):
#        hurricaney+= math.cos(math.radians( q ) ) * s
#        hurricanex+= math.sin(math.radians( q ) ) * s
#        o.rect.y=int(hurricaney)
#        o.rect.x=int(hurricanex)
#        print(hurricanex,hurricaney,math.sin(math.radians( q ) ) * s,math.cos(math.radians( q ) ) * s)






#Clock
main_clock = pygame.time.Clock()
while True:
    filenames = next(os.walk("saves"))[2]
    mousepos=pygame.mouse.get_pos()
    mpos[0]=mousepos[0]*(1274/size[0])
    mpos[1]=mousepos[1]*(840/size[1])
    #if h1x>1000:
#        h1x=0
    dx = h1x - hurricane.rect.x
    dy = h1y - hurricane.rect.y
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)-180
    if degs<-180:
        degs+=360
    if degs>180:
        degs-=360
    dist = sqrt((dx**2)+(dy**2))







    for event in pygame.event.get():
        #quitting
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and pause==5 and ((event.key>96 and event.key<124) or (event.key>47 and event.key<58) or event.key==32 or event.key==8):
            if event.key==8:
                savename=savename[:len(savename)-1]
            elif len(savename)<16:
                savename+=str(chr(event.key))
        if event.type == VIDEORESIZE:
            main_screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
            main_screen.blit(pygame.transform.scale(screen, event.dict['size']), (0, 0))
            size = event.dict['size']
            pygame.display.flip()
        else:
            pass
    #clock, fps
    main_clock.tick(30)

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        if pause ==1:
            if month==1:
                hurrtime=24*151
            elif month==2:
                hurrtime=24*181
            elif month==3:
                hurrtime=24*212
            elif month==4:
                hurrtime=24*243
            elif month==5:
                hurrtime=24*273
            elif month==6:
                hurrtime=24*304
            #hurrtime=0
            minmb=10000
            zaa = 0
            highsx=[]
            highsy=[]
            if season==1:
                hurricane.rect.x=random.randint(250,330)
                hurricane.rect.y=random.randint(630,700)
            elif season==2:
                zaa = random.randint(0,1)
                if zaa == 0:
                    hurricane.rect.x=random.randint(600,850)
                    hurricane.rect.y=random.randint(650,720)
                else:
                    hurricane.rect.x=random.randint(400,850)
                    hurricane.rect.y=random.randint(620,760)
            elif season==3:
                #hurricane.rect.x=random.randint(150,450)
                #hurricane.rect.y=random.randint(630,700)
                hurricane.rect.x=random.randint(150,320)
                hurricane.rect.y=random.randint(630,660)
            elif season==4:
                hurricane.rect.x=random.randint(200,250)
                hurricane.rect.y=random.randint(500,570)
            elif season==5:
                hurricane.rect.x=random.randint(170,250)
                hurricane.rect.y=random.randint(540,560)
            hurricanex = hurricane.rect.x
            hurricaney = hurricane.rect.y
            carb=0
            if season==1:
                q=random.randint(-140,-90)
            elif season==5:
                q=random.randint(-100,-75)
            elif season==2:
                zaa = random.randint(0,1)
                if zaa == 0:
                    q=random.randint(-95,-85)
                else:
                    q=random.randint(-110,-80)
            else:
 #               q=random.randint(-210,-175)
#                 q=random.randint(-180,-140)
                q=random.randint(150,180)

            mph=35
            shearing=0
            bombo = 0
            nsub = 0
            pause = 0
            stormn+=1
            namen+=1

            hig = random.randint(1,3)
            if season==1 or season==5:
                for i in range(4):
                    highsx.append(random.randint(200,450))
                    highsy.append(random.randint(300,550))
                h1x = random.randint(200,450)
                h1y = random.randint(300,550)

            elif season==2:
                for i in range(4):
                    highsx.append(random.randint(200,800))
                    highsy.append(random.randint(300,550))
                h1x = random.randint(250,800)
                h1y = random.randint(300,550)
            elif season==3:
                for i in range(4):
                    highsx.append(random.randint(200,550))
                    highsy.append(random.randint(300,550))
                h1x = random.randint(250,550)
                h1y = random.randint(300,550)
            elif season==4:
                for i in range(4):
                    highsx.append(random.randint(200,500))
                    highsy.append(random.randint(300,500))
                h1x = random.randint(250,500)
                h1y = random.randint(300,500)
            h1s = random.randint(0, 1)
            troughx = random.randint(0,1000)
            troughy = random.randint(50,80)
            maxmph = 0

    if keys[K_RIGHT] and jhelper>10:
        season+=1
        if season>5:
            season = 1
        jhelper = 0
    jhelper+=1
    screen.fill((255, 255, 255))
    if keys[K_DOWN] and jhelper>10:
        month+=1
        if month>6:
            month = 1
        jhelper = 0
    if keys[K_j]:
        pause=4
        menu=0

    if keys[K_k] and pause==2:
        pause=3
        hurrtime=24*151

    if keys[K_l] and pause==2:
        pause=5
        menu=0
        savename=""
        seasongenerator=0

    if keys[K_m] and pause==1 and len(filenames)>0:
        pause=6
        menu=0
        savename=""
        helper6=0

    if pygame.mouse.get_pressed()[0]==1:
        if pause==4 and jhelper>10:
            y=0
            if mpos[0]>63 and mpos[0]<359 and mpos[1]>168 and mpos[1]<343:
                namesseason=names2017
                y=1
                nonames=0

            elif mpos[0]>483 and mpos[0]<782 and mpos[1]>168 and mpos[1]<343:
                namesseason=names2018
                y=1
                nonames=0

            elif mpos[0]>895 and mpos[0]<1194 and mpos[1]>168 and mpos[1]<343:
                namesseason=names2019
                y=1
                nonames=0

            elif mpos[0]>63 and mpos[0]<359 and mpos[1]>368 and mpos[1]<544:
                namesseason=names2020
                y=1
                nonames=0

            elif mpos[0]>483 and mpos[0]<782 and mpos[1]>368 and mpos[1]<544:
                namesseason=names2021
                y=1
                nonames=0

            elif mpos[0]>895 and mpos[0]<1194 and mpos[1]>368 and mpos[1]<544:
                namesseason=names2022
                y=1
                nonames=0

            elif mpos[0]>63 and mpos[0]<359 and mpos[1]>578 and mpos[1]<670:
                nonames=1
                y=1

            elif mpos[0]>895 and mpos[0]<1194 and mpos[1]>578 and mpos[1]<670:
                pause=1

            #rect rows: x=63-359,483-782,895-1194
            #rect columns: y=168-343,368-544,578-670
            if y==1:
                stormn=0
                namen=0
                pointsx=[800]
                pointsy=[700]
                hurricanetimes=[]
                hurricanemph=[]
                storms=["0"]
                pause=2
                seasongenerator=1
                lastmonth=0
                hurrtime=24*151
                x=0
        if menu==0 and jhelper>10 and mpos[0]>8 and mpos[0]<75 and mpos[1]>157 and mpos[1]<224:
            menu=1
            jhelper=0
        elif menu==1 and jhelper>10:
            if mpos[0]>36 and mpos[0]<300 and mpos[1]>24 and mpos[1]<85:
                if pause ==1:
                    if month==1:
                        hurrtime=24*151
                    elif month==2:
                        hurrtime=24*181
                    elif month==3:
                        hurrtime=24*212
                    elif month==4:
                        hurrtime=24*243
                    elif month==5:
                        hurrtime=24*273
                    elif month==6:
                        hurrtime=24*304
                    #hurrtime=0
                    minmb=10000
                    zaa = 0
                    highsx=[]
                    highsy=[]
                    if season==1:
                        hurricane.rect.x=random.randint(250,330)
                        hurricane.rect.y=random.randint(630,700)
                    elif season==2:
                        zaa = random.randint(0,1)
                        if zaa == 0:
                            hurricane.rect.x=random.randint(600,850)
                            hurricane.rect.y=random.randint(650,720)
                        else:
                            hurricane.rect.x=random.randint(400,850)
                            hurricane.rect.y=random.randint(620,760)
                    elif season==3:
                        #hurricane.rect.x=random.randint(150,450)
                        #hurricane.rect.y=random.randint(630,700)
                        hurricane.rect.x=random.randint(150,320)
                        hurricane.rect.y=random.randint(630,660)
                    elif season==4:
                        hurricane.rect.x=random.randint(200,250)
                        hurricane.rect.y=random.randint(500,570)
                    elif season==5:
                        hurricane.rect.x=random.randint(170,250)
                        hurricane.rect.y=random.randint(540,560)
                    hurricanex = hurricane.rect.x
                    hurricaney = hurricane.rect.y
                    carb=0
                    if season==1:
                        q=random.randint(-140,-90)
                    elif season==5:
                        q=random.randint(-100,-75)
                    elif season==2:
                        zaa = random.randint(0,1)
                        if zaa == 0:
                            q=random.randint(-95,-85)
                        else:
                            q=random.randint(-110,-80)
                    else:
         #               q=random.randint(-210,-175)
        #                 q=random.randint(-180,-140)
                        q=random.randint(150,180)

                    mph=35
                    shearing=0
                    bombo = 0
                    nsub = 0
                    pause = 0
                    stormn+=1
                    namen+=1

                    hig = random.randint(1,3)
                    if season==1 or season==5:
                        for i in range(4):
                            highsx.append(random.randint(200,450))
                            highsy.append(random.randint(300,550))
                        h1x = random.randint(200,450)
                        h1y = random.randint(300,550)

                    elif season==2:
                        for i in range(4):
                            highsx.append(random.randint(200,800))
                            highsy.append(random.randint(300,550))
                        h1x = random.randint(250,800)
                        h1y = random.randint(300,550)
                    elif season==3:
                        for i in range(4):
                            highsx.append(random.randint(200,550))
                            highsy.append(random.randint(300,550))
                        h1x = random.randint(250,550)
                        h1y = random.randint(300,550)
                    elif season==4:
                        for i in range(4):
                            highsx.append(random.randint(200,500))
                            highsy.append(random.randint(300,500))
                        h1x = random.randint(250,500)
                        h1y = random.randint(300,500)
                    h1s = random.randint(0, 1)
                    troughx = random.randint(0,1000)
                    troughy = random.randint(50,80)
                    maxmph = 0
                    menu=0
            if mpos[0]>36 and mpos[0]<300 and mpos[1]>96 and mpos[1]<156:
                pause=4
                menu=0
            if mpos[0]>36 and mpos[0]<300 and mpos[1]>166 and mpos[1]<228:
                if pause==2:
                    pause=3
                    hurrtime=24*151
                    menu=0
            if mpos[0]>36 and mpos[0]<300 and mpos[1]>235 and mpos[1]<297:
                if pause==2:
                    pause=5
                    menu=0
                    savename=""
                    seasongenerator=0
            if mpos[0]>36 and mpos[0]<300 and mpos[1]>310 and mpos[1]<365 and len(filenames)>0:
                pause=6
                menu=0
                savename=""
                helper6=0
            elif mpos[0]>300 or mpos[1]>370:
                menu=0
            jhelper=0
    if pause==2 and hurrtime<24*334:
#        hurrtime+=1
        hurrtime+=6
        if hurrtime<24*181: month=1
        elif hurrtime<24*212: month=2
        elif hurrtime<24*243: month=3
        elif hurrtime<24*273: month=4
        elif hurrtime<24*304: month=5
        elif hurrtime<24*334: month=6


        #pause=0
        if month==1:
            if lastmonth==0:
                x=int(random.triangular(65,300,100))
                lastmonth=1
            r=random.randint(1,x)
#            r=random.randint(1,1000)
        elif month==2:
            if lastmonth==1:
                x=int(random.triangular(40,100,55))
                lastmonth=2
            r=random.randint(1,x)
#            r=random.randint(1,350)
        elif month==3:
            if lastmonth==2:
                x=int(random.triangular(18,55,29))
                lastmonth=3
            r=random.randint(1,x)
#            r=random.randint(1,200)
        elif month==4:
            if lastmonth==3:
                x=int(random.triangular(13,46,25))
                lastmonth=4
            r=random.randint(1,x)
#            r=random.randint(1,170)
        elif month==5:
            if lastmonth==4:
                x=int(random.triangular(26,75,37))
                lastmonth=5
            r=random.randint(1,x)
#            r=random.randint(1,250)
        elif month==6:
            if lastmonth==5:
                x=int(random.triangular(65,300,100))
                lastmonth=6
            r=random.randint(1,x)
#            r=random.randint(1,1000)
        if r==1:
            oldhurrtime=hurrtime
            if month==1:
                r=random.randint(1,10)
                if r<=2:
                    season=5
                else:
                    season=1
            elif month==2:
                r=random.randint(1,20)
                if r<=4:
                    season=2
                elif r<=8:
                    season=5
                else:
                    season=1
            elif month==3:
                r=random.randint(1,20)
                if r<=1:
                    season=3
                elif r<=2:
                    season=4
                elif r<=4:
                    season=5
                elif r<=8:
                    season=1
                else:
                    season=2
            elif month==4:
                r=random.randint(1,20)
                if r<=2:
                    season=3
                elif r<=4:
                    season=4
                elif r<=6:
                    season=5
                elif r<=9:
                    season=1
                else:
                    season=2
            elif month==5:
                r=random.randint(1,20)
                if r<=2:
                    season=2
                elif r<=8:
                    season=4
                else:
                    season=3
            elif month==6:
                r=random.randint(1,10)
                if r<=3:
                    season=4
                else:
                    season=3
            minmb=10000
            zaa = 0
            highsx=[]
            highsy=[]
            if season==1:
                hurricane.rect.x=random.randint(250,330)
                hurricane.rect.y=random.randint(630,700)
            elif season==2:
                zaa = random.randint(0,1)
                if zaa == 0:
                    hurricane.rect.x=random.randint(600,850)
                    hurricane.rect.y=random.randint(650,720)
                else:
                    hurricane.rect.x=random.randint(400,850)
                    hurricane.rect.y=random.randint(620,760)
            elif season==3:
                #hurricane.rect.x=random.randint(150,450)
                #hurricane.rect.y=random.randint(630,700)
                hurricane.rect.x=random.randint(150,320)
                hurricane.rect.y=random.randint(630,660)
            elif season==4:
                hurricane.rect.x=random.randint(200,250)
                hurricane.rect.y=random.randint(500,570)
            elif season==5:
                hurricane.rect.x=random.randint(170,250)
                hurricane.rect.y=random.randint(540,560)
            hurricanex = hurricane.rect.x
            hurricaney = hurricane.rect.y
            carb=0
            if season==1:
                q=random.randint(-140,-90)
            elif season==5:
                q=random.randint(-100,-75)
            elif season==2:
                zaa = random.randint(0,1)
                if zaa == 0:
                    q=random.randint(-95,-85)
                else:
                    q=random.randint(-110,-80)
            else:
    #               q=random.randint(-210,-175)
    #                 q=random.randint(-180,-140)
                q=random.randint(150,180)

            mph=35
            shearing=0
            bombo = 0
            nsub = 0
            pause = 0
            stormn+=1
            namen+=1

            hig = random.randint(1,3)
            if season==1 or season==5:
                for i in range(4):
                    highsx.append(random.randint(200,450))
                    highsy.append(random.randint(300,550))
                h1x = random.randint(200,450)
                h1y = random.randint(300,550)

            elif season==2:
                for i in range(4):
                    highsx.append(random.randint(200,800))
                    highsy.append(random.randint(300,550))
                h1x = random.randint(250,800)
                h1y = random.randint(300,550)
            elif season==3:
                for i in range(4):
                    highsx.append(random.randint(200,550))
                    highsy.append(random.randint(300,550))
                h1x = random.randint(250,550)
                h1y = random.randint(300,550)
            elif season==4:
                for i in range(4):
                    highsx.append(random.randint(200,500))
                    highsy.append(random.randint(300,500))
                h1x = random.randint(250,500)
                h1y = random.randint(300,500)
            h1s = random.randint(0, 1)
            troughx = random.randint(0,1000)
            troughy = random.randint(50,80)
            maxmph = 0


    if pause == 0:
        menu=0
        hurrtime+=1
        mb=((25-mph)/(((hurricane.rect.y-300)/300)+1))+1015
        if mb<minmb:
            minmb=mb
        #print(((hurricane.rect.y-300)/200)+1)
        if mb>1000:
            h1x=highsx[0]
            h1y=highsy[0]
        elif mb>975:
            h1x=highsx[1]
            h1y=highsy[1]
        elif mb>945:
            h1x=highsx[2]
            h1y=highsy[2]
        else:
            h1x=highsx[3]
            h1y=highsy[3]
#        hhelper+=1
#        if hhelper%50==0:
#            h1x = random.randint(50,550)
#            h1y = random.randint(300,650)
        troughx+=5
        if troughx>1000:
            troughx=0
        if q<-180:
            q+=360
        if q>180:
            q-=360
        simp=random.randint(1,1000)
        q-=random.randint(-2,2)
        if (degs>90 or degs <-90) and abs(dd)>60:
            if h1s == 0:
                if mph>110 and q<0:
                    q-=random.randint(1,3)
                elif mph>80 and q<0:
                    q-=random.randint(0,3)
                elif mph>60 and q<0:
                    q-=random.randint(0,2)
                elif hurricane.rect.y<550:
                    q-=random.randint(0,2)
            elif h1s == 1:
                if mph>110 and q<0:
                    q-=random.randint(1,5)
                elif mph>80 and q<0:
                    q-=random.randint(1,4)
                elif mph>60 and q<0:
                    q-=random.randint(1,3)
                elif hurricane.rect.y<550:
                    q-=random.randint(1,2)
        #if hurricane.rect.y<h1y and (q<130 and q>0) and mph>50:
 #           q-=random.randint(-3,1)
        if hurricane.rect.y<h1y and q>85+(mph/2):
            if h1s == 0:
                q-=random.randint(-1,4)
            elif h1s == 1:
                q-=random.randint(1,4)
        if speed<2:
            q-=random.randint(-8,-2)
        if q>-85 and q<0 and hurricane.rect.y>650:
            q-=random.randint(3,7)

        if hurricane.rect.x-troughx>0 and hurricane.rect.x-troughx<100 and hurricane.rect.y<troughy:
            q=135
#        if a<-60 and hurricane.rect.x<700:
#            q+=(-a)/18
#        if a>60 and hurricane.rect.x<700:
#            q+=(-a)/18

        #print (hurricane.rect.y, q)
#        if hurricane.rect.x>600:
#
#            q-=random.randint(-2,2)
#        else:
#            if carb == 0:
#                if q>105 or q<75:
#                    if nsub==1:
#                        q -= random.randint(-2, 2)
#                    elif nsub==2:
#                        q -= random.randint(-3, 1)
#                    else:
#                        if season==3:
#                            q-=random.randint(-2,3)
#                        else:
#                            q-=random.randint(-1,4)
#                else:
#                    q-=random.randint(-3,3)
#            else:
#                if hurricane.rect.y>500:
#                    if hurricane.rect.x>250:
#                        q-=random.randint(-2,2)
#                    else:
#                        q-=random.randint(-1,3)
#                else:
#                    carb=0
        if hurricane.rect.y<300:
            simp=random.randint(1,100)
            if simp==100:
                if seasongenerator==1:
                    pause = 2
                    hurrtime=oldhurrtime
                else:
                    pause=1
                if maxmph<39:
                    for i in range(len(storms)):
                        if storms[i]==namesseason[namen]:
                            storms.pop(i)
                            storms.insert(i,str(stormn))
                    namen-=1
        simp = random.randint(1,200)
        if hurricane.rect.y>600 and simp<=2:
            carb=1
        if hurricane.rect.y<600 and simp==3:
            nsub = 1
        if hurricane.rect.y<600 and simp==4:
            nsub = 2
        if bombotime>0:
            bombotime+=1
        if bombotime>15:
            bombo = 0

        #if hurricane.rect.y>550:
#            speed = (abs(abs(q)-180)/30)+(abs(hurricane.rect.y-600)/400)+2
#        elif hurricane.rect.y>450:
#            speed = (abs(abs(q-45)-180)/30)+(abs(hurricane.rect.y-600)/400)+2
#        else:
#            speed = (abs(abs(q-90)-180)/30)+(abs(hurricane.rect.y-600)/400)+1
        #speed=5
        if dist>500:

            degs = abs(hurricane.rect.y-1000)-500
            if degs<-90:
                degs = -90
            elif degs>90:
                degs = 90

            a = q - degs
            a = (a + 180) % 360 - 180

            speed = (abs(a)/30)+2
#            speed = speed / 2

            hurricaney+= math.cos(math.radians( q ) ) * s
            hurricanex+= math.sin(math.radians( q ) ) * s
            hurricane.rect.y=int(hurricaney)
            hurricane.rect.x=int(hurricanex)

        else:
            a = q - degs
            a = (a + 180) % 360 - 180

            speed = abs(abs((dist/200)-6)/100*(abs((abs(a)+1)/2)-100))

            dd = q - (degs-90)
            dd = (dd + 180) % 360 - 180

            speed+=((abs(dd)-90)/50)/(dist/100)

            if hurricane.rect.y<h1y and (q>45 and q<135):
                speed-=(hurricane.rect.y/100)-6
            if q>-90 and q<90:
                speed-=speed/((abs(q)/45)+1)
#            speed = speed / 2
            hurricaney+= math.cos(math.radians( q ) ) * speed
            hurricanex+= math.sin(math.radians( q ) ) * speed
            hurricane.rect.y=int(hurricaney)
            hurricane.rect.x=int(hurricanex)


        if hurricane.rect.x<4 or hurricane.rect.x>1240 or hurricane.rect.y<4 or hurricane.rect.y>810:
            if seasongenerator==1:
                pause = 2
                hurrtime=oldhurrtime
            else:
                pause=1
            if maxmph<39:
                for i in range(len(storms)):
                    if storms[i]==namesseason[namen]:
                        storms.pop(i)
                        storms.insert(i,str(stormn))
                namen-=1

        if mph<20:
            if seasongenerator==1:
                pause = 2
                hurrtime=oldhurrtime
            else:
                pause=1
            if maxmph<39:
                #if len(storms)>
                for i in range(len(storms)):
                    if storms[i]==namesseason[namen]:
                        storms.pop(i)
                        storms.insert(i,str(stormn))
                namen-=1

        simp=random.randint(1,100)
        if simp==1:
            if shearing==0:
                shearing=1
            else:
                shearing=0
        if hurricane.rect.y>530 and hurricane.rect.x<400 and shearing == 0 and mph<131:
            if month==3 or month==4 or month==5:
                if hurricane.rect.x>140 and hurricane.rect.x<300:
                    simp = random.randint(1,25)
                else:
                    simp = random.randint(1,100)
            else:
                if hurricane.rect.x>140 and hurricane.rect.x<300:
                    simp = random.randint(1,150)
            if simp==1:
                bombo = 1
                bombotime = 1



        #screen fill

        draw_group.draw(screen)
        b = screen.get_at((hurricane.rect.x+25,hurricane.rect.y+25))
        if b==(255,255,255,255):
            bombo = 0
            if mph<75:
                mph+=random.randint(-5,-2)
            else:
                mph+=random.randint(-8,-4)

        else:
            if month==1 or month==2:
                if (hurricane.rect.y>470 and hurricane.rect.x<560) or hurricane.rect.y>670:
                    if mph>155:
                        mph+=random.randint(-4,2)
                    elif mph>115:
                        mph+=random.randint(-3,2)
                    elif mph>75:
                        mph+=random.randint(-2,2)
                    else:
                        mph+=random.randint(-2,3)
                    region = 3
                elif (hurricane.rect.y>370 and hurricane.rect.x<720) or hurricane.rect.y>600:
                    if mph>115:
                        mph+=random.randint(-7,2)
                    elif mph>75:
                        mph+=random.randint(-4,2)
                    else:
                        mph+=random.randint(-2,2)
                    region = 2
                else:
                    if mph>115:
                        mph+=random.randint(-9,2)
                    elif mph>75:
                        mph+=random.randint(-7,2)
                    else:
                        mph+=random.randint(-5,2)
                    region = 1

            elif month==3 or month==4:
                if hurricane.rect.y>530 and hurricane.rect.y<700 and hurricane.rect.x>140 and hurricane.rect.x<300:
                    if mph>155:
                        mph+=random.randint(-3,2)
                    elif mph>115:
                        mph+=random.randint(-2,3)
                    elif mph>75:
                        mph+=random.randint(-1,3)
                    else:
                        mph+=random.randint(-1,4)
                    region = 4
                elif (hurricane.rect.y>470 and hurricane.rect.x<560) or hurricane.rect.y>670:
                    if mph>155:
                        mph+=random.randint(-4,2)
                    elif mph>115:
                        mph+=random.randint(-3,2)
                    elif mph>75:
                        mph+=random.randint(-2,3)
                    else:
                        mph+=random.randint(-2,4)
                    region = 3
                elif (hurricane.rect.y>370 and hurricane.rect.x<720) or hurricane.rect.y>600:
                    if mph>115:
                        mph+=random.randint(-5,2)
                    elif mph>75:
                        mph+=random.randint(-3,2)
                    else:
                        mph+=random.randint(-2,3)
                    region = 2
                else:
                    if mph>115:
                        mph+=random.randint(-7,2)
                    elif mph>75:
                        mph+=random.randint(-5,2)
                    else:
                        mph+=random.randint(-3,2)
                    region = 1

            elif month==5:
                if hurricane.rect.y>530 and hurricane.rect.y<700 and hurricane.rect.x>140 and hurricane.rect.x<300:
                    if mph>155:
                        mph+=random.randint(-3,2)
                    elif mph>115:
                        mph+=random.randint(-2,3)
                    elif mph>75:
                        mph+=random.randint(-1,3)
                    else:
                        mph+=random.randint(-1,4)
                    region = 4
                elif hurricane.rect.y>500 and hurricane.rect.x<470:
                    if mph>155:
                        mph+=random.randint(-4,2)
                    elif mph>115:
                        mph+=random.randint(-3,2)
                    elif mph>75:
                        mph+=random.randint(-2,3)
                    else:
                        mph+=random.randint(-2,4)
                    region = 3
                elif (hurricane.rect.y>430 and hurricane.rect.x<550) or hurricane.rect.y>640:
                    if mph>115:
                        mph+=random.randint(-5,2)
                    elif mph>75:
                        mph+=random.randint(-3,2)
                    else:
                        mph+=random.randint(-2,3)
                    region = 2
                else:
                    if mph>115:
                        mph+=random.randint(-7,2)
                    elif mph>75:
                        mph+=random.randint(-5,2)
                    else:
                        mph+=random.randint(-3,2)
                    region = 1

            elif month==6:
                if hurricane.rect.y>500 and hurricane.rect.x<470:
                    if mph>155:
                        mph+=random.randint(-4,2)
                    elif mph>115:
                        mph+=random.randint(-3,2)
                    elif mph>75:
                        mph+=random.randint(-2,2)
                    else:
                        mph+=random.randint(-2,3)
                    region = 3
                elif (hurricane.rect.y>430 and hurricane.rect.x<550) or hurricane.rect.y>640:
                    if mph>115:
                        mph+=random.randint(-7,2)
                    elif mph>75:
                        mph+=random.randint(-5,2)
                    else:
                        mph+=random.randint(-2,2)
                    region = 2
                else:
                    if mph>115:
                        mph+=random.randint(-9,2)
                    elif mph>75:
                        mph+=random.randint(-7,2)
                    else:
                        mph+=random.randint(-4,2)
                    region = 1
        if shearing==1:
            if annular==0:
                mph-=2
        if bombo ==1:
            mph+=4
            simp=random.randint(1,10)
            if simp==1:
                bombo=0
        hurricanemph.append(mph)
        if seasongenerator==1:
            hurricanetimes.append(hurrtime)
        for i in range (len(pointsx)):
            if hurricanemph[i-1]<39:
                pygame.draw.rect(screen, (64,64,64), (pointsx[i-1], pointsy[i-1], 5, 5))
            elif hurricanemph[i-1]<74:
                pygame.draw.rect(screen, (0,140,0), (pointsx[i-1], pointsy[i-1], 5, 5))
            elif hurricanemph[i-1]<96:
                pygame.draw.rect(screen, (255,255,136), (pointsx[i-1], pointsy[i-1], 5, 5))
            elif hurricanemph[i-1]<111:
                pygame.draw.rect(screen, (255,116,0), (pointsx[i-1], pointsy[i-1], 5, 5))
            elif hurricanemph[i-1]<131:
                pygame.draw.rect(screen, (204,0,0), (pointsx[i-1], pointsy[i-1], 5, 5))
            elif hurricanemph[i-1]<156:
                pygame.draw.rect(screen, (255,0,132), (pointsx[i-1], pointsy[i-1], 5, 5))
            else:
                pygame.draw.rect(screen, (164,70,149), (pointsx[i-1], pointsy[i-1], 5, 5))
        if mph>maxmph:
            maxmph = mph
        pointsx.append(hurricane.rect.x+25)
        pointsy.append(hurricane.rect.y+25)
        if namen>0 and namen<22 and nonames==0:
            storms.append(namesseason[namen-1])
        else:
            storms.append(stormn)
        front_group.draw(screen)
    if pause==1 or pause==2 or pause==3:
        draw_group.draw(screen)
        if len(pointsx)>1:
            for i in range (len(pointsx)):
                if hurricanemph[i-1]<39:
                    pygame.draw.rect(screen, (64,64,64), (pointsx[i-1], pointsy[i-1], 5, 5))
                elif hurricanemph[i-1]<74:
                    pygame.draw.rect(screen, (0,140,0), (pointsx[i-1], pointsy[i-1], 5, 5))
                elif hurricanemph[i-1]<96:
                    pygame.draw.rect(screen, (255,255,136), (pointsx[i-1], pointsy[i-1], 5, 5))
                elif hurricanemph[i-1]<111:
                    pygame.draw.rect(screen, (255,116,0), (pointsx[i-1], pointsy[i-1], 5, 5))
                elif hurricanemph[i-1]<131:
                    pygame.draw.rect(screen, (204,0,0), (pointsx[i-1], pointsy[i-1], 5, 5))
                elif hurricanemph[i-1]<156:
                    pygame.draw.rect(screen, (255,0,132), (pointsx[i-1], pointsy[i-1], 5, 5))
                else:
                    pygame.draw.rect(screen, (164,70,149), (pointsx[i-1], pointsy[i-1], 5, 5))
    if pause==4:
        season_group.draw(screen)
    if pause==5:
        save_group.draw(screen)
        draw_text(savename, font2, screen, 150,480)
        if keys[K_RETURN] and savename!="":
            f = open('saves/'+savename+'.txt', 'w')
            for i in range(len(pointsx)):
                f.write(str(pointsx[i])+ '\n')
            f.write('c\n')
            for i in range(len(pointsy)):
                f.write(str(pointsy[i])+ '\n')
            f.write('c\n')
            for i in range(len(hurricanetimes)):
                f.write(str(hurricanetimes[i])+ '\n')
            f.write('c\n')
            for i in range(len(hurricanemph)):
                f.write(str(hurricanemph[i])+ '\n')
            f.write('c\n')
            for i in range(len(storms)):
                f.write(str(storms[i])+ '\n')
            f.write('c\n')
            f.close()
            pause=2
            seasongenerator=1
    if pause==6:
        draw_text(savename, font2, screen, 150,480)
        load_group.draw(screen)
        if keys[K_LEFT] and jhelper>10:
            jhelper=0
            helper6+=1
            if helper6>=len(filenames):
                helper6=0

        if keys[K_RIGHT] and jhelper>10:
            jhelper=0
            helper6-=1
            if helper6==-1:
                helper6=len(filenames)-1
        if helper6<len(filenames):
            savename=filenames[helper6]
            draw_text(savename, font2, screen, 150,480)                
        if keys[K_RETURN]:
            pointsx=[]
            pointsy=[]
            hurricanetimes=[]
            hurricanemph=[]
            storms=[]
            f = open('saves/'+savename, 'r')
    #        print("bla")
            e=""
            while e!="c\n":
                e=f.readline()
                if e!="c\n":
                    pointsx.append(int(e))
    #        print("test")
            e=""
            while e!="c\n":
                e=f.readline()
                if e!="c\n":
                    pointsy.append(int(e))
            e=""
            while e!="c\n":
                e=f.readline()
                if e!="c\n":
                    hurricanetimes.append(int(e))
            e=""
            while e!="c\n":
                e=f.readline()
                if e!="c\n":
                    hurricanemph.append(int(e))
            e=""
            while e!="c\n":
                e=f.readline()
                if e!="c\n":
                    storms.append(e.rstrip())
    #        print(pointsx, "e")

            f.close()
            pause=2
            seasongenerator=1
            hurrtime=24*334
    if pause==3 and hurrtime<24*334:
        r=0
        for i in range(len(hurricanetimes)):
            if hurricanetimes[i]==hurrtime:
                screen.blit(hurricaneimage, (pointsx[i+1]-25,pointsy[i+1]-25))
                r+=1
        if r==0:
            hurrtime+=6
        else:
            hurrtime+=1
    elif hurrtime>=24*334 and pause==3:
        pause=2
    #screen.blit(hurricaneimage, (0,0))
    if pause!=4 and pause!=5 and pause!=6:
        draw_text(str(mph)+ ' MPH', font, screen, 10, 10)
        draw_text(str(int(mb))+ ' MB', font, screen, 10, 70)
        if minmb!=10000:
            draw_text(str(int(minmb))+ ' MB MIN', font, screen, 10, 100)
        draw_text(str(maxmph) + ' MPH MAX', font, screen, 10, 40)
        if hurrtime<24*31:
            draw_text('January '+str(int((hurrtime/24)+1))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*59:
            draw_text('February '+str(int((hurrtime/24)-30))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*90:
            draw_text('March '+str(int((hurrtime/24)-58))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*120:
            draw_text('April '+str(int((hurrtime/24)-89))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*151:
            draw_text('May '+str(int((hurrtime/24)-119))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*181:
            draw_text('June '+str(int((hurrtime/24)-150))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*212:
            draw_text('July '+str(int((hurrtime/24)-180))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*243:
            draw_text('August '+str(int((hurrtime/24)-211))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*273:
            draw_text('September '+str(int((hurrtime/24)-242))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*304:
            draw_text('October '+str(int((hurrtime/24)-272))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*334:
            draw_text('November '+str(int((hurrtime/24)-303))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        elif hurrtime<24*365:
            draw_text('December '+str(int((hurrtime/24)-333))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 130)
        else:
            hurrtime-=(24*365)
            draw_text('January '+str(int((hurrtime/24)+1))+' at '+str(int(hurrtime-(int(hurrtime/24))*24))+':00', font, screen, 10, 160)

        #draw_text('H', font, screen, h1x, h1y)
        #draw_text('T', font, screen, troughx, troughy)
        if season==1:
            draw_text('Caribbean West', font, screen, 1050, 10)
        elif season==2:
            draw_text('Cape Verde', font, screen, 1050, 10)
        elif season==3:
            draw_text('Caribbean North' , font, screen, 1050, 10)
        elif season==4:
            draw_text('Bahamas', font, screen, 1050, 10)
        else:
            draw_text('Bahamas West', font, screen, 1050, 10)
        if month==1:
            draw_text('June', font, screen, 850, 10)
        elif month==2:
            draw_text('July', font, screen, 850, 10)
        elif month==3:
            draw_text('August', font, screen, 850, 10)
        elif month==4:
            draw_text('September', font, screen, 850, 10)
        elif month==5:
            draw_text('October', font, screen, 850, 10)
        elif month==6:
            draw_text('November', font, screen, 850, 10)
    printr1=0
    if pause!=4 and pause!=5 and pause!=6:
        for i in range(len(storms)):
            if (mpos[0]>pointsx[i]-1 and mpos[0]<pointsx[i]+6) and (mpos[1]>pointsy[i]-1 and mpos[1]<pointsy[i]+6) and printr1==0:
                draw_text('Storm ' + str(storms[i]), font, screen, 650, 10)
                if seasongenerator==1:
                    htime=hurricanetimes[i-1]
                    if htime<24*31:
                        draw_text('January '+str(int((htime/24)+1))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*59:
                        draw_text('February '+str(int((htime/24)-30))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*90:
                        draw_text('March '+str(int((htime/24)-58))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*120:
                        draw_text('April '+str(int((htime/24)-89))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*151:
                        draw_text('May '+str(int((htime/24)-119))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*181:
                        draw_text('June '+str(int((htime/24)-150))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*212:
                        draw_text('July '+str(int((htime/24)-180))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*243:
                        draw_text('August '+str(int((htime/24)-211))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*273:
                        draw_text('September '+str(int((htime/24)-242))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*304:
                        draw_text('October '+str(int((htime/24)-272))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*334:
                        draw_text('November '+str(int((htime/24)-303))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                    elif htime<24*365:
                        draw_text('December '+str(int((htime/24)-333))+' at '+str(int(htime-(int(htime/24))*24))+':00', font, screen, 300, 10)
                draw_text(str(hurricanemph[i-1]) + "MPH", font, screen, 200, 10)
                printr1=1
    if menu==1:
        menu_group.draw(screen)
    main_screen.blit(pygame.transform.scale(screen, size), (0,0))
    pygame.display.flip()
