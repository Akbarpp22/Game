import pygame

from gambar_mainan import *

class Button: 
    def __init__(self, x , y ,image , scale):
        """
        Inisialisasi objek Button dengan posisi, gambar, dan skala yang ditentukan.

        Args:
        - x (int): Koordinat x untuk posisi button.
        - y (int): Koordinat y untuk posisi button.
        - image (Surface): Gambar button yang akan ditampilkan.
        - scale (float): Skala perubahan ukuran gambar button.

        Attributes:
        - __width (int): Lebar gambar button.
        - __height (int): Tinggi gambar button.
        - __x (int): Koordinat x saat ini button.
        - __y (int): Koordinat y saat ini button.
        - __x_s (int): Koordinat x awal button.
        - __y_s (int): Koordinat y awal button.
        - image (Surface): Gambar button setelah diubah ukurannya.
        - rect (Rect): Kotak pembatas gambar button.
        - clicked (bool): Status klik button.
        - __count (int): Hitungan untuk efek animasi button.
        """
        self.__width = image.get_width()
        self.__height = image.get_height()
        self.__x = x
        self.__y = y
        self.__x_s = x
        self.__y_s = y
        self.image = pygame.transform.scale(image, (int(self.__width * scale) , int(self.__height * scale)))
        self.rect = self.image.get_rect(center=(self.__x, self.__y))
        self.clicked = False
        self.__count=0

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.__count<3:
                self.__x+=1
                self.__y+=1
                self.rect = self.image.get_rect(center=(self.__x, self.__y))
                self.__count+=1
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.__x = self.__x_s
            self.__y = self.__y_s
            self.rect = self.image.get_rect(center=(self.__x_s, self.__y_s))
            self.__count = 0

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image,(self.rect.x , self.rect.y))
        return action


#Tombol Start
button_start = pygame.image.load('Gambarrr/Background/button_start.png')
start_button = Button(750,450,button_start,0.8)

#Tombol How to play
how_to = pygame.image.load('Gambarrr/Background/howtoplay_button.png')
button_how_to = Button(750,530,how_to,0.15)

#Tombol Credits
credits = pygame.image.load('Gambarrr/Background/CREDITS.png')
button_credits = Button(750,610,credits,0.18)

#Tombol Exit
button_end = pygame.image.load('Gambarrr/Background/exitt.png')
end_button = Button(750,690,button_end,0.8)


#PILIHAN KETIKA GAME OVER
#Tombol Play Again
gameover_button = pygame.image.load('Gambarrr/Background/PlayAgain.png')
button_gameover = Button(750,600,gameover_button,0.18)
gameover_button_ptero = pygame.image.load('Gambarrr/Background/PlayAgain_night.png')
button_gameover_ptero = Button(750,600,gameover_button_ptero,0.18)

#Tombol Exit
gameover_button_exit = pygame.image.load('Gambarrr/Background/button_exit.png')
button_gameover_exit = Button(750,680,gameover_button_exit,0.18)
gameover_button_exit_ptero = pygame.image.load('Gambarrr/Background/button_exit_night.png')
button_gameover_exit_ptero = Button(750,680,gameover_button_exit_ptero,0.18)

#Gambar Ptero mati
gameover_ptero = pygame.image.load ('Gambarrr/Background/GAME OVER.png')
gameover_ptero = pygame.transform.scale(gameover_ptero,(width,height))