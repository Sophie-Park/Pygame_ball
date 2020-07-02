#  일반 가격 
def price(ppl):
    print("{0} 명 가격은 {1} 원 입니다.".format(ppl, ppl * 10000))

# 조조 할인 가격
def price_morning(ppl):
    print("{0} 명 조조 할인 가격은 {1} 원 입니다.".format(ppl, ppl * 6000))

# 군인 할인 가격
def price_soldier(ppl):
    print("{0} 명 군인 할인 가격은 {1} 원 입니다.".format(ppl, ppl * 4000))