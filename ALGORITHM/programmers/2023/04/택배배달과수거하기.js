function solution(cap, n, deliveries, pickups) {
  let ans = 0
  let haveToD = 0
  let haveToP = 0
  
  for (let i = n - 1; i >= 0; i--) {
    haveToD += deliveries[i]
    haveToP += pickups[i]
    while (haveToD > 0 || haveToP > 0) {
      ans += (i + 1)
      haveToD -= cap
      haveToP -= cap
    }
  }
  return ans * 2
}

const cap = 4
const n = 5
const deliveries = [1, 0, 3, 1, 2]
const pickups = [0, 3, 0, 4, 0]

// const cap = 2
// const n = 7
// const deliveries = [1, 0, 2, 0, 1, 0, 2]
// const pickups = [0, 2, 0, 1, 0, 2, 0]

solution(cap, n, deliveries, pickups)
