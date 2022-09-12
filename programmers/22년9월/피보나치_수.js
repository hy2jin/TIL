function solution(n) {
  if (n < 2) return n;
  let a = 0
  let b = 1
  for (i = 1; i <= n; i++) {
      tmp = a
      a = b
      b = (tmp + b) % 1234567
  }
  return a
}