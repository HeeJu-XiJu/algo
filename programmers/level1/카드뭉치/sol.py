def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if len(cards1) != 0 and i == cards1[0]:
            cards1.pop(0)
        elif len(cards2) != 0 and i == cards2[0] :
            cards2.pop(0)
        else:
            answer = 'No'
            break
    
    return answer

print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))