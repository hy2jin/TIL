function solution(number) {
  let ans = 0;
  const N = number.length;
  for (let i = 0; i < N - 2; i++) {
      for (let j = i + 1; j < N - 1; j++) {
          for (let k = j + 1; k < N; k++) {
              if (number[i] + number[j] + number[k] === 0) ans++
          }
      }
  }
  return ans
}