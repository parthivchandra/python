import time
questions = [

{
    'question' : 'what is the square root of  1764?',
    'options' : ['A) 36','B) 41','C) 42','D)32'],
    'answer' :  'C'
},
{
    'question' : 'what is 28x26?',
    'options' : ['A)828', 'B)728','C)646','D)986'],
    'answer' : 'B'
},
{
    'question' : 'what is 125+464',
    'options' : ['A)489','B)589','C)579','D)559'],
    'answer' : 'B'
}
]
 
def quiz(questions,timelimit = 10):
    totalscore = 0
    questionnumber = 1
    for q in questions:
        print(f"\nQuestion{questionnumber}:{q['question']}")
        for options in q ['options']:
            print(options)
        starttime = time.time()
        answer = input(f'\n enter your choice(A/B/C/D),time limit{timelimit} seconds:')
        endtime = time.time()
        timetaken = endtime - starttime
        if timetaken > timelimit:
            print('time up')
        elif answer == q['answer']:
            score = (10)
            print(f'correct answer {score} marks')
            totalscore += score
        else:
            print('incorrect answer')
        questionnumber += 1
    print('\n quiz completed')
    print(f"total score is: {totalscore} out of {len(questions)*10}")
quiz(questions)
