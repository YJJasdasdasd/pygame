import pygame  # 1. pygame 선언
import random
import os

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
white = (255, 255, 255)
BLACK = (0, 0, 0)
size = [1100, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)

# 타이머
total_time = 1
start_ticks = pygame.time.get_ticks()


def runGame():
    # 폭탄 이미지 불러오기 and 폭탄 리스트 생성
    bomb_image = pygame.image.load('bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (50, 50))
    bombs = []
    # 코인 이미지 불러오기 and 코인 리스트 생성
    coin1_image = pygame.image.load('coin1_.png')
    coin1_image = pygame.transform.scale(coin1_image, (50, 50))
    coins1 = []
    coin2_image = pygame.image.load('coin2_.png')
    coin2_image = pygame.transform.scale(coin2_image, (50, 50))
    coins2 = []
    coin3_image = pygame.image.load('coin3_.png')
    coin3_image = pygame.transform.scale(coin3_image, (50, 50))
    coins3 = []
    # 초기 라이프 설정
    total_life = 3

    # 폭탄 개수 발생.
    for i in range(3):
        rect = pygame.Rect(bomb_image.get_rect())
        rect.left = random.randint(0, size[0]-500-29)
        rect.top = -100
        # 속도 증가
        dy = random.randint(3, 9)
        bombs.append({'rect': rect, 'dy': dy})

    # 코인 개수 발생
    for i in range(5):
        rect_c1 = pygame.Rect(coin1_image.get_rect())
        rect_c1.left = random.randint(0, size[0]-500-69)
        rect_c1.top = -100
        dy_c1 = random.randint(3, 9)
        coins1.append({'rect': rect_c1, 'dy': dy_c1})

    person_image = pygame.image.load('mario_small.png')
    person_image = pygame.transform.scale(person_image, (100, 100))
    person = pygame.Rect(person_image.get_rect())
    person.left = (size[0]-500) // 2 - person.width // 2
    person.top = size[1] - person.height
    person_dx = 0
    person_dy = 0

    global done
    while not done:

        # 사과 이미지 띄우기
        heart_image = pygame.image.load('heart{0}.png'.format(total_life))
        heart_image = pygame.transform.scale(heart_image, (80, 30))
        heart = pygame.Rect(heart_image.get_rect())

        clock.tick(30)
        screen.fill(white)
        # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        # 출력할 글자, True, 글자 색상
        timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))

        # 타이머 띄우기
        screen.blit(timer, (550, 10))
        # 사과 이미지 띄우기
        screen.blit(heart_image, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            # Keydown = 누르고 있을때 KeyUp 은 뗄때
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_dx = -20
                elif event.key == pygame.K_RIGHT:
                    person_dx = 20
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_dx = 0
                elif event.key == pygame.K_RIGHT:
                    person_dx = 0

        # 땅에 닿은 폭탄 제거
        for bomb in bombs:
            bomb['rect'].top += bomb['dy']
            if bomb['rect'].top > size[1]:
                bombs.remove(bomb)
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0, size[0]-500-29)
                rect.top = -100
                dy = random.randint(3, 9)
                bombs.append({'rect': rect, 'dy': dy})

        # 땅에 닿은 사과 제거
        for coin1 in coins1:
            coin1['rect'].top += coin1['dy']
            if coin1['rect'].top > size[1]:
                coins1.remove(coin1)
                rect_c1 = pygame.Rect(coin1_image.get_rect())
                rect_c1.left = random.randint(0, size[0]-500-69)
                rect_c1.top = -100
                dy_c1 = random.randint(3, 9)
                coins1.append({'rect': rect_c1, 'dy': dy_c1})

        person.left = person.left + person_dx

        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - 500 - person.width:
            person.left = size[0] - 500 - person.width

        screen.blit(person_image, person)

        # 폭탄이 닿았을때 이벤트 발생 , done = True가 되면 while not done 에서 while문 종료 즉 게임 종료
        for bomb in bombs:
            if bomb['rect'].colliderect(person) and total_life > 1:
                bombs.remove(bomb)
                total_life -= 1
            elif bomb['rect'].colliderect(person):
                done = True
            screen.blit(bomb_image, bomb['rect'])

        for coin1 in coins1:
            if coin1['rect'].colliderect(person):
                done = False
            screen.blit(coin1_image, coin1['rect'])

        pygame.display.update()


runGame()
pygame.quit()
