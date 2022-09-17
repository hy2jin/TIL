function solution(a, b) {
  let ans = 0
  a.forEach((v, i) => ans += v * b[i])
  return ans
}

function solution(a, b) {
  return a.reduce((acc, _, i) => acc + a[i]*b[i], 0)
}