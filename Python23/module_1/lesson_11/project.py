# suniy intelect
data = {}

while True:
    question = input("Question : ")
    if not data.get(question , False):
        answer = input("Answer : ")
        data[question] = answer
    else:
        print(">>>",data.get(question))


# =================== TZ ======================
"""
1) Question
    >>> Question : 
        if -> answer : 
        else -> >>> value
2) Update
    >>> Question :
    >>> answer : 
    
3) exit
    finish !
>>>1
"""

# EXAM : ALGO 1-172
# 5 savol -> 3 soat







