import pygame

#STEP UTAMA
#init
#user input, atau databaseinput
#update asset
#render ke display

#init
pygame.init()
isRun = True

window_lebar = 500
window_panjang = 500

#membuat display untuk surface object
window = pygame.display.set_mode((window_lebar,window_panjang))

#object game
#posisi
x = 250
y = 250

#ukuran
panjang = 20
lebar = 20

#kecepatan
speed = 0.05


while isRun:
    #user input, atau databaseinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    #keyboard action
    keys = pygame.key.get_pressed()

    # menggerakan ke kiri
    if keys [pygame.K_LEFT] and x > 0:
        x -= speed
    
    #menggerakan ke kanan
    if keys [pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    
    #menggerakan ke bawah
    if keys [pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed

     #menggerakan ke atas
    if keys [pygame.K_UP] and y > 0:
        y -= speed


    #update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))

    #render ke display
    pygame.display.update()

pygame.quit()