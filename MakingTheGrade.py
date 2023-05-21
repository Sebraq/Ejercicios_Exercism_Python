#1.Rounding Scores
def round_scores(student_scores):
    NewList=[]
    for index,score in enumerate(student_scores):
        score=round(score)
        NewList.insert(index,score)
    return NewList

#print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))

#2
def count_failed_students(student_scores):
    count=0
    for c in student_scores:
        if c<=40:count+=1
    return count
#print(count_failed_students([90,40,55,70,30,25,80,95,38,40]))

#3
def above_threshold(student_scores,threshold):
    """
    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best

    .APPEND(SCORE)***
    """
    NewList=[]
    for index,score in enumerate(student_scores):
        if score>=threshold:NewList.insert(index,score)
    return NewList

#print(above_threshold([90,40,55,70,30,68,70,75,83,96],75))

#4
def letter_grades(highest):
    """
    diference=(highest-40)/4
    NewList=[]
    for c in range(4):
        highest=highest-diference
        NewList.append(int(highest+1))#Append???
        NewList.sort()
    return NewList
    """
    diference=(highest-40)/4
    NewList=[]
    for c in range(4):
        highest=highest-diference
        NewList.insert(c,int(highest+1))
        NewList.sort()
    return NewList
    
#print(letter_grades(88))

#5
def student_ranking(student_scores,student_names):
    NewList=[]
    a=1
    for index,c in enumerate(student_scores):
        NewList.insert(index,f'{a}. {student_names[index]}: {c}')
        a+=1
    return NewList
#print(student_ranking([100, 99, 90, 84, 66, 53, 47],['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']))

#6
def perfect_score(student_info):
    NewList=[]
    for inner_list in student_info:
        if 100 in inner_list:
            return inner_list     
    return NewList
#print(perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]]))
    





