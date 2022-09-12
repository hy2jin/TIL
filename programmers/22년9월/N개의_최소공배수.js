function solution(arr) {
  // 최대공약수
  const gcd = (a, b) => {
      if (a > b) {
          const tmp1 = a
          a = b
          b = tmp1
      }
      while (a > 0) {
          const tmp2 = b
          b = a
          a = tmp2 % b
      }
      return b
  }
  // 최소공배수
  let lcm = arr[0]
  arr.map(n => lcm = lcm*n/gcd(lcm,n))
  return lcm
}