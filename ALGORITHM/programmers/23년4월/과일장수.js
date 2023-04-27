function solution(k, m, score) {
  score.sort((a, b) => b - a)
  let ans = 0
  for (let i = 0; i < score.length; i += m) {
    const j = i + m - 1
    if (j >= score.length) break
    ans += score[j] * m
  }
  return ans
}
