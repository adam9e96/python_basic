# 클래스의 메서드 사용
import sample_class
sample_class.PrintTxt.print_greet() # 출력 : hello class


# 클래스의 메서드 사용
from sample_class import PrintTxt
PrintTxt.print_greet()     # 출력 : hello class

# 모듈의 함수 사용
import sample_module
sample_module.print_greet() # 출력 : hello module

# 파이썬에서는 클래스보다는 모듈을 더 많이 사용함. 차이도 없기도 하고
# 사용예시를 봐도 큰 차이가 안보인다.