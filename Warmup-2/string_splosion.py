def string_splosion(str):
  answer = ""
  for i in range(len(str)+1):
    answer += str[:i]
  return answer