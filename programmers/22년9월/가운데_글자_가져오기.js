function solution(s) {
  let i = parseInt(s.length/2)
  return s.length % 2 ? s[i] : s[i-1] + s[i]
}