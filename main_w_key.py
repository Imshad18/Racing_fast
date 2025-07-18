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

start_stop_rect=start_stop.get_rect(topleft=(600,610))

x,y = 100,100
speed = 5
last_angle = 0
car_image = og_car_image

font = pygame.font.SysFont(None, 36)
lap_time =0
start_time = None
lap_started =False
car_on_line = False

time_surface = font.render(f"Lap Time: {lap_time}s", True, (255, 255, 255))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            y -= speed
            x += speed
            car_image = pygame.transform.rotate(og_car_image, 45)
            last_angle = 45
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            y -= speed
            x -= speed
            car_image = pygame.transform.rotate(og_car_image, 135)
            last_angle = 135
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            y += speed
            x -= speed
            car_image = pygame.transform.rotate(og_car_image, 225)
            last_angle = 225
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            y += speed
            x += speed
            car_image = pygame.transform.rotate(og_car_image, 315)
            last_angle = 315
        elif keys[pygame.K_UP]:
            y -= speed
            car_image = pygame.transform.rotate(og_car_image, 90)
            last_angle = 90
        elif keys[pygame.K_RIGHT]:
            x += speed
            car_image = pygame.transform.rotate(og_car_image, 0)
            last_angle = 0
        elif keys[pygame.K_DOWN]:
            y += speed
            car_image = pygame.transform.rotate(og_car_image, 270)
            last_angle = 270
        elif keys[pygame.K_LEFT]:
            x -= speed
            car_image = pygame.transform.rotate(og_car_image, 180)
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
    car_rect=car_image.get_rect(topleft=(x,y))
    if start_time is None:
        start_time = pygame.time.get_ticks()
        lap_started = True
        last_lap_time = 0  # Initialize last lap time
        last_lap_surface = font.render(f"Last Lap: {last_lap_time}s", True, (255, 255, 255))
    if car_rect.colliderect(start_stop_rect) and not car_on_line:
        car_on_line = True
        if lap_started:
            now = pygame.time.get_ticks()
            last_lap_time = lap_time  # Store current lap time as last
            lap_time = round((now - start_time) / 1000, 2)
            time_surface = font.render(f"Lap Time: {lap_time}s", True, (255, 255, 255))
            last_lap_surface = font.render(f"Last Lap: {last_lap_time}s", True, (255, 255, 255))
            start_time = now
            lap_started = True
    elif not car_rect.colliderect(start_stop_rect):
        car_on_line = False
    if lap_started:
        now = pygame.time.get_ticks()
        lap_time = round((now - start_time) / 1000, 2)
        time_surface = font.render(f"Lap Time: {lap_time}s", True, (255, 255, 255))

    screen.blit(car_image, (x,y))
    screen.blit(time_surface, (20, 20))
    screen.blit(last_lap_surface, (20, 50))


    pygame.display.flip()
    clock.tick(60)
