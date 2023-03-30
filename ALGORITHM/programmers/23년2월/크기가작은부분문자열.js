function solution(t, p) {
    let ans = 0;
    for (let i = 0; i <= t.length - p.length; i++) {
        let n = t.slice(i, i+p.length)
        if (Number(n) <= Number(p)) ans++
    }
    return ans
}