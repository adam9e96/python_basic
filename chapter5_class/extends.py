class Person:  # 슈퍼 클래스
    def __init__(self, name: str):
        self.name = name

    def eat(self, food: str) -> None:
        print(f'{self.name}가 {food}를 먹습니다.')


class Student(Person):  # 서브 클래스
    def __init__(self, name: str, school: str) -> None:
        super().__init__(name)  # 슈퍼 클래스의 생성자 실행    # 부모 클래스의 생성자를 이용해서 name 을 넘겨줌
        self.school = school

    def study(self) -> None:
        print(f'{self.name}는 {self.school}에서 공부를 합니다.')


person1 = Person('김홍도')
person1.eat('바나나')  # 출력 : 김홍도가  바나나를 먹습니다.

potter = Student('해리포터', '호그와트')
potter.eat('감자')  # 출력 : 해리포터가 감자를 먹습니다.    # 부모 클래스의 메소드 실행

potter.study()  # 출력 : 해리포터는 호그와트에서 공부를 합니다.    # 자식 클래스의 메소드 실행


# 파이썬은 다중 상속도 가능하다.

class Computer:  # 슈퍼 클래스
    def __init__(self):
        print('슈퍼 클래스의 생성자가 실행되었습니다.')


class NoteBook(Computer):  # 서브 클래스
    def __init__(self):
        super().__init__()
        print('서브 클래스의 생성자가 실행되었습니다.')


N = NoteBook()
# 출력
# 슈퍼 클래스의 생성자가 실행되었습니다.
# 서브 클래스의 생성자가 실행되었습니다.


print(isinstance(potter, Student))  # 출력 : True
print(isinstance(potter, Person))  # 출력 : True


# 4. 서브 클래스의 인스턴스 자료형 활용
# 원두(bean) 을 저장하는 Coffee 클래스와 원두(bean)에 물을 섞은 Espresso 클래스를 상속

class Coffee:  # 슈퍼 클래스
    def __init__(self, bean: str):
        self.bean = bean

    def coffee_info(self):
        print(f'원두 : {self.bean}')


class Espresso(Coffee):  # 서브 클래스
    def __init__(self, bean: str, water: str):
        super().__init__(bean)  # 슈퍼 클래스의 생성자 실행
        self.water = water

    def espresso_info(self):
        super().coffee_info()  # 슈퍼 클래스의 메서드 실행
        print(f'물: {self.water}ml')

class Americano(Espresso):
    def __init__(self, bean: str, water: str, more_water: str):
        super().__init__(bean, water)
        # super() 대신에 클래스명도 사용가능하지만 self를 써야되서 잘 안씀
        # Espresso.__init__(self, bean,water) # 클래스 이름으로 접근도 가능. 객체를 매개 변수로 전달
        self.more_water = more_water

    def americano_info(self):
        super().espresso_info()  # 슈퍼 클래스의 메서드 실행
        # Espresso.espresso_info(self)  # 클래스 이름으로 실행을 할 경우에는 객체를 매개 변수로 전달
        print(f'물 더 : {self.more_water}ml')


coffee = Espresso('콜롬비아', '30')
coffee.espresso_info()
# 원두 : 콜롬비아
# 물: 30ml
print()

coffee = Americano('파나마', '20', '200')
coffee.americano_info()
# 원두 : 파나마
# 물: 20ml
# 물 더 : 200ml
print()

Espresso.espresso_info(coffee)  # 인스턴스 메서드이지만 클래스 이름으로 호출 가능. 대신 객체를 매개 변수 self 로 전달해야함
# 객체를 매개변수 SELF 를 이용해 전달도 가능하다.


# 문제
