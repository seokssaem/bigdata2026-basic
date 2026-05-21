def book_movie(title):
    print(f"🎬{title} 예매가 완료되었습니다!")

def check_age(age):
    if age >= 15:
        print('관람 가능!')
        return True
    else:
        print('보지마!!!!')
        return False
    
if __name__ == "__main__":
    age = int(input('나이 입력?? : '))
    if check_age(age):
        title = input('영화 제목?? : ')
        book_movie(title)