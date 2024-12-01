from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
from .models import *
import random

def home(request):
    context = {'categories':Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request,'home.html',context)

def quiz(request):
    context = {'category':request.GET.get('category')}
    return render(request,'quiz.html',context)

# Now we random question generator using API's
def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs = list(question_objs)

        data = []
        # it randomly shuffle with question
        random.shuffle(question_objs)

        for questions_ob in question_objs:
            data.append({
                'uid': questions_ob.uid,
                'category': questions_ob.category.category_name,
                "question": questions_ob.question,
                "marks": questions_ob.marks,
                'answers':questions_ob.get_answer()
            })
        payload = {'status':True,'data':data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went Wrong")        