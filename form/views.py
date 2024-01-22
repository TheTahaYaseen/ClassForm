from django.shortcuts import redirect, render

from .models import City, Student
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def form_view(request):

    error = ""
    not_submitted = True

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        city = request.POST.get("city")
        age = request.POST.get("age")
        qualifications = request.POST.get("qualifications")
        description = request.POST.get("description")        

        fields = [name, email, contact, city, age, qualifications, description]

        if "" in fields:
            error = "Please donot leave any of the fields empty!"
        elif [field for field in [name, email, city] if len(field) > 255]:
            error = "Please make sure length of name, email or city is not longer than 255."
        else:
            city = City.objects.create(city=city)
            student = Student.objects.create(name=name, email=email, contact=contact, city=city, age=age, qualifications=qualifications, description=description)
            error = "Registration Submitted! Please Wait For Any Updates!"
            not_submitted = False

    context = {"error": error, "not_submitted": not_submitted}
    return render(request, "form.html", context)

def login_view(request):
    page_title = "Login"
    form_action = page_title
    error = ""

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        if "" in [username, password]:
            error = "You cannot leave any field empty"
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                error = "User with username doesn't exist"

        if not error: 
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("form")
            else: 
                error = "Incorrect credentials!"

    context = {"page_title": page_title, "form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("form")
