# Алгоритм Прима
import math
# graf = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6), (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]
graf = [(15, 1, 2), (14, 1, 5), (23, 1, 4), (19, 2, 3), (16, 2, 4), (15, 2, 5), (14, 3, 5), (26, 3, 6), (25, 4, 5),
       (23, 4, 7), (20, 4, 8), (24, 5, 6), (27, 5, 8), (18, 5, 9), (14, 7, 8), (18, 8, 9)]
use = {1}
otv = []
cnt = 0
while (len(use) < len(graf)):
     rb = (math.inf, -1, -1)
     for s in graf:
          for i in use:
               if (s[1] == i or s[2] == i) and (s[1] not in use or s[2] not in use):
                    if s[0] < rb[0]:
                         rb = s
     if rb[0] == math.inf:
          break
     otv.append(rb)
     use.add(rb[1])
     use.add(rb[2])
     cnt += rb[0]
print(otv)
print(cnt)
# [(13, 1, 2), (14, 1, 5), (17, 1, 4), (18, 1, 3), (22, 1, 6)] 84

# с помощью матрицы
graf = [[0, 13, 18, 17, 14, 22],
        [13, 0, 26, 0, 19, 0],
        [18, 26, 0, 30, 0, 0],
        [17, 0, 30, 0, 0, 22],
        [14, 19, 0, 0, 0, 0],
        [22, 0, 0, 22, 0, 0]]
cnt = 0
v = {1}
otv = []
while len(v) < len(graf):
    rb = (math.inf, -1,-1)
    for k in v:
        for i in range(0, len(graf)):
            for j in range(i + 1, len(graf)):
                if ((i + 1) == k or (j + 1) == k) and ((i + 1) not in v or (j + 1) not in v) and graf[i][j] != 0:
                    if graf[i][j] < rb[0]:
                        rb = (graf[i][j], i+1, j+1)
    if rb[0] == math.inf:
        break
    otv.append(rb)
    v.add(rb[1])
    v.add(rb[2])
    cnt += rb[0]
print(cnt, otv)