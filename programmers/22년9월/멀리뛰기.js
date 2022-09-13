function solution(n) {
  if (n < 4) return n;
  let a = 1
  let b = 1
  for (i = 0; i < n; i++) {
      let tmp = a
      a = b
      b = (tmp + b) % 1234567
  }
  return a
}