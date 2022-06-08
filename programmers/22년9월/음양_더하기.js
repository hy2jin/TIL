function solution(absolutes, signs) {
    let ans = 0
    for (i in signs) {
        if (signs[i]) ans += absolutes[i]
        else ans -= absolutes[i]
    }
    return ans
}

function solution(absolutes, signs) {
    let ans = 0
    absolutes.forEach((v, i) => {
        if (signs[i]) ans += v
        else ans -= v
    })
    return ans
}