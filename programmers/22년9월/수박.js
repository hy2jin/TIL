function solution(n) {
  let ans = ""
  for (i = 1; i <= n; i++) {
      if (i % 2) ans += "수"
      else ans += "박"
  }
  return ans
}