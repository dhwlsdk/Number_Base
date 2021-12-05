def take_guess():
    print("숫자를 맞출 차례입니다. 숫자를 한 개씩 입력해주세요")

    result_num = []

    for i in range(1, 5):
        num = int(input("{}번째 숫자를 입력하세요: ".format(i)))
        while True:
            if num in result_num:
                print("중복되는 숫자입니다. 다시 입력하세요")
                num = int(input("{}번째 숫자를 입력하세요: ".format(i)))
            else:
                result_num.append(num)
                break

        while True:
            if int(num) < 0 or int(num) >= 10:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
                num = input("{}번째 숫자를 입력하세요: ".format(i))
            else:
                break

    guess_num = ''
    for i in result_num:
        guess_num += str(i)

    return guess_num


def get_score(guess_num, answer_num):
    strike = 0
    ball = 0

    while True:
        for i in range(4):
            if guess_num[i] == answer_num[i]:
                strike += 1
            elif guess_num[i] in answer_num and guess_num[i] != answer_num[i]:
                ball += 1
        else:
            break

    return strike, ball


if __name__ == '__main__':
    print("숫자를 뽑을 차례입니다. 4자리 숫자를 입력해주세요")
    answer_num = input("정답 숫자를 입력해주세요: ")

    while True:
        if len(answer_num) != 4:
            print("4자리 숫자가 아닙니다. 다시 입력하세요")
            answer_num = input("정답 숫자를 입력해주세요: ")
        else:
            break

    while True:
        if answer_num[0] != answer_num[1] != answer_num[2] != answer_num[3]:
            break
        else:
            print("중복되는 숫자가 있습니다. 다시 입력하세요")
            answer_num = input("정답 숫자를 입력해주세요: ")

    Round = 1
    guess_num = take_guess()
    strike, ball = get_score(guess_num, answer_num)

    while True:
        print("{}R:\n{}S{}B".format(Round, strike, ball))
        if strike != 4:
            Round += 1
            guess_num = take_guess()
            strike, ball = get_score(guess_num, answer_num)
        else:
            print("축하합니다! 정답을 {}번만에 맞추셨습니다".format(Round))
            break

