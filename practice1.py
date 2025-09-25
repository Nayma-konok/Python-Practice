import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
print(data)

for question in data:
    print(question["question_txt"])
    for i,alternative in enumerate(question["alternatives"]):
        print(i+1,".",alternative)
    user_choice=int(input("enter your answer:"))
    question["user_choice"]=user_choice

score=0   

for i,question in enumerate(data):
    if question["user_choice"]== question["correct_answer"]:
        score+=1
        result="correct answer"
    else:
        result="wrong answer"

    massage=f" {i+1}{result}-your answer:{question["user_choice"]},"\
             f"correct anser:{question["correct_answer"]}"
    print(massage)

print(score,"/",len(data))


