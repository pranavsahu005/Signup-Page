from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'HTML/front.html')


def signup(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        s_password = request.POST.get('s_password')
        c_password = request.POST.get('c_password')
        
        
        security_question = request.POST.get('security_question')
        security_answer = request.POST.get('security_answer')

        if s_password == c_password:
            password = s_password
            
            try:
              
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO details (username, password, email, contact, security_question, security_answer) VALUES (%s, %s, %s, %s, %s, %s)",
                        [username, password, email, contact, security_question, security_answer]
                    )
                messages.success(request, 'Signup successful! You can now sign in.')
                return redirect('signin') 
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')

        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'HTML/signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists in the DB using raw SQL
        with connection.cursor() as cursor:
            cursor.execute("SELECT username FROM details WHERE email = %s AND password = %s", [email, password])
            row = cursor.fetchone()

        if row:
            # If valid, log the user in manually using Django’s login()
            username = row[0]

            # Create a mock User object (not ideal — better to use Django's User model)
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a temporary user object (only needed if you are not using Django's auth model)
                user = User.objects.create_user(username=username, password=password)
            login(request, user)

            # Redirect to next or dashboard
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials. Try again.')

    return render(request, 'HTML/signin.html')


@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'HTML/dashboard.html', {'user': request.user})
