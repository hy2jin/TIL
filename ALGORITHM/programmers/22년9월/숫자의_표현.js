// 수학으로 접근해야 효율성 검사 통과
// 파이썬과 같이 풀면 효율성 검사 실패함

function solution(n) {
  let ans = 0
  for (i = 1; i <= n; i += 2) {
      if (n % i === 0) {
          ans++
      }
  }
  return ans
}