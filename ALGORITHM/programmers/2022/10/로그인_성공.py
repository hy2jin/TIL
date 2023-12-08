def solution(id_pw, db):
    ans = ["wrong pw", "fail"]
    idx = -1
    for a, b in db:
        if a == id_pw[0]:
            if b == id_pw[1]:
                return "login"
            else:
                idx = 0
        elif idx < 0:
            idx = 1
    return ans[idx]