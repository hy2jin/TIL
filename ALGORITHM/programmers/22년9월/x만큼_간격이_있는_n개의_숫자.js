function solution(x, n) {
  const ans = []
  for (let i = 1; i <= n; i++) {
      ans.push(x*i)
  }
  return ans
}