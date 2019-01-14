import pygame

pygame.init()

pygame.display.set_mode((800,10))
#pygame.quit()
#quit()
false = False
while not false:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            false = True
        #print(event)

pygame.quit()
quit()
