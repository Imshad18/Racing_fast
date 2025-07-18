import pygame, sys
pygame.init()

pygame.display.set_caption('Racing Fast')
icon = pygame.image.load('files/car.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
og_car_image=pygame.transform.scale(pygame.image.load("files/car.png").convert_alpha(), (100,75))
track_image=pygame.image.load("files/track.png").convert_alpha()
cheqeured =pygame.transform.scale(pygame.image.load("files/chequered.PNG").convert_alpha(), (100,75))
start_stop = pygame.transform.rotate(cheqeured,90)
x,y = 100,100
speed = 5
car_image = og_car_image

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        car_image = pygame.transform.rotate(og_car_image, 45)
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        car_image = pygame.transform.rotate(og_car_image, 135)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        car_image = pygame.transform.rotate(og_car_image, 225)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        car_image = pygame.transform.rotate(og_car_image, 315)
    elif keys[pygame.K_UP]:
        car_image = pygame.transform.rotate(og_car_image, 90)
    elif keys[pygame.K_RIGHT]:
        car_image = pygame.transform.rotate(og_car_image, 0)
    elif keys[pygame.K_DOWN]:
        car_image = pygame.transform.rotate(og_car_image, 270)
    elif keys[pygame.K_LEFT]:
        car_image = pygame.transform.rotate(og_car_image, 180)







    screen.fill((34, 139, 34))
    screen.blit(track_image, (0, -250))
    screen.blit(start_stop, (600,610))
    screen.blit(car_image, (x, y))


    pygame.display.flip()
    clock.tick(60)  # 60 FPS
