from django.shortcuts import render
from .models import QandA,Subject,Score
from django.core.paginator import Paginator
from django.contrib.auth.models import User
def homepage(request):    
    sub=Subject.objects.all()
    paginator=Paginator(sub,3)
    page=request.GET.get('page')
    sub=paginator.get_page(page)
    return render(request,'quiz/homepage.html',{'sub':sub})

def question(request,user_id,sub_id):
    user=User.objects.get(id=user_id)
    sub=Subject.objects.get(id=sub_id)
    questions_ob=QandA.objects.filter(sub=sub_id)  
    return render(request,'quiz/question.html',{'questions_ob':questions_ob,'user':user,'sub':sub})

def result(request,user_id,sub_id):
    questions_ob=QandA.objects.all()
    count=0
    if(request.method=="POST"):
        for question_ob in questions_ob:
            selected_options=request.POST.get('ques'+str(question_ob.id))
            correct_answer=question_ob.answer
            # print(selected_options)
            # print(correct_answer)
            if(selected_options==correct_answer):
                count+=1
        
        user=User.objects.get(id=user_id)
        sub=Subject.objects.get(id=sub_id)
        if(Score.objects.filter(user=user,sub=sub).exists()):
            score=Score.objects.get(user=user,sub=sub)
            score.marks=count
            score.save()
        else:
            marks=count
            score=Score(user=user,sub=sub,marks=marks)
            score.save()
        return render(request,'quiz/result.html',{'count':count})
    return render(request,'quiz/question.html')

