def reserve_seat(seat_number):
    print(f'{seat_number}번 좌석 예약이 완료되었습니다!')

def check_membership(grade):
    if grade == '정회원' or grade == '우수회원':
        print('좌석 예약 권한 확인 환료!')
        return True
    else:
        print('좌석 예약 권한 없음!')
        return False
    
print(__name__)
if __name__ == '__main__':
    grade = input('회원 등급을 입력하세요(준회원/정회원/우수회원) : ')
    print(__name__)
    if check_membership(grade):  # 함수 호출
        seat_number = int(input('좌석 번호를 입력하세요 : '))
        reserve_seat(seat_number) # 함수 호출

# grade = input('회원 등급을 입력하세요(준회원/정회원/우수회원) : ')
# print(__name__)
# if check_membership(grade):  # 함수 호출
#     seat_number = int(input('좌석 번호를 입력하세요 : '))
#     reserve_seat(seat_number) # 함수 호출

