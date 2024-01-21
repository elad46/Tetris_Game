import pygame
import random

# אתחול Pygame
pygame.init()

# קביעת גדלים וצבעים
WIDTH, HEIGHT = 640, 480
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

# הגדרת חלון המשחק
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def show_text(message, color, font, size, position):
    font = pygame.font.SysFont(font, size)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    game_window.blit(text_surface, text_rect)

def choose_speed():
    speed_chosen = False
    snake_speed = 15  # מהירות ברירת מחדל
    while not speed_chosen:
        game_window.fill(BACKGROUND_COLOR)
        show_text("בחר מהירות: לחץ 1 לאט, 2 בינוני, 3 מהיר", WHITE, 'times new roman', 30, (WIDTH / 2, HEIGHT / 4))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_speed = 5
                    speed_chosen = True
                elif event.key == pygame.K_2:
                    snake_speed = 15
                    speed_chosen = True
                elif event.key == pygame.K_3:
                    snake_speed = 30
                    speed_chosen = True

        pygame.display.update()
    return snake_speed

snake_speed = choose_speed()

# הגדרת משתנים למשחק
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def show_score():
    score_font = pygame.font.SysFont('times new roman', 20)
    score_surface = score_font.render('Score : ' + str(score), True, WHITE)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WIDTH / 10, 15)
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, WHITE)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    game_window.fill(BACKGROUND_COLOR)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

# לולאת המשחק הראשית
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # עדכון הכיוון של הנחש
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # תנועת הנחש
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # עדכון הגוף של הנחש
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
        SNAKE_COLOR = get_random_color()
    else:
        snake_body.pop()

    # בדיקת התנגשות עם המזון
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    # בדיקת התנגשות עם עצמו או הקירות
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()

    # ציור הנחש והמזון
    game_window.fill(BACKGROUND_COLOR)
    for pos in snake_body:
        pygame.draw.rect(game_window, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # הצגת ניקוד
    show_score()

    # עדכון המסך ושליטה במהירות המשחק
    pygame.display.update()
    clock.tick(snake_speed)
