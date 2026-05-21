import seat

if __name__ == '__main__':
    grade = input('회원 등급을 입력하세요(준회원/정회원/우수회원) : ')
    if seat.check_membership(grade):  # 함수 호출
        seat_number = int(input('좌석 번호를 입력하세요 : '))
        seat.reserve_seat(seat_number) # 함수 호출

