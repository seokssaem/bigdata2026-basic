def enter_gym(name):
    print(f"💪{name}님, 입장을 환영합니다!")


def check_membership(membership):
    if membership == '유효':
        print('입장 가능!')
        return True
    else:
        print('회원권 없음')
        return False

if __name__ == "__main__":
    membership = input('회원권 상태(유효/만료):')
    if check_membership(membership):
        name = input('이름?? :')
        enter_gym(name)