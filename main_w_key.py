import pygame, sys
pygame.init()

pygame.display.set_caption('Racing Fast')
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
og_car_image=pygame.transform.scale(pygame.image.load("car.png").convert_alpha(), (100,75))
track_image=pygame.image.load("track.png").convert_alpha()
cheqeured =pygame.transform.scale(pygame.image.load("chequered.PNG").convert_alpha(), (100,75))
start_stop = pygame.transform.rotate(cheqeured,90)
x,y = 100,100
speed = 5
last_angle = 0

car_image = og_car_image

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            car_image = pygame.transform.rotate(og_car_image, 45)
            y -= speed
            x += speed
            last_angle = 45

        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            car_image = pygame.transform.rotate(og_car_image, 135)
            y -= speed
            x -= speed
            last_angle = 135

        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            car_image = pygame.transform.rotate(og_car_image, 225)
            y += speed
            x -= speed
            last_angle = 225

        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            car_image = pygame.transform.rotate(og_car_image, 315)
            y += speed
            x += speed
            last_angle = 315

        elif keys[pygame.K_UP]:
            car_image = pygame.transform.rotate(og_car_image, 90)
            y -= speed
            last_angle = 90
        elif keys[pygame.K_RIGHT]:
            car_image = pygame.transform.rotate(og_car_image, 0)
            x += speed
            last_angle = 0
        elif keys[pygame.K_DOWN]:
            car_image = pygame.transform.rotate(og_car_image, 270)
            y += speed
            last_angle = 270
        elif keys[pygame.K_LEFT]:
            car_image = pygame.transform.rotate(og_car_image, 180)
            x -= speed
            last_angle = 180

        else:
            if last_angle == 0:
                x += speed
            if last_angle == 45:
                y -= speed
                x += speed

            if last_angle == 90:
                y -= speed
            if last_angle == 135:
                y -= speed
                x -= speed
            if last_angle == 180:
                x -= speed
            if last_angle == 225:
                y += speed
                x -= speed
            if last_angle == 270:
                y += speed
            if last_angle == 315:
                y += speed
                x += speed




    screen.fill((34,139,34))
    screen.blit(track_image, (0, -250))
    screen.blit(start_stop, (600,610))
    screen.blit(car_image, (x, y))


    pygame.display.flip()
    clock.tick(60) 
