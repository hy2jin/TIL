def makeDateNum(date):
    y, m, d = map(int, date.split('.'))
    return d + (m * 28) + (y * 12 * 28)

def solution(today, terms, privacies):
    today = makeDateNum(today)
    dic = {}
    for t in terms:
        k, v = t.split()
        dic[k] = int(v) * 28
    ans = []
    for i in range(len(privacies)):
        date, k = privacies[i].split()
        date = makeDateNum(date) + dic[k]
        if today >= date:
            ans.append(i + 1)
    return ans