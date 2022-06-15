function solution(x) {
  let num = 0
  for (i of String(x)) num += Number(i)
  // return x % num ? false : true
  return !(x%num)
}