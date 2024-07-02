import random

def up_and_down_game():
    print("뚜뚜뚜 뚜뚜뚜 뚜루두루 뚜뚜뚜(대충 오징어 게임 노래)")
    print("이번 게임은 Up and Down 게임입니다.")
    print("통과한다면 다음 라운드에 진출할수 있습니다.")

up_and_down_game()
random_number = random.randint(1, 100)
max_attemps = 5
attemps = 0

while True:

    # 시도 횟수 체크
    attemps += 1
    if max_attemps < attemps:
        print(f"탈락하였습니다. 정답은 {random_number} 였습니다")

        choice = input("다시 시도하시겠습니까? (y/n): ")
        if choice == "y":
            # 시도 횟수 초기화
            attemps = 0
            random_number = random.randint(1, 100)
            continue
        else:
            print("게임을 종료합니다.")
            break

    else:
        player = int(
            input(
                f"1에서 100까지의 숫자를 입력하세요!. 기회는 {max_attemps - attemps} 번:"
            )
        )

        if player > random_number:
            print("Down")

        elif player < random_number:
            print("Up")

        else:
            print("이번 라운드 통과 하였습니다")
            break