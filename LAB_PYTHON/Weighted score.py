weights = [10, 20, 30, 40]
max_scores = [50, 40, 80, 80]
scores = [45, 30, 50, 40]

sum = 0

if(len(weights) == 0):
    temp = 100/len(scores)
    for i in range(len(scores)):
        weights.append(temp)


for i in range(len(scores)):
    result = (scores[i]/max_scores[i])*weights[i]
    sum += result

print("%.2f"%sum)