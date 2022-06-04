function solution(n) {
  n = String(n).split("")
  n.sort((a, b) => b - a)
  let ans = n.reduce((acc, cur) => acc + cur, "")
  return parseInt(ans)
}

function solution(n) {
  let arr = []
  while (n > 0) {
      arr.push(n % 10)
      n = parseInt(n / 10)
  }
  arr.sort((a, b) => b - a)
  return arr.join("")*1
}