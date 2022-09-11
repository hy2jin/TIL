function solution(n, m) {
  const max = Math.max(n, m)
  const min = n + m - max
  const funcGcd = (a, b) => a % b === 0 ? b : funcGcd(b, a%b)
  const gcd = funcGcd(max, min)
  return [gcd, n*m/gcd]
}