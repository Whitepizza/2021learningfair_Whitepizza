#알고리즘

#퀴즈 함수
#힌트 함수



from tkinter import *


#시작 UI

print("")
print("                                             ooooooo     𐦀    𐦀     ⌧           𐦀                                                                                                     ")
print("                                            ooooooooo    𐦀    𐦀     ⌧           𐦀                                                                                                     ")
print("                                           ooooooooooo   𐦀 𐦀 𐦀 𐦀     ⌧           𐦀                                                                                                     ")
print("                                           ooooooooooo   𐦀 𐦀 𐦀 𐦀     ⌧           𐦀                                                                                                     ")
print("                                            ooooooooo    𐦀    𐦀     ⌧           𐦀                                                                                                     ")
print("                                             ooooooo     𐦀    𐦀     ⌧⌧⌧⌧⌧  𐦀                                                                                                       ")
print("                                                                                     oooooooo    𐦀    ⌧⌧⌧⌧⌧                                                                      ")
print("                                                                                            o    𐦀       ⌧⌧                                                                         ")
print("                                                                                     oooooooo    𐦀      ⌧  ⌧                                                                        ")
print("                                                                                            o    𐦀                                                                                    ")
print("                                                                                     𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀    𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀                                                                    ") 
print("                                                                                           𐦀     𐦀                                                                                    ")
print("                                                                                                                      ooooooooo  𐦀         ooooo      ⌧⌧⌧⌧⌧  𐦀 𐦀                  ")
print("                                                                                                                      ooooooooo  𐦀        ooooooo             ⌧  𐦀 𐦀                  ")
print("                                                                                                                      ooooooooo  𐦀 𐦀 𐦀       o o               ⌧  𐦀 𐦀                  ")
print("                                                                                                                      ooooooooo  𐦀         o   o              ⌧  𐦀 𐦀                  ")
print("                                                                                                                                                                                       ")
print("                                                                                                                       𐦀 𐦀 𐦀 𐦀 𐦀 𐦀         𐦀 𐦀 𐦀 𐦀 𐦀 𐦀 𐦀                                     ")
print("                                                                                                                         𐦀  𐦀                o                                        ")
print("                                                                                                                        𐦀    𐦀               o                                          ")


print("\n\n                                                                                        <애니 퀴즈 맞추기!>")

print("\n\n\n\n                                                 *   알고리즘과 게임컨텐츠 1분반 11조(하얀피자) 김혜린 장예진 주영주 최영은  * \n\n")
print("                                                                          PRESS ENTER TO START ")

input()

print("\n\n\n                       안녕하세요. 애니 퀴즈 맞추기 게임에 오신 것을 환영합니다. 게임을 시작하기 전에 간단히 게임설명을 하겠습니다. \n")

input()

print("""\n\n                       이 게임은 두 가지로 이루어져 있습니다. 하나는 스무고개처럼 텍스트 힌트를 통해 애니메이션의 제목을 맞추는 게임이고,
                                                           다른 하나는 방금 맞춘 그 애니메이션의 캐릭터를 맞추는 게임입니다.""")

input()

print("""\n\n                       각 게임에서는 참고한 힌트가 적을수록, 시도 횟수가 적을수록 높은 점수를 얻을 수 있습니다. 안내에 따라 즐겁게 게임을 즐겨보세요.\n\n\n                  START!""")

input()


score = 0 #게임마다 획득할 점수 변수
trial = 5 #게임마다 시도한 횟수
sum_score = 0 #전체 획득 점수


def print_O():
    print("")
    print("                  ☺☺☺☺☺☺☺           ")
    print("                ☺☺☺☺☺☺☺☺☺☺☺         ")
    print("               ☺☺☺☺☺☺☺☺☺☺☺☺☺        ")
    print("              ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺       ")
    print("              ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺       ")
    print("              ☺☺☺☺☺☺☺o☺☺☺☺☺☺☺       ")
    print("              ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺       ")
    print("              ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺       ")
    print("               ☺☺☺☺☺☺☺☺☺☺☺☺☺        ")
    print("                ☺☺☺☺☺☺☺☺☺☺☺         ")
    print("                  ☺☺☺☺☺☺☺           ")


def print_X():
    print("") 
    print("                𐦀          𐦀          ")
    print("                 𐦀        𐦀           ")
    print("                  𐦀      𐦀            ")
    print("                   𐦀    𐦀             ")
    print("                    𐦀  𐦀              ")
    print("                     𐦀𐦀               ")
    print("                     𐦀                ")
    print("                     𐦀𐦀               ")
    print("                    𐦀  𐦀              ")
    print("                   𐦀    𐦀             ")
    print("                  𐦀      𐦀            ")
    print("                 𐦀        𐦀           ")
    print("                𐦀          𐦀          ")
    print("               𐦀            𐦀         ")
   
 
 


    

    



def Hint_1(): #스폰지밥 힌트를 출력해주는 함수
    
    global Hint_num #힌트번호 전역변수
    global score #획득할 점수 전역변수

    #힌트를 적게 볼수록 획득점수 많아진다.

    if Hint_num == 0:
        print("\n\n\n1. 바닷속이 배경인 애니메이션입니다.\n")
        input()
        score = 10 #1번 힌트만 보고 맞추면 10점
        
    elif Hint_num == 1:
        print("\n\n\n1. 바닷속이 배경인 애니메이션입니다. \n\n2. 주인공은 햄버거집에서 일을 합니다.\n")
        input()
        score = 5 #2번 힌트까지 보고 맞추면 5점
        
    elif Hint_num == 2:
        print("\n\n\n1. 바닷속이 배경인 애니메이션입니다. \n\n2. 주인공은 햄버거집에서 일을 합니다. \n\n3.주인공은 네모바지를 입고 있습니다.\n")
        input()
        score = 3 #3번 힌트까지 보고 맞추면 3점
    
    else:
        print("\n\n\n4. 셋 중 하나에 답이 있습니다 \n\n1)스펀지밥 \n\n2)귀멸의 칼날 \n\n3)토이스토리\n")
        input()
        score = 1 #선택지 보고 맞추면 1점


#힌트함수 2, 3은 힌트함수 1과 같은 형식이다.

def Hint_2():
    
    global Hint_num
    global score

    if Hint_num == 0:
        print("\n\n\n1. 이 애니의 주인공 가족은 4인가족 입니다.\n")
        input()
        score = 10
        
    elif Hint_num == 1:
        print("\n\n\n1. 이 애니의 주인공 가족은 4인가족 입니다. \n\n2. 하얀 강아지를 키웁니다.\n")
        input()
        score = 5
        
    elif Hint_num == 2:
        print("\n\n\n1. 이 애니의 주인공 가족은 4인가족 입니다. \n\n2. 하얀 강아지를 키웁니다. \n\n3.이 만화의 주인공은 5살입니다.\n")
        input()
        score = 3
    
    else:
        print("\n\n\n4. 셋 중 하나에 답이 있습니다 \n\n1)코난 \n\n2)짱구 \n\n3)겨울왕국\n")
        input()
        score = 1
        


def Hint_3():
    
    global Hint_num
    global score

    if Hint_num == 0:
        print("\n\n\n1. 이 만화는 십 년이 넘게 아직 연재중입니다.\n")
        input()
        score = 10
        
    elif Hint_num == 1:
        print("\n\n1. 이 만화는 십 년이 넘게 아직 연재중입니다. \n\n2. 이 만화의 주인공은 보물을 찾아다닙니다.\n")
        input()
        score = 5
        
    elif Hint_num == 2:
        print("\n\n\n1. 이 애니의 주인공 가족은 4인가족 입니다. \n\n2. 이 만화의 주인공은 보물을 찾아다닙니다. \n\n3. 이 만화의 주인공은 밀집모자를 쓰고 있습니다.\n")
        input()
        score = 3
    
    else:
        print("\n\n\n4. 셋 중 하나에 답이 있습니다 \n\n1)토토로 \n\n2)원피스 \n\n3)나루토\n")
        input()
        score = 1



def Quiz_1(): #퀴즈를 만들어주는 함수이다.

    global Hint_num #볼 힌트번호를 저장할 전역 변수
    global trial #시도횟수 전역 변수
    global sum_score #전체 획득점수
    global score #이번 게임에서 획득할 점수

    Hint_num = 0 #처음은 1번힌트를 출력하기 위해 0으로 초기화

    trial = 5 #시도는 5번까지 가능하도록 설정
    
    answer = "스펀지밥" #정답 문자열
    user = "" #사용자의 정답을 저장할 변수

    print("잘 오셨습니다!")

    input()
    
    print("<이 게임은 애니메이션 이름 맞추기 게임입니다.>")
    input()

    print("이 게임은 시도 횟수와 상관없이, 적은 힌트를 가지고 맞출수록 높은 점수를 얻습니다.")
    input()

    print("하지만 5번까지 시도할 수 있습니다. 1개의 힌트를 보고 맞추면 10점, 본 힌트가 늘어날수록 5, 3, 1 순서로 점수가 줄어듭니다. 힌트는 총 4개!")

    input()
    
    print(f"\n현재 스코어 :{sum_score}") #현재 총 스코어를 보여준다.

    input()

    while 1:

        print("\n\n이번 문제에서 남은 도전 횟수: ", trial)

        input()

        
        print("\n1번 퀴즈입니다. 다음 힌트를 듣고 맞는 정답을 입력해 주세요")

        input()
        
        Hint_1()

        user = input("정답은?:")

        if answer == user:
            
            print("\n\n정답입니다!\n\n\n")

            print_O()            

            input()
            
            print(Hint_num + 1,"번 힌트에서 맞추셨군요.")
            
            sum_score = sum_score + score #획득한 점수를 전체 획득 점수에 추가
            
            print(f"이번 게임에서 획득한 점수는 {score}점 입니다.\n")
            print(f"현재 점수는 {sum_score}점 입니다.\n")

            print("다음 문제로 넘어갑니다.")

            input()
            
            break #while문을 빠져나가게 된다.

        else:
            print("\n\n틀렸습니다.\n") #틀렸을경우
            print_X()
            input()
            
            if trial == 1: #시도횟수 소진시
                score = 0
                print("\n횟수가 소진되었습니다. 다음 퀴즈로 넘어갑니다.\n") 

                input()
                
                break

            else: #시도횟수가 남았다면
                trial = trial - 1 #시도횟수 하나 빼기
                while 1:
                    print("\n재시도를 원하시면 1, 다음 힌트를 원하시면 2를 눌러주세요\n")
                    re_or_nextHint = input("1 혹은 2를 입력하세요 :")

                    if re_or_nextHint == '1': #재시도를 원하는 경우
                        break #다시 문제로 돌아가 보았던 힌트만 보고 다시 재시도
        
                    elif re_or_nextHint == '2': #힌트를 더 보길 원하는 경우
                        Hint_num = Hint_num + 1 #다음 힌트를 보고 재시도
                        if Hint_num>3:
                            print("\n4번 힌트까지 모두 보셨습니다. 힌트는 다시 4번까지 출력해 드립니다.\n") #만약 힌트를 다 보면 안내하기

                            input()
                        
                        break
                    else: #1이나 2가 아닌 다른 문자 입력시 다시 입력 요청
                        print("잘못 입력하셨습니다. 다시 입력하세요.")
                        input()
                        continue
                continue

#퀴즈 함수 2와 3도 1과 같은 형식이다.

def Quiz_2():

    global Hint_num
    global trial
    global sum_score
    global score

    Hint_num = 0


    trial = 5
    
    answer = "짱구"
    user = ""

    print("두 번째 문제로 어서 오세요!")

    input()

    print("<이 게임은 애니메이션 이름 맞추기 게임입니다.>")
    input()

    print("이 게임은 시도 횟수와 상관없이, 적은 힌트를 가지고 맞출수록 높은 점수를 얻습니다.")
    input()

    print("하지만 5번까지 시도할 수 있습니다. 1개의 힌트를 보고 맞추면 10점, 본 힌트가 늘어날수록 5, 3, 1 순서로 점수가 줄어듭니다. 힌트는 총 4개!")

    input()

    print(f"\n현재 스코어 :{sum_score}")

    input()

    while 1:

        print("\n\n이번 문제에서 남은 도전 횟수: ", trial)

        input()
        
        
        print("\n2번 퀴즈입니다. 다음 힌트를 듣고 맞는 정답을 입력해 주세요")

        input()
        
        Hint_2()

        user = input("정답은?:")

        if answer == user:
            
            print("\n\n정답입니다!\n\n\n")

            print_O()            

            input()
            
            print(Hint_num + 1,"번 힌트에서 맞추셨군요.")
            
            sum_score = sum_score + score
            
            print(f"이번 게임에서 획득한 점수는 {score}점 입니다.\n")
            print(f"현재 점수는 {sum_score}점 입니다.\n")

            print("다음 문제로 넘어갑니다.")

            input()
            
            break

        else:
            print("\n\n틀렸습니다.\n")
            print_X()
            input()
            
            if trial == 1:
                score = 0
                print("\n횟수가 소진되었습니다. 다음 퀴즈로 넘어갑니다.\n")

                input()
                
                break

            else:
                trial = trial - 1
                while 1:
                    print("\n재시도를 원하시면 1, 다음 힌트를 원하시면 2를 눌러주세요\n")
                    re_or_nextHint = input("1 혹은 2를 입력하세요 :")

                    if re_or_nextHint == '1':
                        break
        
                    elif re_or_nextHint == '2':
                        Hint_num = Hint_num + 1
                        if Hint_num>3:
                            print("\n4번 힌트까지 모두 보셨습니다. 힌트는 다시 4번까지 출력해 드립니다.\n")

                            input()
                        
                        break
                    else:
                        print("잘못 입력하셨습니다. 다시 입력하세요.")
                        input()
                        continue
                continue



def Quiz_3():

    global Hint_num
    global trial
    global sum_score
    global score

    Hint_num = 0


    trial = 5
    
    answer = "원피스"
    user = ""

    print("\n\n\n애니이름 퀴즈의 마지막 문제!")
    

    print("<이 게임은 애니메이션 이름 맞추기 게임입니다.>")
    input()

    print("이 게임은 시도 횟수와 상관없이, 적은 힌트를 가지고 맞출수록 높은 점수를 얻습니다.")
    input()

    print("하지만 5번까지 시도할 수 있습니다. 1개의 힌트를 보고 맞추면 10점, 본 힌트가 늘어날수록 5, 3, 1 순서로 점수가 줄어듭니다. 힌트는 총 4개!")

    input()



    input()

    print(f"\n현재 스코어 :{sum_score}")

    input()

    while 1:

        print("\n\n이번 문제에서 남은 도전 횟수: ", trial)

        input()


        
        
        print("\n3번 퀴즈입니다. 다음 힌트를 듣고 맞는 정답을 입력해 주세요")

        input()
        
        Hint_3()

        user = input("정답은?:")

        if answer == user:
            
            print("\n\n정답입니다!\n\n\n")

            print_O()            

            input()
            
            print(Hint_num + 1,"번 힌트에서 맞추셨군요.")
            
            sum_score = sum_score + score
            
            print(f"이번 게임에서 획득한 점수는 {score}점 입니다.\n")
            print(f"현재 점수는 {sum_score}점 입니다.\n")

            print("다음 문제로 넘어갑니다.")

            input()
            
            break

        else:
            print("\n\n틀렸습니다.\n")
            print_X()
            input()
            
            if trial == 1:
                score = 0
                print("\n횟수가 소진되었습니다. 다음 퀴즈로 넘어갑니다.\n")

                input()
                
                break

            else:
                trial = trial - 1
                while 1:
                    print("\n재시도를 원하시면 1, 다음 힌트를 원하시면 2를 눌러주세요\n")
                    re_or_nextHint = input("1 혹은 2를 입력하세요 :")

                    if re_or_nextHint == '1':
                        break
        
                    elif re_or_nextHint == '2':
                        Hint_num = Hint_num + 1
                        if Hint_num>3:
                            print("\n4번 힌트까지 모두 보셨습니다. 힌트는 다시 4번까지 출력해 드립니다.\n")

                            input()
                        
                        break
                    else:
                        print("잘못 입력하셨습니다. 다시 입력하세요.")
                        input()
                        continue
                continue



def spongeZa(): #사용자 입력 정답을 만들어주는 함수. 문자 a를 문자열에 추가한다.
    if num == 1:
        making_ans1("a")
    elif num == 2: 
        making_ans2("a")
    elif num == 3:
        making_ans3("a")
    

def spongeZb(): #사용자 입력 정답을 만들어주는 함수. 문자 b를 문자열에 추가한다.
    if num == 1:
        making_ans1("b")
    elif num == 2:
        making_ans2("b")
    elif num == 3:
        making_ans3("b")
        
def spongeZc(): #사용자 입력 정답을 만들어주는 함수. 문자 c를 문자열에 추가한다.
    if num == 1:
        making_ans1("c")
    elif num == 2:
        making_ans2("c")
    elif num == 3:
        making_ans3("c")


        

def making_ans1(alphabet): #사용자 문자열과 정답 문자열을 비교해 정답을 맞추었는지 판별하고 사용자에게 정답을 맞추도록 안내하는 함수
    global user_answer # 사용자가 누른 버튼으로 만들어진, 사용자 입력 정답 문자열을 저장할 변수
    global real_answer #진짜 정답 문자열

    #정답 출력시 보여줄 이미지 저장 변수들
    global spongeBob
    global spongeBob1_b
    global spongeBob2_a
    global spongeBob3_b

    #시도 횟수와 획득 점수
    global trial #주의: 앞서 텍스트 게임에서는 남은 시도횟수였으나 이미지 게임에서는 현재 시도한 횟수이다.
    global score
    global sum_score

    
    

    user_answer = user_answer + alphabet #사용자가 누른 버튼으로 문자열을 만든다.
    frame = Frame(window)

    if trial == 0 :
        score = 10
    elif trial == 1:
        score = 7
    elif trial == 2:
        score = 5
    elif trial == 3:
        score = 3
    else:
        score = 1
    
    

    if len(user_answer) == 3 and trial <= 4 :
        if user_answer == real_answer:

            sum_score = sum_score + score
            
            Label(window, text = "정답입니다! 창을 닫으면 다음 문제로 넘어갑니다. 획득한 점수 :" + str(score) + "  현재 점수: " + str(sum_score)).pack()
            spongeBoblabel = Label(frame, image = spongeBob)
            spongeBoblabel.pack(side = "left")

            spongeBob1_b_label = Label(frame, image = spongeBob1_b)
            spongeBob1_b_label.pack(side = "left")

            spongeBob2_a_label = Label(frame, image = spongeBob2_a)
            spongeBob2_a_label.pack(side = "left")

            spongeBob3_b_label = Label(frame, image = spongeBob3_b)
            spongeBob3_b_label.pack(side = "left")

            

            frame.pack()
        else:
            trial = trial + 1
            Label(window, text = "틀렸습니다! 재시도 하세요. 현재 시도 횟수: "  + str(trial) + " 남은 시도 횟수: " + str(5-trial)).pack()
            user_answer = "" #사용자 정답 초기화
    elif trial > 4: 
        Label(window, text = "기회가 모두 소진되었습니다. 다음 게임으로 넘어갑니다. 창을 닫아주세요.").pack()
        


def making_ans2(alphabet):
    global user_answer
    global real_answer
    
    global zzang
    global zzang1_c
    global zzang2_b
    global zzang3_a
    
    global trial
    global score
    global sum_score

   

    user_answer = user_answer + alphabet
    frame = Frame(window2)

    if trial == 0 :
        score = 10
    elif trial == 1:
        score = 7
    elif trial == 2:
        score = 5
    elif trial == 3:
        score = 3
    else:
        score = 1
    

    if len(user_answer) == 3 and trial <= 4 :
        if user_answer == real_answer:

            sum_score = sum_score + score
            
            Label(window2, text = "정답입니다! 창을 닫으면 다음 문제로 넘어갑니다. 획득한 점수 :" + str(score) + "  현재 점수: " + str(sum_score)).pack()
            zzanglabel = Label(frame, image = zzang)
            zzanglabel.pack(side = "left")

            zzang1_c_label = Label(frame, image = zzang1_c)
            zzang1_c_label.pack(side = "left")

            zzang2_b_label = Label(frame, image = zzang2_b)
            zzang2_b_label.pack(side = "left")

            zzang3_a_label = Label(frame, image = zzang3_a)
            zzang3_a_label.pack(side = "left")

            frame.pack()
        else:
            trial = trial + 1
            Label(window2, text = "틀렸습니다! 재시도 하세요. 현재 시도 횟수: "  + str(trial) + " 남은 시도 횟수: " + str(5-trial)).pack()
            user_answer = ""
    elif trial > 4:
        Label(window2, text = "기회가 모두 소진되었습니다. 다음 게임으로 넘어갑니다. 창을 닫아주세요.").pack()
        





def making_ans3(alphabet):
    global user_answer
    global real_answer
    
    global one
    global one1_a
    global one2_c
    global one3_c
    
    global trial
    global score
    global sum_score

    

    user_answer = user_answer + alphabet
    frame = Frame(window3)

    if trial == 0 :
        score = 10
    elif trial == 1:
        score = 7
    elif trial == 2:
        score = 5
    elif trial == 3:
        score = 3
    else:
        score = 1
    

    if len(user_answer) == 3 and trial <= 4 :
        if user_answer == real_answer:
            
            sum_score = sum_score + score
            
            Label(window3, text = "정답입니다! 창을 닫으면 최종 화면으로 넘어갑니다. 획득한 점수 :" + str(score) + "  현재 점수: " + str(sum_score)).pack()
            onelabel = Label(frame, image = one)
            onelabel.pack(side = "left")

            one1_c_label = Label(frame, image = one1_a)
            one1_c_label.pack(side = "left")

            one2_b_label = Label(frame, image = one2_c)
            one2_b_label.pack(side = "left")

            one3_a_label = Label(frame, image = one3_c)
            one3_a_label.pack(side = "left")

            frame.pack()
        else:
            trial = trial + 1
            Label(window3, text = "틀렸습니다! 재시도 하세요. 현재 시도 횟수: "  + str(trial) + " 남은 시도 횟수: " + str(5-trial)).pack()
            user_answer = ""
    elif trial > 4:
        Label(window3, text = "기회가 모두 소진되었습니다. 최종 화면으로 넘어갑니다. 창을 닫아주세요.").pack()










#main 함수


#첫번째 애니메이션
            

Quiz_1() #텍스트 퀴즈

trial = 0        

print("""\n\n\n다음 퀴즈는 지금 문제의 정답인 스펀지밥의 등장인물 캐릭터를 맞추는 문제입니다. 엔터키를 눌러주세요\n
        만약 아무것도 나오지 않는다면 새 창이 잘 떴는지 아래 작업 표시줄을 확인해 주세요.\n\n\n\n\n\n\n""")

input()


#1번문제 시작
            

score = 0

user_answer = ""
real_answer = "bab"
trial = 0            
    

window = Tk()

num = 1

#1번 눈

Label(window, text ="애니메이션 '네모바지 스펀지밥'의 주인공 스펀지밥 캐릭터를 맞춰보세요. 순서대로 클릭해야 합니다.").pack()
Label(window, text ="기회는 총 5번. 한번에 맞추면 10점, 그 이후로 7, 5, 3, 1 점 입니다.").pack()
Label(window, text ="1번. 스펀지밥의 눈은? 셋 중 하나를 클릭하세요.").pack()

frame1 = Frame(window)

spongeBob = PhotoImage(file = "spongeBob.gif")
spongeBob1_a = PhotoImage(file = "spongeBob1_a.gif")
spongeBob1_b = PhotoImage(file = "spongeBob1_b.gif")
spongeBob1_c = PhotoImage(file = "spongeBob1_c.gif")


spongeButton1_a = Button(frame1, image = spongeBob1_a, command = spongeZa)
spongeButton1_a.pack(side = "left")

spongeButton1_b = Button(frame1, image = spongeBob1_b, command = spongeZb)
spongeButton1_b.pack(side = "left")

spongeButton1_c = Button(frame1, image = spongeBob1_c, command = spongeZc)
spongeButton1_c.pack(side = "left")

frame1.pack()


#2번 다리


Label(window, text ="2번. 스펀지밥의 팔은? 셋 중 하나를 클릭하세요.").pack()

frame2 = Frame(window)

spongeBob2_a = PhotoImage(file = "spongeBob2_a.gif")
spongeBob2_b = PhotoImage(file = "spongeBob2_b.gif")
spongeBob2_c = PhotoImage(file = "spongeBob2_c.gif")

spongeButton2_a = Button(frame2, image = spongeBob2_a, command = spongeZa)
spongeButton2_a.pack(side = "left")

spongeButton2_b = Button(frame2, image = spongeBob2_b, command = spongeZb)
spongeButton2_b.pack(side = "left")

spongeButton2_c = Button(frame2, image = spongeBob2_c, command = spongeZc)
spongeButton2_c.pack(side = "left")

frame2.pack()


#3번 다리


Label(window, text ="3번. 스펀지밥의 다리는? 셋 중 하나를 클릭하세요.").pack()

frame3 = Frame(window)

spongeBob3_a = PhotoImage(file = "spongeBob3_a.gif")
spongeBob3_b = PhotoImage(file = "spongeBob3_b.gif")
spongeBob3_c = PhotoImage(file = "spongeBob3_c.gif")

spongeButton3_a = Button(frame3, image = spongeBob3_a, command = spongeZa)
spongeButton3_a.pack(side = "left")

spongeButton3_b = Button(frame3, image = spongeBob3_b, command = spongeZb)
spongeButton3_b.pack(side = "left")

spongeButton3_c = Button(frame3, image = spongeBob3_c, command = spongeZc)
spongeButton3_c.pack(side = "left")

frame3.pack()
    

window.mainloop()









#두번째 애니메이션


Quiz_2()

trial = 0        

print("""\n\n\n다음 퀴즈는 지금 문제의 정답인 짱구의 등장인물 캐릭터를 맞추는 문제입니다. 엔터키를 눌러주세요\n
        만약 아무것도 나오지 않는다면 새 창이 잘 떴는지 아래 작업 표시줄을 확인해 주세요.\n\n\n\n\n\n\n""")
input()



#2번문제 시작


user_answer = ""
real_answer = "cba"
trial = 0



window2 = Tk()

num = 2

#1번 얼굴

Label(window2, text ="애니메이션 짱구의 등장인물 중 하나인 짱구 아버지 신형만 캐릭터를 맞춰보세요. 순서대로 클릭해야 합니다.").pack()
Label(window2, text ="기회는 총 5번. 한번에 맞추면 10점, 그 이후로 7, 5, 3, 1 점 입니다.").pack()
Label(window2, text ="1번. 신형만의 얼굴은? 셋 중 하나를 클릭하세요.").pack()

frame1 = Frame(window2)

zzang = PhotoImage(file = "zzang.gif")
zzang1_a = PhotoImage(file = "zzang1_a.gif")
zzang1_b = PhotoImage(file = "zzang1_b.gif")
zzang1_c = PhotoImage(file = "zzang1_c.gif")


zzangButton1_a = Button(frame1, image = zzang1_a, command = spongeZa)
zzangButton1_a.pack(side = "left")

zzangButton1_b = Button(frame1, image = zzang1_b, command = spongeZb)
zzangButton1_b.pack(side = "left")

zzangButton1_c = Button(frame1, image = zzang1_c, command = spongeZc)
zzangButton1_c.pack(side = "left")

frame1.pack()


#2번 다리


Label(window2, text ="2번. 신형만의 상체는? 셋 중 하나를 클릭하세요.").pack()

frame2 = Frame(window2)

zzang2_a = PhotoImage(file = "zzang2_a.gif")
zzang2_b = PhotoImage(file = "zzang2_b.gif")
zzang2_c = PhotoImage(file = "zzang2_c.gif")

zzangButton2_a = Button(frame2, image = zzang2_a, command = spongeZa)
zzangButton2_a.pack(side = "left")

zzangButton2_b = Button(frame2, image = zzang2_b, command = spongeZb)
zzangButton2_b.pack(side = "left")

zzangButton2_c = Button(frame2, image = zzang2_c, command = spongeZc)
zzangButton2_c.pack(side = "left")

frame2.pack()


#3번 다리


Label(window2, text ="3번. 신형만의 다리는? 셋 중 하나를 클릭하세요.").pack()

frame3 = Frame(window2)

zzang3_a = PhotoImage(file = "zzang3_a.gif")
zzang3_b = PhotoImage(file = "zzang3_b.gif")
zzang3_c = PhotoImage(file = "zzang3_c.gif")

zzangButton3_a = Button(frame3, image = zzang3_a, command = spongeZa)
zzangButton3_a.pack(side = "left")

zzangButton3_b = Button(frame3, image = zzang3_b, command = spongeZb)
zzangButton3_b.pack(side = "left")

zzangButton3_c = Button(frame3, image = zzang3_c, command = spongeZc)
zzangButton3_c.pack(side = "left")

frame3.pack()



window2.mainloop()









#세번째 애니메이션


Quiz_3()

trial = 0        

print("""\n\n\n다음 퀴즈는 지금 문제의 정답인 원피스의 등장인물 캐릭터를 맞추는 문제입니다. 엔터키를 눌러주세요\n
        만약 아무것도 나오지 않는다면 새 창이 잘 떴는지 아래 작업 표시줄을 확인해 주세요.\n\n\n\n\n\n\n""")

input()


#3번문제 시작


user_answer = ""
real_answer = "acc"
trial = 0



window3 = Tk()

num = 3

#1번 얼굴

Label(window3, text ="애니메이션 원피스 캐릭터 중 하나인 쵸파 캐릭터를 맞춰보세요. 순서대로 클릭해야 합니다.").pack()
Label(window3, text ="기회는 총 5번. 한번에 맞추면 10점, 그 이후로 7, 5, 3, 1 점 입니다.").pack()
Label(window3, text ="1번. 쵸파의 눈은? 셋 중 하나를 클릭하세요.").pack()

frame1 = Frame(window3)

one = PhotoImage(file = "one.gif")
one1_a = PhotoImage(file = "one1_a.gif")
one1_b = PhotoImage(file = "one1_b.gif")
one1_c = PhotoImage(file = "one1_c.gif")


oneButton1_a = Button(frame1, image = one1_a, command = spongeZa)
oneButton1_a.pack(side = "left")

oneButton1_b = Button(frame1, image = one1_b, command = spongeZb)
oneButton1_b.pack(side = "left")

oneButton1_c = Button(frame1, image = one1_c, command = spongeZc)
oneButton1_c.pack(side = "left")

frame1.pack()


#2번 다리


Label(window3, text ="2번. 쵸파의 모자는? 셋 중 하나를 클릭하세요.").pack()

frame2 = Frame(window3)

one2_a = PhotoImage(file = "one2_a.gif")
one2_b = PhotoImage(file = "one2_b.gif")
one2_c = PhotoImage(file = "one2_c.gif")

oneButton2_a = Button(frame2, image = one2_a, command = spongeZa)
oneButton2_a.pack(side = "left")

oneButton2_b = Button(frame2, image = one2_b, command = spongeZb)
oneButton2_b.pack(side = "left")

oneButton2_c = Button(frame2, image = one2_c, command = spongeZc)
oneButton2_c.pack(side = "left")

frame2.pack()


#3번 다리


Label(window3, text ="3번. 쵸파의 손은? 셋 중 하나를 클릭하세요.").pack()

frame3 = Frame(window3)

one3_a = PhotoImage(file = "one3_a.gif")
one3_b = PhotoImage(file = "one3_b.gif")
one3_c = PhotoImage(file = "one3_c.gif")

oneButton3_a = Button(frame3, image = one3_a, command = spongeZa)
oneButton3_a.pack(side = "left")

oneButton3_b = Button(frame3, image = one3_b, command = spongeZb)
oneButton3_b.pack(side = "left")

oneButton3_c = Button(frame3, image = one3_c, command = spongeZc)
oneButton3_c.pack(side = "left")

frame3.pack()



window3.mainloop()



print("엔터를 누르면 최종화면이 뜹니다!")
input()

print("")
print("                                                                  o o o o o o o o o         ")
print("                                                                 o                  o       ")
print("                                                                o   o o o o o o o    o      ")
print("                                                               o   o o         o  o   o     ")
print("                                                              o   o   o       o    o   o    ")
print("                                                              o  o     o     o ⯑   o  o     ")
print("                                                              o  o⯑    o   o       o  o     ")
print("                                                              o  o       o o        o  o     ")
print("                                                              o  o   ⯑   o         o  o     ")
print("                                                              o  o      o   o       o  o     ")
print("                                                              o  o     o     o      o  o     ")
print("                                                              o  o    o       o     o  o     ")
print("                                                              o  o   o   ⯑    o    o  o     ")
print("                                                               o  o o           o  o  o      ")
print("                                                                o    o o o o o o o   o       ")
print("                                                                 o                  o        ")           
print("                                                                  o o o o o o o o o          ")

print("                                                                      <하얀피자>")



print(f"""\n\n\n                                                          축하합니다! 게임을 클리어하셨습니다.\n
                                                       총 획득한 점수는 {sum_score} 점 입니다. 수고하셨습니다^^!""")

print("\n\n\n\n                                       *   알고리즘과 게임컨텐츠 1분반 11조(하얀피자) 김혜린 장예진 주영주 최영은  * \n\n")


input()
input()
input()
            
            

    

    

    
