import pygame

pygame.init() # 초기화 하는 것 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Sophie Game")# 게임 이름


# 배경이미지 불러오기
background = pygame.image.load("C:/Users/ricar/Desktop/PYTHONWORKSPACE/pygame_basic.py/background.png")



# 이벤트 루프

running = True # 게임이 진행중인가를 체크
while running :
    for event in pygame.event.get(): # 파이게임 실행시 무조건 있어야하는 코드  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT : # 창의 맨위의 X를 눌러서 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.
   

    screen.blit(background, (0,0)) # 왼쪽 맨위 x = 1, y =0 # 배경 그리기
    # screen.fill((0,0,255)) # R, G , B - 단순히 색만 채울때 이 경우 파란색임

    pygame.display.update() # 게임화면을 다시 그리기 ! 반드시 있어야함

# pygame 종료
pygame.quit()