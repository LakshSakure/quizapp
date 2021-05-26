from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Student, Question, Quiz, Feedback
from django.shortcuts import redirect
from .login_form import LoginForm

def Intro(request):
    return render(request, 'into.html')

def Login(request):
    if 'id' in request.session:
        return redirect('quiz-home')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            try:
                s_email_id = request.POST.get('username')
                s_password = request.POST.get('password')
                student = Student.objects.get(email_id=s_email_id, password=s_password)
                if student:
                    request.session['id'] = student.id
                    return redirect('/quiz-home')

            except Student.DoesNotExist:
                return render(request, 'login.html', {'form': form , 'errMsg': 'Invalid Login Credentials Please Contact to your School/College'})
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})

def quizHome(request):
    if 'id' in request.session:
        id = request.session.get('id')
        form = LoginForm(request.POST or None)
        try:
            student = Student.objects.get(id=id) # getting checking and get Student data
            school = student.school_name    # getting School/College Details
            quiz = Quiz.objects.filter(school_name=school.id)  # geidtting Quiz details
            if student:
                request.session['id'] = student.id
                return render(request, 'quiz_home.html', {'studentData': student, 'school': school, 'quiz': quiz})

        except Student.DoesNotExist:
            pass
    else:
        return  HttpResponse("HTTP 403: Forbidden", status=403)


def CheckAns(request):
    if request.method == 'POST':
        try:
            user_option = request.POST.get('opt')
            q_id = request.POST.get('q')
            option_no = request.POST.get('option_no')
            question = Question.objects.get(id=q_id)
            if question:
                if question.correct_option == user_option:
                    request.session['score'] = request.session.get('score') + 1

                    res = {"error": 0, 'c': 1, 'c_option': option_no+'. '+question.correct_option, 'q': q_id}
                    return JsonResponse(res, status=200)
        except Question.DoesNotExist:
            pass

    res = {"error": 1, 'c': '0', 'q': q_id, 'c_option': question.correct_option}
    return JsonResponse(res, status=200)

def checkScore(request):
    if 'score' in request.session:
        score = request.session.get('score')
        request.session['score'] = 0
        return render(request, 'result.html', {'score': score, 'total_questions': total_questions});
    else:
        return HttpResponse("HTTP 403: Forbidden", status=403)


def testPlay(request, id):
    if 'id' in request.session:
        try:
            quiz = Quiz.objects.get(id=id)  # geidtting Quiz details
            quiz_questions = Question.objects.filter(quiz_name=quiz.id)
            request.session['score'] = 0;
            request.session['total_questions'] = quiz_questions.count()
            return render(request, 'quizes.html', {'quiz_questions': quiz_questions, 'quiz': quiz})
        except:
            pass
    else:
        return HttpResponse("HTTP 403: Forbidden", status=403)

def Logout(request):
    if 'id' in request.session:
        del request.session['id']
    if 'score'in request.session:
        del request.session['score']
    return redirect('/login')


def regFeedback(request):
    if request.method == 'POST':
        # feed = Feedback(request.POST)
        feed = Feedback.objects.create(f_name=request.POST.get('f_name'), feedback= request.POST.get('feedback'))
        if feed:
            return HttpResponse("Your Feedback registered <br /> <a href='/' class='font-weight-bold'>Go Back >></a>", status=200)
        else:
            return HttpResponse("Something going wrong, try again. <br /> <a href='/' class='font-weight-bold'>Go Back >></a>", status=403)