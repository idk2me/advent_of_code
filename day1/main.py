import re

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],


def answer(data: list[str]) -> int:
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

def answer2(data: list[str], numbers:[list[str]]) -> int:
  # I currently have no idea how to approach this
  pass

with open('day1.txt', 'r') as f:
  data = f.read().splitlines()
  print(answer(data))
  print(answer2(data, numbers))

  