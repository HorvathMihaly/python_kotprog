import pygame
import sys
import os
import time

def main():
    #start pozíció
    x = 5
    y = 7

    #kocsisor kezdő pont meghatározása
    lane1index = 0
    lane2index = 0
    lane3index = 0
    lane4index = 0
    
    #pygame ablak
    canvas = pygame.display.set_mode( (11 * 100, 8 * 100) )
    pygame.display.set_caption("Misi Frogger")
    clock = pygame.time.Clock()

    #fájl elérési út megadása
    dirname = os.path.dirname(__file__)
    racoon_filename = os.path.join(dirname, 'raccoon1.png')
    grass_filename = os.path.join(dirname, 'fu.jpg') 
    car1_filename = os.path.join(dirname, 'auto1.png')
    car2_filename = os.path.join(dirname, 'auto2.png')
    truck1_filename = os.path.join(dirname, 'kamion1.png')
    truck2_filename = os.path.join(dirname, 'kamion2.png')

    #mosómedveképek betöltése
    racoonImgRight = pygame.image.load(racoon_filename)
    racoonImgRight = pygame.transform.scale(racoonImgRight, (100, 100))
    racoonImgLeft = pygame.transform.flip(racoonImgRight, True, False)
    
    racoonImgCurrent = racoonImgRight

    #járművek képeinek betöltése
    truck1ImgLeft = pygame.image.load(truck1_filename)
    truck1ImgLeft = pygame.transform.scale(truck1ImgLeft, (200, 100))
    truck1ImgRight = pygame.transform.flip(truck1ImgLeft, True, False)

    truck2ImgLeft = pygame.image.load(truck2_filename)
    truck2ImgLeft = pygame.transform.scale(truck2ImgLeft, (200, 100))
    truck2ImgRight = pygame.transform.flip(truck2ImgLeft, True, False)

    car1ImgLeft = pygame.image.load(car1_filename)
    car1ImgLeft = pygame.transform.scale(car1ImgLeft, (200, 100))
    car1ImgRight = pygame.transform.flip(car1ImgLeft, True, False)

    car2ImgLeft = pygame.image.load(car2_filename)
    car2ImgLeft = pygame.transform.scale(car2ImgLeft, (200, 100))
    car2ImgRight = pygame.transform.flip(car2ImgLeft, True, False)
    
    #pihenőhely kép betöltése
    island = pygame.image.load(grass_filename)

    #kocsisorok megrajzolása
    lane1 = pygame.Surface((30 * 100, 100))
    lane1.blit(truck1ImgRight, (0,0))
    lane1.blit(car1ImgRight, (5*100,0))
    lane1.blit(car2ImgRight, (9*100,0))
    lane1.blit(truck2ImgRight, (14*100,0))
    lane1.blit(car2ImgRight, (21*100,0))
    lane1.blit(truck1ImgRight, (24*100,0))
    lane1.blit(car1ImgRight, (27*100,0))

    lane2 = pygame.Surface((30*100, 100))
    lane2.blit(car1ImgLeft, (0,0))
    lane2.blit(truck2ImgLeft, (3*100,0))
    lane2.blit(car2ImgLeft, (7*100,0))
    lane2.blit(car1ImgLeft, (13*100,0))
    lane2.blit(truck1ImgLeft, (16*100,0))
    lane2.blit(car2ImgLeft, (20*100,0))
    lane2.blit(car1ImgLeft, (26*100,0))

    lane3 = pygame.Surface((30 * 100, 100))
    lane3.blit(car1ImgRight, (0,0))
    lane3.blit(car1ImgRight, (5*100,0))
    lane3.blit(car2ImgRight, (9*100,0))
    lane3.blit(truck2ImgRight, (14*100,0))
    lane3.blit(truck1ImgRight, (22*100,0))
    lane3.blit(truck2ImgRight, (27*100,0))

    lane4 = pygame.Surface((30*100, 100))
    lane4.blit(truck2ImgLeft, (0,0))
    lane4.blit(truck1ImgLeft, (3*100,0))
    lane4.blit(car1ImgLeft, (8*100,0))
    lane4.blit(car2ImgLeft, (13*100,0))
    lane4.blit(truck1ImgLeft, (16*100,0))
    lane4.blit(car2ImgLeft, (21*100,0))
    lane4.blit(truck1ImgLeft, (26*100,0))

    #font betöltése
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 40)

    #kezdő idő
    startTime = time.time()

    #játék logika
    while True:
        
        #billentyűzet input lekezelés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # UP
                if event.key == pygame.K_UP:
                    if y - 1 >= 1:
                        y = y - 1
                    print("K_UP")
                # DOWN
                elif event.key == pygame.K_DOWN:
                    if  y + 1 <= 7:
                        y = y + 1
                    print ("K_DOWN")
                # RIGHT
                elif event.key == pygame.K_RIGHT:
                    if  x + 1 <= 10:
                        x = x + 1
                        racoonImgCurrent = racoonImgRight
                    print ("K_RIGHT")
                # LEFT
                elif event.key == pygame.K_LEFT:
                
                    if x - 1 >= 0:
                        x = x - 1
                        racoonImgCurrent = racoonImgLeft
                    print ("K_LEFT")
        
        #vászon kitörlése
        canvas.fill((0, 0, 0))

        #pihenő és célsorok rajzolása
        for i in range(11):
            canvas.blit(island, (i*100, 1*100), (0, 0, 100, 100)) #cel sor hatter
            canvas.blit(island, (i*100, 4*100), (0, 0, 100, 100)) #pihenosor hatter
            canvas.blit(island, (i*100, 7*100), (0, 0, 100, 100)) #start sor hatter

        #kocsisorok kirajzolása
        canvas.blit(lane1, (lane1index, 6*100))
        canvas.blit(lane1, (lane1index - (30 * 100), 6*100))
        canvas.blit(lane2, (lane2index, 5*100))
        canvas.blit(lane2, (lane2index + (30 * 100), 5*100))
        canvas.blit(lane3, (lane3index, 3*100))
        canvas.blit(lane3, (lane3index - (30 * 100), 3*100))
        canvas.blit(lane4, (lane4index, 2*100))
        canvas.blit(lane4, (lane4index + (30 * 100), 2*100))

        #mosómedve kirajzolása
        canvas.blit(racoonImgCurrent, (x * 100, y * 100))

        #eltelt idő kiszámítása, kiírása
        currentTime = time.time() - startTime
        timetext = font.render(str(int(currentTime)), True, (200,0,0))
        canvas.blit(timetext, (0,0))

        #vászon frissítés
        pygame.display.update()
    
        #várakozás
        clock.tick(60)

        #ütközés detektálás, ütközés esetén kezdőpontba helyezés+idő nullázás
        if y == 6:
            for i in [0, 5, 9, 14, 21, 24, 27]:
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane1index + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane1index - (30 * 100) + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
        
        if y == 5:
            for i in [0, 3, 7, 13, 16, 20, 26]:
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane2index + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane2index + (30 * 100) + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
        
        if y == 3:
            for i in [0, 5, 9, 14, 22, 27]:
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane3index + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane3index - (30 * 100) + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
        
        if y == 2:
            for i in [0, 3, 8, 13, 16, 21, 26]:
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane4index + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
                if pygame.Rect(x*100, 0, 100, 100).colliderect(pygame.Rect(lane4index + (30 * 100) + (i * 100), 0, 200, 100)):
                    x = 5
                    y = 7
                    startTime = time.time()
        
        #célbaérés ellenőrzése
        if y == 1:

            #győzelmi felirat
            won_text = font.render('You Won!', True, (200,0,0))
            canvas.blit(won_text, (450,0)) 
            pygame.display.update()

            #várakozás a kilépésre
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

        #kocsisorok mozgatása
        lane1index = lane1index+5
        if lane1index > (30 * 100):
            lane1index = 0

        lane2index = lane2index-6
        if lane2index < (-30 * 100):
            lane2index = 0

        lane3index = lane3index+7
        if lane3index > (30 * 100):
            lane3index = 0
        
        lane4index = lane4index-4
        if lane4index < (-30 * 100):
            lane4index = 0

    return

if __name__ == '__main__':
    main()
