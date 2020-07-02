# print(abs(-5)) # 절대값 구하기
# print(pow(4,2)) # 4^2 = 4*4 = 16
# # # # # # print(max(5,12)) # 최대값 꺼내기 # 12
# # # # # # print(min(5,12)) # 최소값 꺼내기 # 5
# # # # # # print(round(3.14))# 반올림하기 # 3
# # # # # # print(round(4.99)) # 5
# # # # # # print()
# from math import *
# print(floor(4.89)) # 내림값 구하기 # 4
# print(ceil(3.89)) # 올림값 구하기 # 4
# print(sqrt(16))# 제곱근 값 구하기 # 4
# print()
# # # # # from random import *
# # # # # # print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
# # # # # # print(random()*10)# 0.0 이상 10.0 미만의 임의의 값 생성
# # # # # # print(int(random()*10))# 0.0 이상 10.0 미만의 임의의 값 생성(정수값 만)
# # # # # # print(int(random()*10))# 0.0 이상 10.0 미만의 임의의 값 생성(정수값 만)
# # # # # # print(int(random()*10))# 0.0 이상 10.0 미만의 임의의 값 생성(정수값 만)
# # # # # # print()
# # # # # # print(int(random()*10+1))# 1 이상 10.0 이하의 임의의 값 생성(정수값 만)
# # # # # # print(int(random()*10+1))# 1 이상 10.0 이하의 임의의 값 생성(정수값 만)
# # # # # # print(int(random()*10+1))# 1 이상 10.0 이하의 임의의 값 생성(정수값 만)
# # # # # # print(int(random()*10+1))# 1 이상 10.0 이하의 임의의 값 생성(정수값 만)
# # # # # # print(int(random()*10+1))# 1 이상 10.0 이하의 임의의 값 생성(정수값 만)
# # # # # # print()
# # # # # # print(int(random()*45+1))
# # # # # # print(int(random()*45+1))
# # # # # # print(int(random()*45+1))
# # # # # # print(int(random()*45+1))
# # # # # # print(int(random()*45+1))
# # # # # # print(int(random()*45+1))

# 로또번호 뽑기
# # # # # # print(randrange(1,46)) #1~46 미만의 임의 값 생성
# # # # # # print(randrange(1,46)) #1~46 미만의 임의 값 생성
# # # # # # print(randrange(1,46)) #1~46 미만의 임의 값 생성
# # # # # # print(randrange(1,46)) #1~46 미만의 임의 값 생성
# # # # # # print(randrange(1,46)) #1~46 미만의 임의 값 생성
# # # # # # print(randrange(1,46)) #1~46 미만의 임의 값 생성 

# # # # # print(randint(1,45)) # 1~45 이하의 임의 값 생성
# # # # # print(randint(1,45)) # 1~45 이하의 임의 값 생성
# # # # # print(randint(1,45)) # 1~45 이하의 임의 값 생성
# # # # # print(randint(1,45)) # 1~45 이하의 임의 값 생성
# # # # # print(randint(1,45)) # 1~45 이하의 임의 값 생성
# # # # # print(randint(1,45)) # 1~45 이하의 임의 값 생성
#(9) 문자열
# # # # # sentence = '나는 소년입니다'
# # # # # print(sentence)
# # # # # sentence2 = "파이썬은 쉬워요"
# # # # # print(sentence2)
# # # # # sentence3 = """
# # # # # 나는 소년이고,
# # # # # 파이썬은 쉬워요
# # # # # """
# # # # # print(sentence3)

#10 슬라이싱 - 필요한 정보만 잘라서 가져오기
# # # # # 슬라이싱 배우기
# # # # id = "990120-1234567"
# # # # print("성별 : "+ id[7])
# # # # print("연 : " + id[0:2])0번째부터 2번째 직전 값 까지, 2는 포함하지 않음
# # # # print("월 : "+ id[2:4])
# # # # print("일 : "+id[4:6])
# # # # print("생년월일 : "+id[:6]) # 0은 안적어도 됨. 처음부터 6 직전까지의 값을 불러옴 [0:6] = [:6]
# # # # print("뒤 7자리 : "+id[7:]) # 맨 마지막까지의 값을 구한다면 생략 가능 [7:14] = [7:]
# # # # print("뒤 7자리 (뒤에부터) : "+id[-7:]) [-7:-1] = [-7:] 맨뒷자리 숫자는 -1임.

# 11 문자열 처리함수

# # # python = "Python is Amazing"
# # # print(python.lower()) - 전체문장 소문자
# # # print(python.upper()) - 전제문장 대문자
# # # print(python[0].isupper())- 0번째문자가 대문자인지 아닌지 알려주는 boolean
# # # print(len(python)) - 문자길이알려줌
# # # print(python.replace("Python","Java")) - python을 java로 바꾸어서 출력됨

# # # index = python.index("n") - 문장에서 n이 몇번째에 있는지 알려줌
# # # print(index)
# # # index = python.index("n", index +1)- 처음 n 뒤부터 n 을 찾음
# # # print(index)

# # # print(python.find("Java")) # 내가 찾는 값이 없으면 -1을 값으로 꺼내주고 밑의 함수가 계속 진행이 됨
#  이것이 index와의 차이점
 # # print(python.find("n")) = python.index("n")
# # # # print(python.index("Java")) # index에는 내가 찾는 값이 없으면 Error를 일으키며 프로그램을 종료시킴.
#print(python.count("n")) - n이 문장안에서 몇번나오는지 알려줌

#12 문자열 포맷***************************************************************


#방법 1 - %를 사용하는 방법
# print("나는 %d살입니다. " % 20) # d 는 정수값만을 반영함
# print("나는 %s을 좋아해요." % "파이썬") - s = str 문자열을 넣겠다는 의미
# print("Apple 은 %c로 시작해요. " % "A") # c는 한 글자만 가져옴 

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # #방법 2 - {} 사용하는 방법
# # print("나는 {}살 입니다.".format(20))
# # print("나는 {}색과 {}색을 좋아해요. ".format("파란", "빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요. ".format("파란", "빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요. ".format("파란", "빨간"))


# # #방법 3 - {}와 변수를 같이 사용하는 방법
# # print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))



# # #방법 4 - 변수를 미리 만들고 난 후 {}를 사용하는 방법
# # age = 20
# # # color = "빨간"
# # # print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 13 탈출 문자


# # print("백문이 불여일견\n백견이 불여일타") #\n : 줄바꿈
# # print("저는 \"Sophie\"입니다.") #\" 혹은 \' 은 문장내에서 " 또는 '를 그대로 프린트하게 도와줌

# # #  \\ = 문장내에서 \ 로 프린트 해줌
# # # 우리는 프린트로 C:\Users\ricar\Desktop\PYTHONWORKSPACE> 를 하고 싶다면 
# # # print("C:\\Users\\ricar\\Desktop\\PYTHONWORKSPACE>")
# # #이렇게 쳐야 프린트 될때는 C:\Users\ricar\Desktop\PYTHONWORKSPACE>  이 결과값 이 도출 됨.
# # print("C:\\Users\\ricar\\Desktop\\PYTHONWORKSPACE>")

# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")  = PineApple
# # 위에처럼 하면 Pine이 문장 맨앞으로 오면서 그 문장앞에 원래있던 글자위에 덮어 씌움.

# # \b : 백스페이스 (한 글자 삭제 - \b앞의 글자를 삭제
# print("Redd\bApple") = RedApple


# # \t : 탭
# # print("Red\tApple") = Red         Apple
# # # -------------------------------Quiz 3 까지의 강의--------------------------------------[1 : 22: 31]


# 14 리스트 []

#append - 맨 뒤에 값을 추가함.
#insert - 정해진 위치에 값을 추가함
# subway.insert(1,"정형돈") - 정형돈을 1 자리에 추가함.
# pop 뒤에서부터 하나씩 값을 꺼내서 값을 출력하고 그룹에서 지움.
#sort - 순서대로 정렬
#Ex - num_list = [5,4,3,2,1]
# num_list.sort()
# print(num_list) = 출력값은 [1,2,3,4,5]

#sort의 반대도 가능 = reverse
# num_list.reverse() = 출력값은 [5,4,3,2,1]
# num_list.clear - 모든 값을 없앰 - [] 이라고 출력됨.

# list 끼리 합치는것도 가능함. 리스트 확장
# num_list = [5,4,3,2,1]
# mix_list = ["조세호", 20, True]
# num_list.extend(mix_list)
# print(num_list) - 출력값 : [5, 4, 3, 2, 1, '조세호', 20, True]

# 15 사전 {}
#dictionary = {key : value}
#print(dictionary(key)) - value가 출력됨.
#print(dictionary.get(key)) - Value가 출력됨.
#get의 차이점 - 일반적으로 key값이 사전내에 있을 경우, get을 쓰나 그냥 key값을 바로 쓰나 결과값은 동일함.
# 그러나 key값이 사전내에 존재하지 않은 경우, key값만으로 결과값을 도출할 시 error 발생하며 코드가 멈춤.
# get을 이용하여 결과값을 도출시, key가 사전내에 존재하지 않으므로 None이 출력된 후 그 다음 코드로 넘어감.
# 만약, key 값이 존재하지 않는 경우 None 대신 다른 결과값을 도출하고 싶다면 
#print(dictionary.get(key, "원하는 출력값기재")) 하게되면, key가 존재하지 않을 시 "" 안의 값이 출력됨.

# key값이 사전안에 존재하는지 아닌지
#print(3 in dictionary) : 3 이 사전안에 존재한다면 TRUE가 출력.


# cabinet = {"A-3":"유재석", "B-100": "조세호", "C-20":"김태호"}
# del cabinet["A-3"]
# print(cabinet)

# 새손님
#print(cabinet)
#cabinet["D-32":"Sophie"] > 추가 key & value 

# 16 튜플 () - 변경되지 않는 목록/ 대신 속도가 빠름.


# menu = ("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])
# 튜플에서는 add가 지원되지 않음.


# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
# (name, age, hobby) = ("김종국",20,"코딩")
# print(name, age, hobby)


# 17 set  집합 - 중복 안됨, 순서 없음 , 변경이 가능 list처럼


# my_set={1,2,3,3,3,3,4}
# print(my_set) #{1, 2, 3, 4}

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# #교집합 (java & python 모두 다룰 수 있는 사람) - and

# # print(java & python)
# # print(java.intersection(python))

# # 합집합  - or

# print(java|python) # {'박명수', '유재석', '김태호', '양세형'}
# print(java.union(python)) # {'박명수', '유재석', '김태호', '양세형'}

# #차집합(java ok python no)

# print(java - python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#java.remove("김태호")


# 18 자료구조의 변경


#커피숍
#menu = {"coffee", "milk", "juice"}
# list > tuple > set 교차가능

# ----------------------------------------------Quiz 4 까지의 강의------------------------------[1:57:33]


# 19 IF 
# if 조건 :
#   실행 명령문
#weather = "미세먼지"
#if weather == "Rain" : 
#   print("Please take your umbrella")
#elif weather == "microdirt" :
#   print("Please take your mask")
#else :
#   print("No need to prepare anything.")

# 20 For 반복문
#print("대기번호 : 1")
#print("대기번호 : 2")
#print("대기번호 : 3")
#print("대기번호 : 4")
#print("대기번호 : 5")

# for waiting_no in range(5) : # range(1,6)으로하면 1,2,3,4,5
#     print("대기번호 : {}".format(waiting_no))
# # 결과값
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4


# starbucks = ["아이언맨","토르","그루트"]
# for customer in starbucks :
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# 결과값 : 
# 아이언맨, 커피가 준비되었습니다.
# 토르, 커피가 준비되었습니다.
# 그루트, 커피가 준비되었습니다.


# 21  while 구문

# customer = "토르"
# index = 5
# while index >= 1 : # while (조건) :
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요." .format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기 처분 되었습니다.")

# 결과값 : 
# 토르, 커피가 준비되었습니다. 5 번 남았어요.
# 토르, 커피가 준비되었습니다. 4 번 남았어요.
# 토르, 커피가 준비되었습니다. 3 번 남았어요.
# 토르, 커피가 준비되었습니다. 2 번 남았어요.
# 토르, 커피가 준비되었습니다. 1 번 남았어요.
# 커피는 폐기 처분 되었습니다.


# customer = "아이언맨"
# index = 1
# while True : # while (조건) :
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회" .format(customer,index))
#     index += 1

# 결과값 : 
# 네버엔딩스토리.................... > 무한루프에 빠지게 됨. crtl + C 를 하면 강제 종료됨.


# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")
#     if person == customer :
#         print("{0}, 저희 커피와 함께 좋은 하루 되세요 :)".format(customer))


# 22 continue 와 break - 반복문 내에서 사용됨.

# absent = [2,5] # 결석
# no_book = [7] # 책을 깜박했음
# for student in range (1,11) : # 1 부터 10번까지
#     if student in absent :
#         continue     # 계속해서 다음 반복을 진행함
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와.".format(student))
#         break          # 조건과 만날경우 바로 프로그램 종료
#     print("{0}, 책을 읽어봐".format(student))

# 결과값 : 
# 1, 책을 읽어봐
# 3, 책을 읽어봐
# 4, 책을 읽어봐
# 6, 책을 읽어봐
# 오늘 수업 여기까지. 7은 교무실로 따라와.


# 23 한 줄로 끝내는 for 문장

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함. -> 101,102,103, 104

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students] #  len 문자열의 길이
# print(students)

# 결과값 : 
# [8, 4, 10]

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# 결과값 : 
# ['IRON MAN', 'THOR', 'I AM GROOT']

#---------------------------------------Quiz 5까지의 강의---------------------------------------
# 24 함수-----2:28:52

# # def open_account():           >> def  함수 정의만 해 두는 것. 실제로 호출하기 전까지는 실행되지 않음.
# #     print("새로운 계좌가 생성되었습니다.")
# # >> open_account() 를 해야 print문이 실행됨.

# # 25 전달값과 반환값

# def deposit(balance , money) :      #>> 여기서 (balance , money) 이 전달하려는 값. 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.". format(balance + money))
#     return balance + money          #>> 반환값

# # balance = 0 # 잔액
# # balance = deposit(balance, 1000)
# # print(balance)

# #>> 결과값 : 
# # # 입금이 완료되었습니다. 잔액은 1000 원입니다.
# # #1000

# # 출금하는 함수

# def withdraw(balacnce, money):  #출금
#     if balacnce >= money :  # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else :   # 잔액이 출금보다 적으면
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# # balance = 0 
# # balance = deposit(balance, 1000)
# # balance = withdraw (balance, 2000)
# # >>> 결과값 : 
# # 입금이 완료되었습니다. 잔액은 1000 원입니다.
# # 출금이 완료되지 않았습니다. 잔액은 1000 원입니다

# # balance = 0 
# # balance = deposit(balance, 1000)
# # balance = withdraw (balance, 500)

# # 결과값 : 
# # 입금이 완료되었습니다. 잔액은 1000 원입니다.
# # 출금이 완료되었습니다. 잔액은 500 원입니다.

# def withdraw_night(balacnce, money) : # 저녁에 출금 수수료 떼임
#     commission = 100 
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # # balance = withdraw(balance, 2000)
# # # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# # 결과 값
# # 입금이 완료되었습니다. 잔액은 1000 원입니다.
# # 수수료는 100원이며, 잔액은 400 원입니다.

 
#26 기본 값

# def profile(name, age, main_lan) :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lan))  # \ 하고 엔터치면 줄바꿈됨.

# profile("유재석", 20,"파이썬")
# profile("김태호", 25,"자바")

# 결과 값 : 

# 이름 : 유재석   나이 : 20       주 사용 언어 : 파이썬
# 이름 : 김태호   나이 : 25       주 사용 언어 : 자바

# 가정 - 같은 학교 같은학년 같은 반 같은 수업.

# def profile(name, age = 17, main_lan = "python") : # 정보를 전달 받지 못하였을때, 나이와 언어는 기본값으로 출력
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lan))
# profile("유재석")
# profile("김태호")

# # 결과값 : 

# 이름 : 유재석   나이 : 17       주 사용 언어 : python
# 이름 : 김태호   나이 : 17       주 사용 언어 : python


# 27 키워드 값

# def profile (name, age, main_lan) :
#     print(name, age, main_lan)

# profile(name = "유재석", main_lan = "python", age = 20)
# profile( main_lan = "자바",name = "김태호", age = 40)

# 결과값 : 
# 유재석 20 python
# 김태호 40 자바


# 28 가변인자


# def profile(name, age, lan1, lan2, lan3, lan4, lan5) :
#     print("이름 : {0}\t나이 : {1}\t".format(name, age),end=" ")
#     print(lan1,lan2,lan3,lan4,lan5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호",25,"Kotlin", "Swift","","","")

# 결과값 :
# 이름 : 유재석   나이 : 20        Python Java C C++ C#
# 이름 : 김태호   나이 : 25        Kotlin Swift

# 이 상태에서 유재석이 언어를 하나 더 배우면 위의 함수자체를 바꿔야 하는 상황이 옴.
# 그럴때 밑의 함수를 쓰는 거임.

# def profile(name, age, *language) : # *로 시작하는 가변인자. *이 옴으로써 내가 넣고 싶은만큼의 lan을 출력가능
#     print("이름 : {0}\t나이 : {1}\t".format(name, age),end=" ")
#     for lan in language :
#         print(lan, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#","JavaScript")
# profile("김태호",25,"Kotlin", "Swift")

# 결과값 : 
# 이름 : 유재석   나이 : 20        Python Java C C++ C# JavaScript
# 이름 : 김태호   나이 : 25        Kotlin Swift

#----------------------------29 지역변수(함수내에서만 쓸 수 있음)와 전역변수 (2:47:55) // 책갈피
# 전역변수(프로그램 내에서 어디서든지 부를 수 있음)

# gun = 10 # 전역변수

# def checkpoint(soldiers) : # 경계근무 나가는 군인 수
#     gun = gun - soldiers # 두번째 gun이 정의가 되지 않음.
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

# >> 결과 값 : UnboundLocalError: local variable 'gun' referenced before assignment

# gun = 10 # 전역변수

# def checkpoint(soldiers) : # 경계근무 나가는 군인 수
#     gun = 20 # 지역변수
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

# >>결과값 : 
# 전체 총 : 10
# [함수 내] 남은 총 : 18 # 함수로 인해 gun이 정의됨.
# 남은 총 : 10

# gun = 10 # 전역변수

# def checkpoint(soldiers) : # 경계근무 나가는 군인 수
#     global gun # 전역 공간에 있는 gun을 불러와서 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

# >> 결과값 : 
# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

# 주로 전역변수를 많이 쓰면 코드 관리가 어려워짐. 가급적 함수의 전달값으로 parameter를 던져서 계산을 하고 반환값을
#받아서 사용 하는방법이 밑에 함수임.

# gun = 10 # 전역변수

# def checkpoint_ret(gun,soldiers) :
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))


# >> 결과값 : 
# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

# --------Quiz 6

# 30 표준 입출력


# print("PYthon", "Java")
# print("PYthon", "Java", sep=",") # sep = separate with " ..."
# print("PYthon", "Java",sep = " vs ")

#>>>> 결과값 : 
# PYthon Java
# PYthon,Java
# PYthon vs Java

# print("Python", "Java", sep=",", end ="?")
# print("무엇이 더 재밌을까요?")

# >> 결과값 : Python,Java?무엇이 더 재밌을까요?

# import sys
# print("PYthon", "Java", file=sys.stdout) # 표준 출력
# print("PYthon", "Java", file=sys.stderr) # 표준 에러

# >> 결과값 : 
# PYthon Java
# PYthon Java



# 시험 성적
# scores = {"수학" : 0 , "영어" : 50, "코딩": 100}
# for subject, score in scores.items(): # 키와 밸류가 페어로 둘다나옴.
#     print(subject,score)

# >> 결과값 : 
# 수학 0
# 영어 50
# 코딩 100

# scores = {"수학" : 0 , "영어" : 50, "코딩": 100}
# for subject, score in scores.items(): # 키와 밸류가 페어로 둘다나옴.
#     print(subject.ljust(5), str(score).rjust(4),sep=":") # ljust(2) - 왼쪽으로 정렬하되 2 자리를 확보해줘
#                                                         # rjust(2) - 오른쪽으로 정렬하되 2 자리를 확보해줘
# >> 결과값 : 

# 수학   :   0
# 영어   :  50
# 코딩   : 100



# 은행 대기 순번표
# 보틍의 은행 대기 순번표 - 001, 002, 003 ````````

# for num in range (1,21) : # 1부터 20까지의 숫자
#     print("대기번호 : " + str(num).zfill(3))  # zfill(3) : 3자리를 확보하되 값이 없는 자리는 0으로 채워줘

# >>결과값 :
# 대기번호 : 001
# 대기번호 : 002
# ......

# 대기번호 : 019
# 대기번호 : 020


# answer = input ("아무 값이나 입력하세요 : ") # input으로 받은 값은 항상 str 스트링 형태로 들어옴.  
                                             ## input으로 받은 값은 숫자넣어도 문자로 인식
# print("입력하신 값은 " + answer + " 입니다.")



# 31 다양한 출력 포맷




# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))  # {0: >10} - 0 뒤가 비어있으므로 빈공간으로 두는 것을 나타냄
                                 ##{0: >10} - > 오른쪽 정렬을 의미
                                 ##{0: >10} - 10  열자리 공간을 확보


# # 양수일 때는 +로 표시, 음수일 땐 -로 표시 # 주식의 가격변동같은...?
# print("{0: >+10}".format(500)) 
# print("{0: >+10}".format(-500)) 
# print("{0: >10}".format(500))  # >> 10앞에 + 부호가 없는 경우 양수일 때 그냥 숫자만 표기됨. + 500아님.

# >>결과값 : 

#       +500
#       -500
#        500


# # # 왼쪽 정렬하고, 빈칸을 _ 로 채움
# print("{0:_<+10}".format(500)) 
# >>> 결과값 : +500______


# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000)) 
# >> 결과값 : 100,000,000,000,000


# # #3자리마다 콤마를 찍어주기, + - 부호도 붙이기
# print("{0:+,}".format(100000000000000)) 
# print("{0:+,}".format(-100000000000000)) 
# >>> 결과값 : 
# +100,000,000,000,000
# -100,000,000,000,000

# print("{0:,+}".format(100000000000000)) 
# print("{0:,+}".format(-100000000000000)) 
# >>>> 결과값 : ValueError: Cannot specify ',' with '+'.



# #3자리마다 콤마를 찍어주기, + - 부호도 붙이기, 자릿 수 확보
# # 돈이 많으면 행복하니 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(100000000000000)) # : 1. 빈칸채울거 2. 정렬 3. 부호 4. 자릿수 확보 5. 콤마
# >>>결과값 : +100,000,000,000,000^^^^^^^^^^


# # # 소수점 출력
# print("{0:f}".format(5/3)) 
# >>>결과값 : 1.666667


# # 소수점 특정 자리수 까지만 표시 (소수점 3 째 자리에서 반올림)
# print("{0:.2f}".format(5/3)) 
# >>>결과값 : 1.67



# 32 파일 입출력



# score_file = open("score.txt","w", encoding = "utf8") # (파일이름, 용도,..? ) w 는 쓰기용
# print("수학 : 0", file = score_file)
# print("영어 : 50", file=score_file)
# score_file.close() ## 파일을 open 했다면 반드시 close해야함.

# score_file = open("score.txt","a", encoding="utf8") # a 는 추가용(원래 있던 파일에 내용 추가) -append를 나타냄
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # \n : 줄바꿈
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r 은 모든 내용 읽어오기 - read
# print(score_file.read()) # 파일에 있는 모든 파일을 읽어옴.
# score_file.close()
# >>>> 결과값 : 
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(),end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()
# >>> 결과값 :
# 수학 : 0


# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(),end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# >>> 결과값 : 
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100


# score_file = open("score.txt", "r", encoding="utf8")
# while True : # 파일의 내용이 총 몇 줄일지 모를때
#     line = score_file.readline() 
#     if not line : # 만약 더이상의 읽어올 내용이 없다면
#         break # 반복문 탈출
#     print(line)
# score_file.close()

# >>> 결과값 : 
# 수학 : 0

# 영어 : 50

# 과학 : 80

# 코딩 : 100

# for 구문으로 불러오기

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines :
#     print(line, end="")

# score_file.close()

# >> 결과값 :
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 10



# 33 pickle - 프로그램상에서 사용하는 데이터를 파일형태로 저장하는 모듈




# import pickle
# profile_file = open("profile.pickle", "wb") # 'w' - 쓰기목적 'b' - binary - 이진법형태
# profile = {"이름" : "박세은", "나이" : 29, "취미":["독서","메이크업", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# >>> 결과값 :
# {'이름': '박세은', '나이': 29, '취미': ['독서', '메이크업', '코딩']}

# import pickle
# profile_file = open("profile.pickle", "rb") # 'r' - 읽기목적 'b' - binary - 이진법형태
# profile = pickle.load(profile_file) # 파일에 있는 내용을 그대로 데이터 형태로 profile에 불러옴.
# print(profile)
# profile_file.close()

# >>> 결과값 :
# {'이름': '박세은', '나이': 29, '취미': ['독서', '메이크업', '코딩']}



# 34 - with

# import pickle

# with open("profile.pickle","rb") as profile_file : # close 할 필요가 없음
#     print(pickle.load(profile_file))

# >>>결과값 : 

# {'이름': '박세은', '나이': 29, '취미': ['독서', '메이크업', '코딩']}

# with open("study.txt","w", encoding="utf8") as study_file :
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file :
#     print(study_file.read())

# >> 결과값 : 파이썬을 열심히 공부하고 있어요


# 35 - 클래스

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음.
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage  = 5 # 유닛의 공격력
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# >>>  결과값 : 

# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5

# 탱크 : 공격 유닛, 탱크 ,포를 쏠 수 있는데 일반모드 / 시즈 모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다, [공격력 {2}]".format( \
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 클래스 - 붕어빵 틀에 비유함, 틀은 하나인데 만들수 있는 빵은 무수함.

# class Unit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# >>> 결과값 :

# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성 되었습니다.
# 체력 150, 공격력 35



# 36  __init__

# __init__ : 생성자, 객체
# 이 함수를 쓸 때 (self, name, hp, damage) 여기서 self 를 제외한 값의 갯수만큼의 값을 넘겨주어야 함.
# ex  - marine1 = Unit("마린", 40, 5) - good
#      marine2 = Unit("마린", 5) - error




# 37  멤버 변수 - 클래스 내에서 정의된 변수.

# class Unit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# # 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80,5)
# print("유닛 이름 :  {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80,5)
# wraith2.clocking = True

# if wraith2.clocking == True : 
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

 

# 38 메소드



# 일반 유닛
# class Unit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#공격 유닛
# class AttackUnit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0 : 
#             print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병


# # 파이어택 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50,16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)



# 39 상속




# #일반 유닛
# class Unit :  # >> 부모 클래스
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# #공격 유닛
# class AttackUnit(Unit):    # (Unit)을 적음으로서 Unit 클래스에서 상속하겠다는 것을 의미 # 자식 클래스
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)  # 상속받는 정보
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0 : 
#             print("{0} : 파괴되었습니다.".format(self.name))

# #메딕 : 의무병


# # 파이어택 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50,16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)




# 40 다중 상속




# #일반 유닛
# class Unit :  # >> 부모 클래스
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# #공격 유닛
# class AttackUnit(Unit):    # (Unit)을 적음으로서 Unit 클래스에서 상속하겠다는 것을 의미 # 자식 클래스
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)  # 상속받는 정보
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0 : 
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가능


# # 날 수 있는 기능을 가진 클래스
# class Flyable : 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location , self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self,flying_speed)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6,5)
# valkyrie.fly(valkyrie.name, "3시")




# 41 메소드 오버라이딩



# #일반 유닛
# class Unit :  # >> 부모 클래스
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# #공격 유닛
# class AttackUnit(Unit):    # (Unit)을 적음으로서 Unit 클래스에서 상속하겠다는 것을 의미 # 자식 클래스
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp,speed)  # 상속받는 정보
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0 : 
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가능


# # 날 수 있는 기능을 가진 클래스
# class Flyable : 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location , self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 , damage) # 지상 스피드를 0으로 받음.
#         Flyable.__init__(self,flying_speed)
    
#     def move(self, location) : 
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# #배틀 크루저 : 공중 유닛, 체력 / 공격력이 매우 좋음.

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# #battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# #>> 결과값 : 

# [지상 유닛 이동]
# 벌쳐 : 11시 방향으로 이동합니다. [속도 10]
# [공중 유닛 이동]
# 배틀크루저 : 9시 방향으로 날아갑니다. [속도 3]



# 42 pass



# #일반 유닛
# class Unit :  # >> 부모 클래스
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# #공격 유닛
# class AttackUnit(Unit):    # (Unit)을 적음으로서 Unit 클래스에서 상속하겠다는 것을 의미 # 자식 클래스
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp,speed)  # 상속받는 정보
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0 : 
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가능


# # 날 수 있는 기능을 가진 클래스
# class Flyable : 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location , self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 , damage) # 지상 스피드를 0으로 받음.
#         Flyable.__init__(self,flying_speed)
    
#     def move(self, location) : 
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit) : 
#     def __init__(self, name, hp, location) : 
#         pass

# # 서플라이 디폿 : 건불 , 1개 건물 = 8개 유닛 생성 가능
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# >> 결과값 : [알림] 새로운 게임을 시작합니다.



# 43 super



# #일반 유닛
# class Unit :  # >> 부모 클래스
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# #공격 유닛
# class AttackUnit(Unit):    # (Unit)을 적음으로서 Unit 클래스에서 상속하겠다는 것을 의미 # 자식 클래스
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp,speed)  # 상속받는 정보
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0 : 
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가능


# # 날 수 있는 기능을 가진 클래스
# class Flyable : 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location , self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 , damage) # 지상 스피드를 0으로 받음.
#         Flyable.__init__(self,flying_speed)
    
#     def move(self, location) : 
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit) : 
#     def __init__(self, name, hp, location) : 
#         #Unit.__init__(self, name, hp, 0) # 이거를 쓰거나
#         super().__init__(name, hp, 0) # 이거를 쓰거나 둘 중 하나. super를 쓸 때는 () 가 있어야하고 self가 필요X
#         self.location = location

# # >>> 다중 상속을 하는 경우에는 super가 적합하지 않음. practice_class 파일을 참조.




# 44 스타크래프트 전반전

# from random import *

# #일반 유닛
# class Unit :  # >> 부모 클래스
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
    
#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#             print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#             self.hp -= damage
#             print ("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#             if self.hp<=0 : 
#                 print("{0} : 파괴되었습니다.".format(self.name))

# #공격 유닛
# class AttackUnit(Unit):    # (Unit)을 적음으로서 Unit 클래스에서 상속하겠다는 것을 의미 # 자식 클래스
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp,speed)  # 상속받는 정보
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공력 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

# # 마린

# class Marine(AttackUnit) :
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40,1,5)
    
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가시켜줌, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10 :
#             self.hp -=10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
    

# #탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격가능. 이동 불가
#     seize_developed = False #   시즈모드 개발여부
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150,1,35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False :
#             return
#         # 현재 시즈모드가 아닐때  -- > 시즈모드
#         if self.seize_mode == False :
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage*= 2
#             self.seize_mode = True
        
#         # 현재 시즈모드 일 때 --> 시즈모드 해제
#         else :
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# # 날 수 있는 기능을 가진 클래스
# class Flyable : 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name,location , self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 , damage) # 지상 스피드를 0으로 받음.
#         Flyable.__init__(self,flying_speed)
    
#     def move(self, location) : 
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20,5)
#         self.clocked = False #  클로킹 모드 (해제상태)

#     def clocking(self):
#         if self.clocked == True : # 클로킹 모드 - > 모드 해제
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked = False

#         else : #  클로킹모드 해제상태 - > 모드 설정
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.clocked = True
            


# # 45 스타크래프트 후반전

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg") # Good game
#     print("[Player]  님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 시작

# game_start()

# # 마린 3 기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2 기 생성

# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units : 
#     unit.move("1시")

# # 탱크 시즈모드 개발

# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공력 모드 준비(탱크 : 시즈모드, 마린 : 스팀팩, 레이스 : 클로킹)

# for unit in attack_units:
#     if isinstance(unit, Marine) : # 지금 만들어진 객체가 어느 클래스의 인스턴스인지 확인 
#         unit.stimpack()
    
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()

#     elif isinstance(unit, Wraith):
#         unit.clocking()


# # 전군 공격

# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (5~20)

# # 게임 종료
# game_over()





# 46 예외 처리 = 에러 처리

# 47 에러 발생시키기

# 48 사용자 정의 예외 처리

# 49  fanally - 예외처리 중 에러가 발생여부와 상관없이 항상 실행됨.

# 50  모듈 - 같은 폴어에 있어야 사용 가능

# import theater_module

# theater_module.price(3) # 3명이서 영화보러 갔을 때의 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을때

# import theater_module as mv # theater_module 를 mv라는 별명을 붙여서 호출가능하게 함.

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * 

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning #  특정 함수만 불러서 사용할 때
# price(5)
# price_morning(6)
# # >>> price_soldier 은 사용 불가능

# from theater_module import price_soldier as price
# price(5)
# # price_soldier의 내용을 price 내용에 넣어서 불러서 사용함.
# # >> 결과값 : 5 명 군인 할인 가격은 20000 원 입니다.



# 51  패키지- 모듈들을 모아놓은 집합.

# import travel.thailand #  import 사용시 맨뒤에 모듈 또는 패키지만 가능, 클래스나 함수는 직접 import할 수 없음.
# # import travel.thailand.ThailandPackage >> 사용 불가 / ThailandPackage 는 클래스임.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # >> 결과값 : [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50 만원

# from travel.thailand import ThailandPackage # from으로 불러오는 경우에는 클래스를 바로 불러올 수 있음.
# trip_to = ThailandPackage()
# trip_to.detail()

# # >>> 결과값 : [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50 만원

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# #>> 결과값 : [베트남 패키지 3박 5일] 다낭 효도 여행 60만원





# 52 __all__

# from travel import * 

# #trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# # >>> 이렇게 하면 에러가 뜸. __init__파일에 __all__ = ["vietnam"]  저장했을경우 잘 나옴.




# 53  모듈 직접 실행

# from travel import * 

# trip_to = thailand.ThailandPackage()
# trip_to.detail()



# 54 패키지, 모듈 위치를 확인하는 방법

# import inspect
# import random
# print(inspect.getfile(random))


# from travel import * 

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# # >>> 결과값 : 
# # C:\Users\ricar\AppData\Local\Programs\Python\Python37-32\lib\random.py
# # c:\Users\ricar\Desktop\PYTHONWORKSPACE\travel\thailand.py




# 55 pip install - pip 로 패키지 설치하기
# 구글에서 pypi로 검색

# >>>>>>>>>>>pip 안됨........제발 알려줘

# # pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, 
# or operable program. Check the spelling of the name, or if a path was included, verify   
# At line:1 char:1
# + pip install beautifulsoup4
# + ~~~
#     + CategoryInfo          : ObjectNotFound: (pip:String) [], CommandNotFoundException  
#     + FullyQualifiedErrorId : CommandNotFoundException
 
# PS C:\Users\ricar\Desktop\PYTHONWORKSPACE> pip list
# pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, 
# or operable program. Check the spelling of the name, or if a path was included, verify   
# that the path is correct and try again.
# At line:1 char:1
# + pip list
# + ~~~
#     + CategoryInfo          : ObjectNotFound: (pip:String) [], CommandNotFoundException  
#     + FullyQualifiedErrorId : CommandNotFoundException




# 56    내장함수 - 내장되어있어서 따로 import 할 필요 없이 바로 쓸 수 있음.
# ex : input
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줫을 때 그 객체가 어떤 변수와 함수를 가지고 있는 지 표시
# print(dir())
# import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 구글에서 list of python builtins 검색


# 57 외장함수 - 직접 import해서 써야함.

# 구글에서 list of python modules 검색

# glob : 경로내의 폴더 / 파일 목록 조회 (윈도우의 dir와 같음)

# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일


# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")

# else : 
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")


# import os
# # print(os.listdir())

# import time # 시간관련 함수

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# # >> 결과값 : 
# 2020-06-22 23:59:24

# import datetime
# print("오늘 날짜는", datetime.date.today())
# # >>> 결과값 : 오늘 날짜는 2020-06-23

# timedelta : 두 날짜 사이의 간격
# import datetime
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# # >> 오늘으로 부터 100일 이후를 출력함.
# print("우리가 만난지 100일은", today + td)

################################################ 공만들기 게임 연습################################

lst = ["가", "나", "다"]

for lst_idx, lst_val in enumerate(lst): 
    print(lst_idx, lst_val)

# ## >> 결과값 : 

# 0 가
# 1 나
# 2 다