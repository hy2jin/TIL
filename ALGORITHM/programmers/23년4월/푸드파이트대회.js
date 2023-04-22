// function reverseString(str) {
//   return str.split('').reverse().join('')
// }

// function solution(food) {
//   let ans = ''
//   for (let i = 1; i < food.length; i++) {
//     if (food[i] > 1) {
//       const str = String(i)
//       const rep = parseInt(food[i]/2)
//       ans += str.repeat(rep)
//     }
//   }
//   return ans + '0' + reverseString(ans)
// }



function solution(food) {
  let ans = ''
  for (let i = 1; i < food.length; i++) {
    ans += String(i).repeat(parseInt(food[i]/2))
  }
  return ans + '0' + [...ans].reverse().join('')
}