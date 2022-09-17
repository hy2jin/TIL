function solution(num) {
  for (i = 0; i < 500; i++) {
      if (num === 1) return i
      num % 2 ? num = num * 3 + 1 : num /= 2
  }
  return -1
}