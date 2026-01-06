# 커다란 뼈대 잡고 안쪽에 빈칸 채우기
# 동시에 여러개 수정 Ctrl d

balance = 0  # 잔액
history = []  # 거래내역

# {
#     "type" = "", #"Deposite", "Withdraw"
#     "amount" = 0,
#     "balance" = 0
# }

while True:
    print(
        """
          ===ATM MENU===
          1. 잔액 조회
          2. 입금
          3. 출금
          4. 거래내역 조회
          0. 종료
          ================
          """
    )
    a = input("메뉴를 선택하세요:")  # 이렇게 입력받으면 문자열로 들어옴
    print(a)

    if a == "0":
        print("===프로그램 종료===")
        break

    elif a == "1":
        print("===잔액 조회===")
        print(f"현재 잔액: {balance}원")
    elif {balance} == 0:
        break

    elif a == "2":
        print("===입금===")
        amount = int(input("입금액을 입력하세요: "))
        if amount <= 0:
            print("오류: 1이상 정수 입력하세요")
            continue
        balance += amount
        # 거래내역 쌓기
        data = {"type": "입금", "amount": amount, "balance": balance}
        history.append(data)

    elif a == "3":
        print("===출금===")
        print(f"현재잔액: {balance}원")
        amount = int(input("출금액을 입력하세요: "))
        if amount <= 0:
            print("오류: 1이상 정수 입력하세요")
            continue
        elif amount > balance:
            print("잔액 부족")
            continue
        balance -= amount
        print(f"[출금 완료] 현재 잔액 {balance - amount}")
        data = {"type": "출금", "amount": amount, "balance": balance}
        history.append(data)

    elif a == "4":
        print("===거래내역 조회===")
        for h in history:
            print(f"[{h["type"]}] 금액: {h["amount"]}원 잔액: {h["balance"]}")
            # 최신순으로 출력하는 방법 1. 최신을 앞에 추가하기 2. 받고 뒤집어 range(인덱스 -1)
