# MILES, POUND는 단위 변환에서 사용하는 변수 (파이썬에는 상수 단위는 없지만 그렇게 보이려고 대문자를 사용했음)
MILES = 0.621371
POUND = 0.00220462


def kilometer_to_miles(kilometer: int | float) -> float:
    """킬로미터를 마일로 변환"""
    return kilometer * MILES


def gram_to_pounds(gram: int | float) -> float:
    """그램을 파운드로 변환하는 함수"""
    return gram * POUND
