function solution(s) {
  if (s.length !== 4 && s.length !== 6) return false
  for (w of s) {
      if (isNaN(w)) return false
  }
  return true
}

// isNaN() 안에 숫자가 아닌 값 넣으면 false, 숫자면 true