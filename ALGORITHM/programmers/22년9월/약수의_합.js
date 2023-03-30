function solution(n) {
  let ans = 0
  for (i = 1; i <= n**0.5; i++) {
      if (n % i === 0) {
          ans += i
          if (i*i !== n) {
              ans += n/i
          }
      }
  }
  return ans
}