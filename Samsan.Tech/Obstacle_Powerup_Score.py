import pygame
import random

from abc import ABC, abstractmethod
from gambar_mainan   import *
from tombol_mainan   import *
from karakter_mainan import *
from gambar_mainan   import *

class Rintangan(ABC):
    @abstractmethod
    def update(self):
        """
        Metode abstrak untuk memperbarui posisi rintangan.
        """
        self.rect.x -= speed
        if self.rect.x <-self.rect.width:
            obstacles.pop()

    @abstractmethod
    def draw(self, screen):
        """
        Metode abstrak untuk menggambar rintangan pada layar.
        """
        screen.blit(self.image, self.rect)

    @abstractmethod
    def buat_rintangan(self):
        """
        Metode abstrak untuk membuat rintangan.
        """
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player.ptero_rect.colliderect(rintangan.rect):
                dead_sound = pygame.mixer.Sound('Music/Mati.ogg') 
                dead_sound.play()
                start_ptero(Score.hitung_score(self))


class ObstaclePipa (Rintangan):
    def update(self):
        """
        Memperbarui posisi rintangan Pipa.
        """
        self.rect.x -= speed

    def ganti_rintangan(self):
            """
            Mengganti jenis rintangan Pipa berdasarkan skor.
            """
            x = random.randint(300 , 600)
            pipaa = pygame.transform.scale(pipa, (80, 880 - x - 170))
            pipaatass = pygame.transform.scale(pipaatas, (110, x))
            if poin % 50 == 0 and poin < 1000:
                obstacles.append(Pipa(pipaa,1))
                obstacles.append(Pipa(pipaatass,-1))
            if poin > 1000 and poin < 2000: 
                if poin % 40== 0:
                    obstacles.append(Pipa(pipaa,1))
                    obstacles.append(Pipa(pipaatass,-1))
            if poin > 2000 and poin < 3000:
                if poin % 30 == 0:
                    obstacles.append(Pipa(pipaa,1))
                    obstacles.append(Pipa(pipaatass,-1))
            
    
    def buat_rintangan(self):
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player.ptero_rect.colliderect(rintangan.rect):
                dead_sound = pygame.mixer.Sound('Music/Mati.ogg') 
                dead_sound.play()
                start_ptero(Score._hitung_score(self))

    def draw(self, screen):
        """
        Menggambar rintangan Pipa pada layar.
        """
        screen.blit(self.image, self.rect)

class Pipa(ObstaclePipa):
    def __init__(self,image,posisi):
        """
        Inisialisasi rintangan Pipa.
        """
        self.image = image
        self.x = 1580
        self.y = 950
        self.rect = self.image.get_rect()
        if posisi == 1: 
            self.rect.bottomleft = (self.x+35,self.y)
        if posisi == -1:
            self.rect.topleft = (self.x,0)

class Score:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    def _hitung_score(self):
        """
        Menghitung skor dan memperbarui kecepatan permainan.
        """
        global poin, speed
        poin += 1
        if poin % 150 == 0:
            speed += 0.5

        text = font.render("Score: " + str(poin), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (800, 100)
        screen.blit(text, textRect)
        self._score = poin

        return poin

    @staticmethod
    def high_score():
        """
        Mengembalikan skor tertinggi yang tersimpan.
        """
        high_score = 0
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        return high_score

    @staticmethod
    def save_high_score(new_high_score):
        """
        Menyimpan skor tertinggi baru ke dalam file.
        """
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()


def how_to_play():
    """
    Menampilkan tampilan panduan bermain.
    """
    running = True
    while running: 
        screen.fill((255,255,255))
        screen.blit(background_how_to,(0,0))

        if end_button.draw():
            start(0)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

def credits():
    """
    Menampilkan tampilan kredit.
    """
    running = True
    while running: 
        screen.fill((255,255,255))
        screen.blit(background_credits,(0,0))

        if end_button.draw():
            start(0)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
   

def start_ptero(nilai):
    """
    Menampilkan tampilan game over dan memulai permainan baru.
    """
    running = True
    while running:  
        screen.fill((255,255,255))
        screen.blit(gameover_ptero,(0,0))
        if button_gameover_ptero.draw():
            karakter()
        if button_gameover_exit_ptero.draw():
            running = False
            pygame.quit()
            exit()
        score = font.render("Your Score: " + str(nilai), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (750, 250+ 20)
        screen.blit(score, scoreRect)
        high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
        high_scoreRect = high_score.get_rect()
        high_scoreRect.center = (750, 250 )
        screen.blit(high_score, high_scoreRect)
        if nilai >Score.high_score():
            Score.save_high_score(nilai)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

def karakter():
        
        pygame.mixer.music.load('Music/Background.ogg') 
        pygame.mixer.music.play(-1)
        game_ptero()
        
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        

TERBANG = False
game_over = False

def game_ptero ():
    """
    Fungsi utama permainan Ptero.
    """
    global TERBANG, poin ,speed,game_over,pipa,obstacles,player,pipaatas
    game_over = False
    running = True
    speed = 8
    poin = 0
    score = Score()
    clock = pygame.time.Clock()
    obstacles = []
    i = 0
    width = 1550
    height = 820
    player = Ptero()
    obstacle = ObstaclePipa()
    pygame.display.set_mode((width,height))

    while running: 
        if game_over == False: 
            user_input = pygame.key.get_pressed()
            screen.fill((255,255,255))
            screen.blit(background_ptero, (i,0))
            screen.blit(background_ptero, (width+i,0))
            if i <= -width:
                screen.blit(background_ptero, (width+i,0))
                i = 0
            i -= speed

            player.draw(screen)
            obstacle.ganti_rintangan()
            obstacle.buat_rintangan()
            user_input = pygame.key.get_pressed()
            player.update(user_input)
            
            if player.rect.bottom > 820:
                game_over = True
                TERBANG = False

            score._hitung_score()
            clock.tick(30)
            pygame.display.update()
            
        else: 
            start(0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and TERBANG == False and game_over == False:
                TERBANG = True

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

def start (nilai):
    pygame.mixer.music.load('Music/Menu.ogg') 
    pygame.mixer.music.play()
    if nilai == 0: 
        running = True
        while running: 
           # pygame.display.set_mode((950,836))
            screen.fill((255,255,255))
            screen.blit(background_menu,(0,0))
            if start_button.draw():
                karakter()
            if button_how_to.draw():
                how_to_play()
            if button_credits.draw():
                credits()
            if end_button.draw():
                running = False
                pygame.quit()
                exit()
            high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
            high_scoreRect = high_score.get_rect()
            high_scoreRect.center = (750, height // 2 - 50)
            screen.blit(high_score, high_scoreRect)
            if nilai >Score.high_score():
                Score.save_high_score(nilai)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()


    else: 
        running = True
        while running: 
           # pygame.display.set_mode((950,836))
            screen.blit(gameover_ptero,(0,0))
            if button_gameover.draw():
                karakter()
            
            if button_gameover_exit.draw():
                running = False
                pygame.quit()
                exit()
            score = font.render("Your Score: " + str(nilai), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (470, 250+ 20)
            screen.blit(score, scoreRect)
            high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
            high_scoreRect = high_score.get_rect()
            high_scoreRect.center = (470, 250 )
            screen.blit(high_score, high_scoreRect)
            if nilai >Score.high_score():
                Score.save_high_score(nilai)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()