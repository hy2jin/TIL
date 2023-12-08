function solution(n) {
  let ans = 0
  while (n > 0) {
      ans += n % 10
      n = parseInt(n / 10)
  }
  return ans
}

function solution2(n) {
  let arr = (n+"").split("")
  return arr.reduce((acc, cur) => acc + parseInt(cur), 0)
}