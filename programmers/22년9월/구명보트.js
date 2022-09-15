function solution1(people, limit) {
  people.sort(function(a, b) {return a-b})
  let i = 0
  let j = people.length- 1
  let ans = 0
  while (i <= j) {
      if (people[i] + people[j] <= limit) {
          i+=1
      }
      j-=1
      ans+=1
  }
  return ans
}

function solution2(people, limit) {
  people.sort(function(a, b) {return a-b})
  let ans = 0
  for (let i = 0, j = people.length - 1; i <= j; j--) {
      if (people[i] + people[j] <= limit) {
          i++
      }
      ans ++
  }
  return ans
}