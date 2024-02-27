from django.shortcuts import render ,redirect
from django.http import HttpResponse,JsonResponse

from .forms import StudentForm
from django.shortcuts import render

from .models import MyUser, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout




# Create your views here.

def signup(request):
    if request.method =='GET':
       return render(request , 'student/signup.html' )
    elif request.method == 'POST':

        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['psw']

        if_vaild=MyUser.objects.filter(email=email)
        if if_vaild:
            return render(request , 'student/signup.html' )
        
        #create Admin User if No problem
        User.objects.create_user(username=name, password=password , email=email)

        # create user if No Problem
        MyUser.objects.create(name=name, email=email, password=password )
        return redirect('login')

 


def login(request):
    
    if request.method =='GET':
       return render(request , 'student/login.html' )
    elif request.method == 'POST':
        
        email=request.POST['email']
        password=request.POST['psw']

        #we will delete password because password of admin is Hashed
        my_users=MyUser.objects.filter(email=email)


        if my_users:
             # Admin point added to check if admin details is correct
             auth=authenticate(username=my_users[0].name , password=password)
             # Here i Check if admin make login open admin dashboard with same email too 
             if auth:
                 django_login(request ,auth)  #take two param req & auth
                 request.session["email"]=email #Create session in the process too
                # Admin End point with all vaild
                 #continue all process same old
                 return redirect('students')
        else:
            return render(request , 'student/login.html' )




def signout(request):
    # Destroy session too
    request.session.clear()
    #logout from admin dashboard and auth email too 
    logout(request)
    return redirect('signup')




def students(request):
    #check if found session start show table of students
    if request.session.get('email'):
        students=Student.objects.all()
        context={}
        context['students']=students
        return render(request , 'student/students.html' , context)
    else:
        return redirect('signup')


def create_student(request):
    if request.session.get('email'):
        if request.method =='GET':
          return render(request , 'student/create_student.html' )
        elif request.method == 'POST':
            
            # create user
            Student.objects.create(f_name=request.POST['firstname'],
                                l_name=request.POST['lastname'],
                                age=request.POST['age']
                                )
            # then :
            return redirect('students')    
    else:
        return redirect("signup")
       





def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.f_name = request.POST['firstname']
        student.l_name = request.POST['lastname']
        student.age = request.POST['age']
        student.save()
        return redirect('students')
    return render(request, 'student/edit_student.html', {'student': student})



def delete_student(request, id):
    Student.objects.get(id=id).delete()
    # then render redirect to homeStudent Page
    return redirect('students')



"""--------------New Form of Django Initilization (view , html , django form)----------------"""

def Student_create_form(request):
    context = {}
    
    if request.method == "GET":
        context['form'] = StudentForm()
        return render(request, 'student/student_form.html', context)
    
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Retrieve form data
            student_id = form.cleaned_data['id']
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            age = form.cleaned_data['age']

            #create student :
            student = Student.objects.create(id=student_id, f_name=f_name, l_name=l_name, age=age)

            # then :
            return redirect('signup')














def contact(request):
     #check if found session start show table of students
    if request.session.get('email'):
        users=MyUser.objects.all()
        context={}
        context['users']=users
        return render(request , 'student/contact.html' , context)
    else:
        return redirect('signup')


