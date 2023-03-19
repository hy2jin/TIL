function solution(a, b, n) {
  let ans = 0
  let give, take, tmp
  while (n >= a) {
      tmp = parseInt(n / a)
      give = tmp * a
      take = tmp * b
      n = n - give + take
      ans += take
  }
  return ans
}