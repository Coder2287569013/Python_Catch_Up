import pygame 

pygame.init()
pygame.mixer.init()

w, h = 700, 500
sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("Catch-Up! v1.0")
clock = pygame.time.Clock()

fps = 60
game = True
pause = False
score_sprite1 = 0
score_sprite2 = 0

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (w, h))
sprite1_img = pygame.image.load("sprite1.png")
sprite2_img = pygame.image.load("sprite2.png")

pygame.mixer.music.load("Sound_07177.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

font = pygame.font.SysFont("Arial", 48)
score1 = font.render(str(score_sprite1), True, (0,0,192))
score2 = font.render(str(score_sprite2), True, (180, 0, 72))

start = pygame.time.get_ticks()

class Sprite:
    def __init__(self, x, y, w, h, image, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.speed = speed
        self.hunter = False
    def move(self, left, right, up, down):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[left] and self.rect.x >= 0: self.rect.x -= 5
        if key_pressed[right] and self.rect.x <= 600: self.rect.x += 5
        if key_pressed[up] and self.rect.y >= 0: self.rect.y -= 5
        if key_pressed[down] and self.rect.y <= 400: self.rect.y += 5
    def set_hunter(self):
        self.hunter = True
    def draw(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))

sprite1 = Sprite(150, 350, 100, 100, sprite1_img, 5)
sprite2 = Sprite(550, 350, 100, 100, sprite2_img, 5)
sprite1.set_hunter()

while game:
    seconds = int((pygame.time.get_ticks()-start)/1000)
    timer = font.render(str(seconds), True, (0,0,0))

    sc.blit(background, (0,0))
    sprite1.draw()
    sprite2.draw()
    sc.blit(score1, (150, 15))
    sc.blit(score2, (550, 15))
    sc.blit(timer, (340, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and pause == False:
                pause = True
            elif event.key == pygame.K_ESCAPE and pause == True:
                pause = False

    sprite1.move(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    sprite2.move(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

    if sprite1.rect.colliderect(sprite2.rect) and sprite1.hunter:
        start = pygame.time.get_ticks()
        seconds = int((pygame.time.get_ticks()-start)/1000)
        timer = font.render(str(seconds), True, (0,0,0))
        sc.blit(timer, (340, 15))
        score_sprite1 += 1
        score1 = font.render(str(score_sprite1), True, (0,0,192))
        sc.blit(score1, (150, 15))
        sprite1.rect.x, sprite1.rect.y = 150, 350
        sprite2.rect.x, sprite2.rect.y = 550, 350
        sprite1.hunter = False
        sprite2.set_hunter()
    if sprite2.rect.colliderect(sprite1.rect) and sprite2.hunter:
        start = pygame.time.get_ticks()
        seconds = int((pygame.time.get_ticks()-start)/1000)
        timer = font.render(str(seconds), True, (0,0,0))
        sc.blit(timer, (340, 15))
        score_sprite2 += 1
        score2 = font.render(str(score_sprite2), True, (180,0,72))
        sc.blit(score2, (550, 15))
        sprite1.rect.x, sprite1.rect.y = 150, 350
        sprite2.rect.x, sprite2.rect.y = 550, 350
        sprite1.set_hunter()
        sprite2.hunter = False
    if sprite1.hunter and seconds >= 10:
        start = pygame.time.get_ticks()
        seconds = int((pygame.time.get_ticks()-start)/1000)
        timer = font.render(str(seconds), True, (0,0,0))
        sc.blit(timer, (340, 15))
        score_sprite2 += 1
        score2 = font.render(str(score_sprite2), True, (180,0,72))
        sc.blit(score2, (550, 15))
        sprite1.rect.x, sprite1.rect.y = 150, 350
        sprite2.rect.x, sprite2.rect.y = 550, 350
        sprite1.hunter = False
        sprite2.set_hunter()
    if sprite2.hunter and seconds >= 10:
        start = pygame.time.get_ticks()
        seconds = int((pygame.time.get_ticks()-start)/1000)
        timer = font.render(str(seconds), True, (0,0,0))
        sc.blit(timer, (340, 15))
        score_sprite1 += 1
        score1 = font.render(str(score_sprite1), True, (0,0,192))
        sc.blit(score1, (150, 15))
        sprite1.rect.x, sprite1.rect.y = 150, 350
        sprite2.rect.x, sprite2.rect.y = 550, 350
        sprite1.set_hunter()
        sprite2.hunter = False

    pygame.display.update()
    clock.tick(fps)