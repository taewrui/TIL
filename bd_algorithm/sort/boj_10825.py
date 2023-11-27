n = int(input())
score = []
for i in range(n):
    dic = list(map(str, input().split()))
    dic = {'name': dic[0], 'kor': int(dic[1]), 'eng': int(dic[2]), 'math': int(dic[3])}
    score.append(dic)

score.sort(key=lambda x: (-x['kor'], x['eng'], -x['math'], x['name']))

for i in score: print(i['name'])