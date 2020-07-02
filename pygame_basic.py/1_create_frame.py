import pygame

pygame.init() # 초기화 하는 것 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Sophie Game")# 게임 이름

# 이벤트 루프

running = True # 게임이 진행중인가를 체크
while running :
    for event in pygame.event.get(): # 파이게임 실행시 무조건 있어야하는 코드  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT : # 창의 맨위의 X를 눌러서 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.

# pygame 종료
pygame.quit()