def solution(coupon):
    ans = 0
    while coupon > 9:
        service, coupon = divmod(coupon, 10)
        ans += service
        coupon += service
    return ans