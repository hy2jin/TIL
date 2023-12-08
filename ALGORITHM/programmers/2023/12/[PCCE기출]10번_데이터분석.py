def solution(data, ext, val_ext, sort_by):
    dic = { 'code': 0, 'date': 1, 'maximum': 2, 'remain': 3 }

    result = []
    for da in data:
        if da[dic[ext]] < val_ext:
            result.append(da)

    result.sort(key=lambda x:x[dic[sort_by]])
    return result
