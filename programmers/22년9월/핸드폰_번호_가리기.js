function solution(phone_number) {
  let len = phone_number.length
  let star = ""
  for (let i in phone_number) {
      if (i < len-4) {
          star += "*"
      }
  }
  return star + phone_number.slice(len-4, len)
}

function solution(phone_number) {
  let len = phone_number.length
  return "*".repeat(len-4) + phone_number.slice(len-4, len)
}