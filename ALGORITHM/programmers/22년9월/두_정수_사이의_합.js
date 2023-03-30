function solution(a, b) {
  let ans = 0
  for (i = Math.min(a, b); i <= Math.max(a, b); i++) ans += i
  return ans
}