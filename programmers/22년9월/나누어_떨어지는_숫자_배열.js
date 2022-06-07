function solution(arr, divisor) {
  const ans = []
  for (n of arr) {
      if (n % divisor === 0) ans.push(n)
  }
  ans.sort((a, b) => a - b)
  return ans.length ? ans : [-1]
}

function solution(arr, divisor) {
  const ans = arr.filter(n => n % divisor === 0)
  return ans.length ? ans.sort((a, b) => (a - b)) : [-1]
}