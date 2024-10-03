import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Частота обновления экрана
clock = pygame.time.Clock()

# Параметры птицы
bird_radius = 20
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Параметры труб
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
pipes = []

# Счет
score = 0
font = pygame.font.Font(None, 36)

# Состояние игры
game_over = False

# Функция для создания труб
def create_pipe():
    pipe_height = random.randint(100, 400)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)
    return top_pipe, bottom_pipe

# Функция для перезапуска игры
def restart_game():
    global bird_y, bird_velocity, pipes, score, game_over
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    pipes = []
    score = 0
    game_over = False

# Основной цикл игры
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = jump_strength
            elif event.key == pygame.K_r and game_over:
                restart_game()

    if not game_over:
        # Обновление позиции птицы
        bird_velocity += gravity
        bird_y += bird_velocity

        # Проверка столкновения с землей
        if bird_y + bird_radius > SCREEN_HEIGHT:
            bird_y = SCREEN_HEIGHT - bird_radius
            bird_velocity = 0
            game_over = True

        # Проверка столкновения с потолком
        if bird_y - bird_radius < 0:
            bird_y = bird_radius
            bird_velocity = 0

        # Создание новых труб
        if len(pipes) == 0 or pipes[-1][0].x < SCREEN_WIDTH - 200:
            pipes.append(create_pipe())

        # Обновление позиций труб
        for pipe in pipes:
            pipe[0].x -= pipe_speed
            pipe[1].x -= pipe_speed

            # Проверка столкновения с трубами
            if (bird_x + bird_radius > pipe[0].x and bird_x - bird_radius < pipe[0].x + pipe_width and
                (bird_y - bird_radius < pipe[0].height or bird_y + bird_radius > pipe[0].height + pipe_gap)):
                game_over = True

            # Удаление труб, которые вышли за пределы экрана
            if pipe[0].x + pipe_width < 0:
                pipes.remove(pipe)
                score += 1

    # Отрисовка птицы
    pygame.draw.circle(screen, BLACK, (bird_x, int(bird_y)), bird_radius)

    # Отрисовка труб
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe[0])
        pygame.draw.rect(screen, GREEN, pipe[1])

    # Отрисовка счета
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if game_over:
        # Отрисовка сообщения о проигрыше
        game_over_text = font.render("Game Over", True, BLACK)
        restart_text = font.render("Press 'R' to Restart", True, BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 50))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(30)

pygame.quit()