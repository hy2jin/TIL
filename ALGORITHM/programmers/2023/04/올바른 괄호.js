function solution(s){
  let chk = 0
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') chk += 1
    else chk -= 1
    if (chk < 0) return false
  }
  return chk === 0
}