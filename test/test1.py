# menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]
# # # 리스트안에 딕셔너리가 있음
# #
# # # 모든 value를 저장할 빈 리스트 생성
# # prices = []
# #
# # # 각 딕셔너리에 대해 반복
# # for item in menu_list:
# #     # 딕셔너리의 value 추출하여 prices 리스트에 추가
# #     for value in item.values():
# #         prices.append(value)
# #
# # # 결과 출력
# # print(prices[0])
# #
# # print(menu_list[0].values())
# # print(menu_list[1].values())
# # # print(menu_list[2].values())
# #
# # prices = []
# # for item in menu_list:
# #     print(item)  # 테스트
# #     for value in item.values():
# #         prices.append(value)
# # print(prices[1])
#
# prices = []
# for item in menu_list:
#     # print(item)  # 테스트
#     for value in item.keys():
#         # print(value)
#         prices.append(value)
# print(prices[1])
#     # if item.keys() == "떡복기":
#     #     print('1')
#
# prices = []
# for item in menu_list:
#     # print(item)  # 테스트
#     for value in item.values():
#         prices.append(value)
#
# print(prices[1])

class Shop:
    total = 0  # 클래스 변수
    menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]

    @classmethod
    def sales(cls, product: str, amount: int) -> None:
        for item in cls.menu_list:
            if product in item:  # 제품 이름이 딕셔너리의 키와 일치하는지 확인
                cls.total += item[product] * amount  # 해당 제품의 가격을 총액에 추가

    @classmethod
    def sales_info(cls):  # 클래스 메소드로 변경
        print(cls.total)  # 클래스 변수에 접근

# 제품 판매
Shop.sales('떡볶이', 1)  # 떡볶이를 1개 판매
Shop.sales('김밥', 2)  # 김밥을 2개 판매
Shop.sales('튀김', 5)  # 튀김을 5개 판매

# 판매 정보 출력
Shop.sales_info()

