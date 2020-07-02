# Quiz ) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x  좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70*70 - character.png
# 3. 똥 : 70*70 - enemy.png
import random
import pygame
#####################################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()  # 초기화 하는 것 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz_1")  # 게임 이름

# FPS
clock = pygame.time.Clock()
#####################################################################
# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도,폰트 등을 설정)

# 배경만들기
background = pygame.image.load("C:\\Users\\ricar\\Desktop\\PYTHONWORKSPACE\\pygame_basic.py\\background_1.png")

# 캐릭터 만들기
character = pygame.image.load("C:\\Users\\ricar\\Desktop\\PYTHONWORKSPACE\pygame_basic.py\\character_1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) # 스크린 중앙
character_y_pos = screen_height - character_height

#캐릭터 이동 위치
to_x = 0 # 캐릭터를 움직이기 위해
character_speed = 10

# 똥 만들기 
ddong = pygame.image.load("C:\\Users\\ricar\\Desktop\\PYTHONWORKSPACE\\pygame_basic.py\\ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width) # 0부터 화면 끝에서 똥의 사이즈를 뺀데까지..어쨋든 화면 끝까지 랜덤

ddong_y_pos = 0  # 위에서 떨어지는 거니까 0이 맞음
ddong_speed = 10



running = True  
while running:
    dt = clock.tick(30) # dt = delta # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 파이게임 실행시 무조건 있어야하는 코드  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창의 맨위의 X를 눌러서 창이 닫히는 이벤트가 발생하였는가?
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
        # 캐릭터가 화면 밖으로 나가지 않도록 경계값 처리하기
    if character_x_pos <0 : # 캐릭터가 왼쪽 밖으로 나가지 않도록 정의함
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 캐릭터가 오른쪽 밖으로 나가지 않도록 정의함
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed
    
    if ddong_y_pos > screen_height : 
        ddong_y_pos = 0  # ddong을 다시 맨 위에서 불러내게끔 함.
        ddong_x_pos = random.randint(0, screen_width - ddong_width)


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos, character_y_pos))    
    screen.blit(ddong, (ddong_x_pos,ddong_y_pos))
    pygame.display.update()  # 게임화면을 다시 그리기 ! 반드시 있어야함

pygame.quit()
