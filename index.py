import random
import time

def roll_dice():
    """1부터 6까지의 무작위 주사위 눈을 반환합니다."""
    return random.randint(1, 6)

def main():
    print("========================================")
    print(" 🎲 파이썬 주사위 대결 게임에 오신 것을 환영합니다! 🎲")
    print("========================================")
    
    player_score = 0
    computer_score = 0
    round_count = 1

    while True:
        print(f"\n[ 라운드 {round_count} ]")
        input("👉 주사위를 던지려면 [Enter] 키를 누르세요...")
        
        # 플레이어 주사위 던지기
        print("\n주사위를 굴리는 중입니다...")
        time.sleep(0.5)
        player_dice = roll_dice()
        print(f"👤 플레이어의 주사위 눈: {player_dice}")
        
        # 컴퓨터 주사위 던지기
        time.sleep(0.5)
        computer_dice = roll_dice()
        print(f"🤖 컴퓨터의 주사위 눈: {computer_dice}")
        
        # 승패 판정
        print("----------------------------------------")
        if player_dice > computer_dice:
            print("🎉 플레이어가 이겼습니다!")
            player_score += 1
        elif player_dice < computer_dice:
            print("💻 컴퓨터가 이겼습니다!")
            computer_score += 1
        else:
            print("🤝 비겼습니다!")
            
        print(f"📊 현재 스코어 -> 플레이어: {player_score} 점 | 컴퓨터: {computer_score} 점")
        print("----------------------------------------")
        
        # 계속 여부 확인
        keep_going = input("한 판 더 하시겠습니까? (y/n): ").strip().lower()
        if keep_going != 'y':
            print("\n========================================")
            print("게임이 종료되었습니다.")
            print(f"🏆 최종 스코어 - 플레이어: {player_score} 점 / 컴퓨터: {computer_score} 점")
            
            if player_score > computer_score:
                print("🥇 최종 승리자: 플레이어! 축하합니다!")
            elif player_score < computer_score:
                print("🥈 최종 승리자: 컴퓨터! 다음 기회에 도전하세요.")
            else:
                print("🤝 최종 결과: 무승부입니다!")
            print("========================================")
            break
            
        round_count += 1

if __name__ == "__main__":
    main()