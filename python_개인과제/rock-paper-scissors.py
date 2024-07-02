import random



choices = ["가위", "바위", "보"]

def winner(player,computer):
    if player == computer:
        return "무"
    elif (player == "가위" and computer == "보") or \
            (player == "바위" and computer == "가위") or \
            (player == "보" and computer == "바위"):
        return "통과하셨습니다"
    else:
        return "탈락하였습니다"


def play_game():
    print("이번 라운드는 가위, 바위, 보 게임입니다!")
    while True:
        # 사용자 입력 받기
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

        if user_choice not in choices:
            print("잘못된 선택입니다. 다시 시도해주세요.")
            continue

        computer_choice = random.choice(choices)
        print(f"컴퓨터의 선택: {computer_choice}")


        result = winner(user_choice, computer_choice)
        print(result)


        play_again = input("다시 플레이하시겠습니까? (예/아니오):")
        if play_again != "예":
            print("게임을 종료합니다. 감사합니다!")
            break
play_game()