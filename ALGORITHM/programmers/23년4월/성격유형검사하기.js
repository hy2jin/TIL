function solution(survey, choices) {
  const obj = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 }
  let k, v
  for (let i = 0; i < survey.length; i++) {
    k = choices[i] < 4 ? survey[i][0] : survey[i][1]
    v = Math.abs(choices[i] - 4)
    obj[k] += v
  }
  let ans = ''
  ans += obj['T'] > obj['R'] ? 'T' : 'R'
  ans += obj['F'] > obj['C'] ? 'F' : 'C'
  ans += obj['M'] > obj['J'] ? 'M' : 'J'
  ans += obj['N'] > obj['A'] ? 'N' : 'A'
  return ans
}
