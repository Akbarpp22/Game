import pygame

#Ukuran Window
screen_info = pygame.display.Info()
width, height = 1550,820

#Buat window dengan ukuran layar saat ini
screen = pygame.display.set_mode((width,height))

#Ukuran Font
font = pygame.font.Font('freesansbold.ttf',20)

#Judul Window
pygame.display.set_caption ("Pterodactyl")

#Icon Window
icon = pygame.image.load ('Gambarrr/pterodactyl.png')
pygame.display.set_icon(icon)


#Background Ptero
background_ptero = pygame.image.load('Gambarrr/FinalNight.png')
background_ptero = pygame.transform.scale(background_ptero,(width,height))


#Background How to Play
background_how_to = pygame.image.load('Gambarrr/howtoplay1.png')
background_how_to = pygame.transform.scale(background_how_to,(width,height))

#Background Credits
background_credits = pygame.image.load('Gambarrr/Background/credits_bg.png')
background_credits = pygame.transform.scale(background_credits,(width,height))

#Gambar Karakter
Gambar_Ptero = [pygame.image.load(f'Gambarrr/Ptero/pterodactyl{i+1}.png') for i in range (0,8) ]

#Gambar Obstacle Ptero
pipa = pygame.image.load('Gambarrr/Pipa/pipa 1.png')
pipa = pygame.transform.flip(pipa, False, True)
pipaatas = pygame.image.load('Gambarrr/Pipa/pipa 2.png')
pipa = pygame.transform.scale(pipa, (80, 380))
pipaatas = pygame.transform.scale(pipaatas, (110, 380))


#Background Menu Game
background_menu = pygame.image.load('Gambarrr/menu_start.png')
background_menu = pygame.transform.scale(background_menu,(width,height)) 



