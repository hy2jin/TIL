function solution(s) {
  const L = s.length
  if (L % 2) return 0                                           // 두개씩 제거되니까 홀수는 실패

  const stack = []
  for (let i = 0; i < L; i++) {
      if (stack.length === 0) stack.push(s[i])                  // 스택이 비어있으면 추가
      else if (s[i] === stack[stack.length - 1]) stack.pop()    // 스택의 마지막과 같으면 제거
      else stack.push(s[i])                                     // 스택의 마지막과 다르면 추가
  }

  return stack.length > 0 ? 0 : 1                               // 아직 스택에 값이 있으면 실패 없으면 성공
}
