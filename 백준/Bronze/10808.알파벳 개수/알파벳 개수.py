my_str = str(input())

from collections import Counter
import string

counter = Counter(my_str)
answer = []


for _ in list(string.ascii_lowercase):  # alphabet list: list(string.ascii_lowercase)
  answer.append(counter[_])

#print(answer)
print(' '.join(map(str, answer)))