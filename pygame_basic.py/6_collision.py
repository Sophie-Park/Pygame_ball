import pygame

pygame.init()  # 초기화 하는 것 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Sophie Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/ricar/Desktop/PYTHONWORKSPACE/pygame_basic.py/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/ricar/Desktop/PYTHONWORKSPACE/pygame_basic.py/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴 # get_rect = method of a pygame / 사각형을 불러옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면가로의 절반크기에 해당하는 곳에 캐릭터 x 좌표 위치
character_y_pos = screen_height - character_height # 화면 세로크기의 가장 아래에 해당하는곳에 캐릭터 y좌표 위치

# 이동할 좌표

to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터 만들기
enemy = pygame.image.load("C:/Users/ricar/Desktop/PYTHONWORKSPACE/pygame_basic.py/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로크기
enemy_height = enemy_size[1]  # 캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면가로의 절반크기에 해당하는 곳에 캐릭터 x 좌표 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2) # 화면 세로크기의 가장 아래에 해당하는곳에 캐릭터 y좌표 위치

# 이벤트 루프

running = True  # 게임이 진행중인가를 체크
while running:
    dt = clock.tick(60) # dt = delta # 게임화면의 초당 프레임 수를 설정

# 캐릭터가 100 만큼 이동해야함.

# 10 fps : 1초동안에 10번 동작 - > 1번에 10만큼 이동 10*10 = 100
# 20 fps : 1초동안 20번 동작 -> 1번에 5만큼 이동 20*5 = 100

    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():  # 파이게임 실행시 무조건 있어야하는 코드  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창의 맨위의 X를 눌러서 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님.

        if event.type == pygame.KEYDOWN:  # 키가 눌러(down)졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릴터를 왼쪽으로
                to_x -= character_speed  # to_x  = to_x- 5
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed  # to_x = to_x+ 5
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키에서 손을 떼면(up) 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # 이동속도 보정 # 프레임이 바뀌어도 속도는 고정 #  프레임이 낮아지면 버벅이지만 속도는 유지
    character_y_pos += to_y * dt # 이동속도 보정 # 프레임이 바뀌어도 속도는 고정 # 프레임이 낮아지면 버벅이지만 속도는 유지

# 가로 경계값 처리
    if character_x_pos <0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

# 세로 경계값 처리
    if character_y_pos <0 : 
        character_y_pos = 0 
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

# 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

# 충돌 체크
    if character_rect.colliderect(enemy_rect): # colliderect - 이 사각형 기준으로 충돌이 있었는지 확인하는 함수
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))  # 왼쪽 맨위 x = 1, y =0 # 배경 그리기 # blit = draw ### blit the surface onto the canvas
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기 # 캐릭터의 바뀐 x y 좌표를 계속 업데이트
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update()  # 게임화면을 다시 그리기 ! 반드시 있어야함

# pygame 종료
pygame.quit()
