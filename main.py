# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import os


WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galaxy')

FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (155, 155, 255)
BORDER = pygame.Rect((WIDTH // 2 - 5, 0), (10, HEIGHT))

BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
RED_SPACESHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'spaceship_red.png')), 90)
YELLOW_SPACESHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')), 270)


# RED_HIT = pygame.USEREVENT + 1
# YELLOW_HIT = pygame.USEREVENT + 2

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 55
        self.height = 40
        self.vel = 5
        self.bullet_vel = 7
        self.bullet_max = 7


class Player1(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y)
        self.img = RED_SPACESHIP_IMG
        self.health = health
        self.bullets = []
        self.bullet = pygame.Rect((self.x + self.width, self.height // 2 - 2), (10, 5))

    def scale(self):
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        return self.img

    def draw(self, window):
        Player1.scale(self)
        window.blit(self.img, (self.x, self.y))

        for self.bullet in self.bullets:
            pygame.draw.rect(window, RED, self.bullet)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.y - self.vel > 0:  # Up
            self.y -= self.vel
        if key[pygame.K_s] and self.y + self.vel + self.height < HEIGHT:  # Down
            self.y += self.vel
        if key[pygame.K_a] and self.x - self.vel > 0:  # Left
            self.x -= self.vel
        if key[pygame.K_d] and self.x + self.vel + self.width < BORDER.x:  # Right
            self.x += self.vel

    def add_bullet(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.bullets.append(self.bullet)
            print('working')


class Player2(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y)
        self.img = YELLOW_SPACESHIP_IMG
        self.health = health

    def scale(self):
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        return self.img

    def draw(self, window):
        Player2.scale(self)
        window.blit(self.img, (self.x, self.y))

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.y - self.vel > 0:  # Up
            self.y -= self.vel
        if key[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT:  # Down
            self.y += self.vel
        if key[pygame.K_LEFT] and self.x - self.vel > BORDER.x + BORDER.width:  # Left
            self.x -= self.vel
        if key[pygame.K_RIGHT] and self.x + self.vel + self.width < WIDTH:  # Right
            self.x += self.vel


class Galaxy:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.border = BORDER

    def draw(self, window):
        WIN.blit(self.img, (self.x, self.y))
        pygame.draw.rect(window, BLUE, self.border)


def main():
    run = True
    clock = pygame.time.Clock()

    galaxy = Galaxy(0, 0, BG)
    player1 = Player1(100, 100)
    player2 = Player2(WIDTH // 2 + 100, 100)

    def redraw_window():
        WIN.fill(WHITE)
        galaxy.draw(WIN)
        player1.draw(WIN)
        player2.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.add_bullet()
        player1.move()
        player2.move()
        redraw_window()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
