// const noNum = (n) => {
//   return (n % 3 === 0) || String(n).includes('3')
// }

// function solution(n) {
//   const ans = new Array(n + 1).fill(0)
//   for (let i = 1; i < n + 1; i++) {
//     let tmp = ans[i - 1] + 1
//     while (noNum(tmp)) {
//       tmp += 1
//     }
//     ans[i] = tmp
//   }
//   return ans[n]
// }


function solution(n) {
  for (let i = 1; i <= n; i++) {
    if (i % 3 === 0 || String(i).includes('3')) n ++
  }
  return n
}