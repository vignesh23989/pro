from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Student, Department
from .forms import BasicForm, StudentForm, DepartmentForm
from django.contrib import messages
# Login
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate, logout #add this


def index(request):
    return HttpResponse("<h1>Hello, guys.</h1>")

def sayhello(request):
    return HttpResponse("Hello world!")

def employee(request):
    return HttpResponse("welcome")

def wishme(request, name):
    return HttpResponse("Hi %s" % name)

def add(request, num1, num2):
    return HttpResponse("Adition result %s" % str(num1+num2))

def current_time(request):
    return HttpResponse("<h1>%s</h1>" % datetime.now())

def home(request):
    context = {
        'name': 'Test',
        'mobile': 4444444444,
        'fruits':['Apple', 'Orange'],
        'inv_items':[
            {'name': 'A', 'price': 10},
            {'name': 'D', 'price': 25},
            {'name': 'C', 'price': 70},
            ]
    }
    return render(request, 'students/home.html', context)



def signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = BasicForm()
    return render(request, 'students/signup.html', {'form': form})

def customized_crispy_signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            print("Hello ")
            print("--------------------")
            print(form.cleaned_data)
            print("--------------------")
            # new_stud = Student.objects(first_name = form.cleaned_data['first_name'])
            
            pass
    else:
        print("Not a valid form")
        form = BasicForm()
    return render(request, 'students/customized_crispy_signup.html', {'form': form})

def thanksView(request):
    return render(request, 'students/thanks.html')

# -------------Students--------------------
def studentsView(request):
    students = Student.objects.all()
    return render(request, 'students/students/student.html', {'data': students})


def studentsAddView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() 
            model = form.instance
            # stu = Student(**form.cleaned_data)
            # val = {'num1':10, 'num2': 20}
            # add(**val) i.e add('num1'=10, 'num2'=20)
            # obj = ModelClasssName(field1='value1', field2='value2') (temporary  object)
            # obj.save()
            # stu.save()            
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students/students/add.html', {'form': form})

def studentsEditView(request, id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save() 
            model = form.instance
            messages.success(request, "Student Updated successfully")
            # for key, value in form.cleaned_data.items():
            #     setattr(stu, key, value)
            # stu.save()            
            return redirect('students')
    else:
        form = StudentForm(initial={
            'first_name': stu.first_name, 
            'last_name': stu.last_name, 
            'register_no': stu.register_no,
            'address': stu.address,
            'gender': stu.gender,
            'DOB': stu.DOB,
            'phone': stu.phone,
            'age': stu.age,
            })
    return render(request, 'students/students/add.html', {'form': form})

def studentsDeleteView(request, id):
    if id:
        student = Student.objects.get(id=id)
        try:
            student.delete()
        except:
            pass
    return redirect('students')
# ----------Department----------------
def departmentsView(request):
    departments = Department.objects.all()
    return render(request, 'students/departments/department.html', {'data':departments})



def departmentAddView(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            #form.save() 
            #model = form.instance
            stu = Student(**form.cleaned_data)
            # val = {'num1':10, 'num2': 20}
            # add(**val) i.e add('num1'=10, 'num2'=20)
            # obj = ModelClasssName(field1='value1', field2='value2') (temporary  object)
            # obj.save()
            stu.save()            
            return redirect('departments')
    else:
        form = DepartmentForm()
    return render(request, 'students/departments/add.html', {'form': form})


# ------------Login-------------------------


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("students")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="students/user/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")