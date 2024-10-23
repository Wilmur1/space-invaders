import pygame
import sys
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("screen")

yellow_rect = pygame.Rect(50,350,70,70)
#pygame.draw.rect(screen,"blue",yellow_rect)


bg = pygame.image.load("space invaders/images space invaders/space background.png")
resize_bg = pygame.transform.scale(bg,(1520,780))
yellow_spaceship = pygame.image.load("space invaders\images space invaders\spceship yellow.png")
rotate = pygame.transform.rotate(yellow_spaceship,90)
resize_yellow_spaceship = pygame.transform.scale(rotate,(70,70))
def draw():
     screen.blit(resize_bg,(0,0))
     screen.blit(resize_yellow_spaceship,(yellow_rect.x,yellow_rect.y))
     
def movement_yellow():
     keys = pygame.key.get_pressed()
     if keys[pygame.K_w]:
          yellow_rect.y = yellow_rect.y - 3
     if keys[pygame.K_a]:
          yellow_rect.x = yellow_rect.x - 3
     if keys[pygame.K_s]:
          yellow_rect.y = yellow_rect.y + 3
     if keys[pygame.K_d]:
          yellow_rect.x = yellow_rect.x + 3






while True:
     draw()
     movement_yellow()
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()