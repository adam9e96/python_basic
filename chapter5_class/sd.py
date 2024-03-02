class Shop:
    total = 0
    menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]

    @classmethod
    def sales(cls, product: str, amount: int) -> None:
        for i in cls.menu_list:
            if product in i: # 제품 이름이 딕셔너리의 키에 해당하는지 확인
                cls.total += i[product] * amount

    @classmethod
    def sales_info(cls):
        print(cls.total)


Shop.sales('떡볶이', 1)  # 떡볶이를 1개 판매 3000 *1
Shop.sales('김밥', 2)  # 김밥을 2개 판매 2000 * 2
Shop.sales('튀김', 5)  # 튀김을 5개 판매 500 * 5  => 9500
Shop.sales_info()

# print(Shop.menu_list[1].values())