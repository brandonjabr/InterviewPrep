def sortMax(scores,maxScore):
    s = [0] * maxScore

    for score in scores:
        s[score] += 1
    
    finalScores = []

    for i in range(len(s)):
        if s[i]:
            finalScores.append(i)
    
    return finalScores