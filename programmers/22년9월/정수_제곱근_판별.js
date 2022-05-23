function solution(n) {
  const x = n**0.5
  return x === parseInt(x) ? (x+1)**2 : -1
}