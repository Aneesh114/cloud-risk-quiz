from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import random
from datetime import datetime
#from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def quizPage(request):
    if request.method == 'POST':
        #print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        qn = 1
        dev = 0
        sec = 0
        secn = 0
        devn = 0
        references = []
        correctl = []
        for q in questions:
            total+=1
           # print(request.POST.get(q.question))
           # print(q.ans)
           # print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
                correctl.append({'question_number':qn,'right':'Correct','ans':q.ans})
                if(q.category == 'Security'):
                  sec += 1
                else:
                  dev += 1
            else:

                wrong+=1
                correctl.append({'question_number':qn,'right':'Incorrect','ans':q.ans})
            
            references.append({'question_number':qn,'reference':q.reference})
            qn+=1
        percent = score/(total*10) *100
        secn = sec/total*360
        devn = dev/total*360
        result = ResultModel.objects.create(user = request.user, score = score)
        result.save() 
        data = ResultModel.objects.all()
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'date': request.POST.get('date'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'references' : references,
            'correctl' : correctl,
            'sec' : sec,
            'dev' : dev,
            'secn' : secn,
            'devn' : devn,
            'data' : data
            
        }
        
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

def tipsPage(request):
        tips = []
        tips.append('1. Use ''Post'' method instead of ''Get'' so that the values of variables present in the code does not appear in the URL making it more secure')
        tips.append('2. Try to use different apps for different functionalities of a Webapp so that it is easier to copy these into another Webapp or debug it')
        tips.append('3. Instead of importing files from a package one by one, you can use an asterisk(*) to get all the files from the package')
        tips.append('4. Once you create a model, objects with required feautures can be created automatically and used by multiple web pages to analyze the data in different perspectives')
        tips.append('5. Security of the data handled by the cloud is a responsibility of both the service provided and the user which is said by \'The Shared Responsibility Model\'')
        tips.append('6. Microsoft Azure provides various services that can be used fused with the webapp to increase its functionality or enable us to monitor and secure data in a feasible way ')
        randomi = random.randint(0,len(tips)-1)
        context = {'tips':tips[randomi]}
        #context = {'tips':k}
        
        return render(request,'Quiz/tip.html',context)

@login_required
def home(request):
    context = {}
    return render(request,'Quiz/home1.html',context)

def learnPage(request):
    context = {}
    return render(request,'Quiz/learn.html',context)

def analyzePage(request):
 data = ResultModel.objects.all()
 date = datetime.now
 context = {'data' : data,
            'date' : date,
            }
 return render(request,'Quiz/analyze.html',context)