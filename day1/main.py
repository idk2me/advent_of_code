import re

numbers = [
  ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
]

def answer(numbers:[list[str]], data: list[str]) -> int:
  sum = 0
  data = list(map(lambda x : re.sub("[a-zA-Z]", "", x), data))
  for i in data:
    if len(i) > 2:
      i = i[0] + i[-1]
    elif len(i) == 1:
      i = 2*i
    print(i)
    sum += int(i)
  return sum

with open('day1.txt', 'r') as f:
  data = f.read().splitlines()
  print(answer(numbers, data))
  