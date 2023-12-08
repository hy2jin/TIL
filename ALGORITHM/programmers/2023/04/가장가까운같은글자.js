function solution(s) {
  const ans = new Array(s.length).fill(-1)
  const obj = {}
  for (let i = 0; i < s.length; i++) {
    if (s[i] in obj) ans[i] = i - obj[s[i]]
    obj[s[i]] = i
  }
  return ans
}