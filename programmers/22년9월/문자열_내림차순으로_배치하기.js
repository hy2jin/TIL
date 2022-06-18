function solution(s) {
  const arr = s.split("")
  arr.sort().reverse()
  return arr.reduce((acc, cur) => acc+cur, "")
}

function solution(s) {
  return s.split("").sort().reverse().join("")
}