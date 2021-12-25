def count_minimum_change(change: int):
    res = [{'sum': 0}, {'change': change}]
    if res[1]['change'] > 0:
        coin_cal(res, coin_type=500)
    if res[1]['change'] > 0:
        coin_cal(res, coin_type=100)
    if res[1]['change'] > 0:
        coin_cal(res, coin_type=50)
    if res[1]['change'] > 0:
        coin_cal(res, coin_type=10)
    print(res[0]['sum'])


def coin_cal(args, coin_type):
    coin_count = args[1]['change'] // coin_type
    args[0]['sum'] += coin_count
    args[1]['change'] -= coin_count * coin_type


count_minimum_change(change=1200)
