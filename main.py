import pygame
import random

pygame.init()

# الشاشة
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

# ألوان
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
gray = (100,100,100)

# اللاعب
player = pygame.Rect(180, 500, 40, 60)

# أزرار
left_btn = pygame.Rect(50, 520, 100, 60)
right_btn = pygame.Rect(250, 520, 100, 60)

# سيارات
cars = []
speed = 5

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 👆 الضغط على الأزرار
        if event.type == pygame.MOUSEBUTTONDOWN:
            if left_btn.collidepoint(event.pos):
                player.x -= 30
            if right_btn.collidepoint(event.pos):
                player.x += 30

    # حدود الحركة
    if player.x < 0:
        player.x = 0
    if player.x > width - 40:
        player.x = width - 40

    # إنشاء سيارات
    if random.randint(1, 20) == 1:
        cars.append(pygame.Rect(random.randint(0, 360), -60, 40, 60))

    # تحريك السيارات
    for car in cars:
        car.y += speed

        if car.colliderect(player):
            print("💥 GAME OVER")
            running = False

    cars = [c for c in cars if c.y < height]

    # رسم اللاعب
    pygame.draw.rect(screen, blue, player)

    # رسم السيارات
    for car in cars:
        pygame.draw.rect(screen, red, car)

    # رسم الأزرار
    pygame.draw.rect(screen, gray, left_btn)
    pygame.draw.rect(screen, gray, right_btn)

    # كتابة النص
    font = pygame.font.SysFont(None, 30)
    screen.blit(font.render("LEFT", True, white), (75, 540))
    screen.blit(font.render("RIGHT", True, white), (265, 540))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
