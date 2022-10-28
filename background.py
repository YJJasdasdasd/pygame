from unittest import runner
import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_widht = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_widht, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 이벤트 루프
running = True  # 게임이 진행중인
while running:
    pass
# pygame exit
pygame.quit()
