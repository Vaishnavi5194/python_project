from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect,HttpResponse
from.models import User, Department, Complaint, Admin
from.forms import fileUploadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


# Create your views here.

#first home page
def homepage(request):
        images = Complaint.objects.all()
        return render(request,'homepage.html',{'i': images})

#user register
def userreg(request):
    if request.method == 'POST':
        member = User(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], date=request.POST['date'],lastname=request.POST['lastname'], gender=request.POST['gender'], phone=request.POST['phone'], address=request.POST['address'], email=request.POST['email'], aadharnumber=request.POST['aadharnumber'])
        member.save()
        return redirect(userlogin)
    else:
        return render(request, 'userreg.html')

#user login
def userlogin(request):
    if request.method == 'POST':
        u1 = request.POST['username']
        p1 = request.POST['password']
        try:
            d = User.objects.get(username=u1)
            if d.password == p1:
                request.session['id'] = u1
                return redirect(userhome)
            else:
                return HttpResponse('erorr')
        except Exception:
            return HttpResponse("Incorrect user name")
    return render(request, "userlogin.html")

#user home
def userhome(request):
    if 'id' in request.session:
        x = request.session['id']
        d = User.objects.filter(username=x)
        return render(request, "userhome.html",{'username':d})
    else:
        return redirect(userlogin)

#user Logout
def userlogout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'userlogin.html')

def usercomplaintdisplay(request):
    if 'id' in request.session:
        x = request.session['id']
        d = Complaint.objects.filter(username=x)
        return render(request, "usercomplaint.html", {'c': d})

def depregister(request):
    if request.method == 'POST':
        member1 = Department(username=request.POST['username'], password=request.POST['password'], firstname=request.POST['firstname'], lastname=request.POST['lastname'],department=request.POST['department'], phone=request.POST['phone'], address=request.POST['address'],email=request.POST['email'])
        member1.save()
        return redirect(deplogin)
    else:
        return render(request,'departmentreg.html')

#department login
def deplogin(request):
    if request.method == 'POST':
        u1 = request.POST['username']
        p1 = request.POST['password']
        d1 = request.POST['department']
        try:
            d = Department.objects.get(username=u1, department=d1)
            if d.password == p1:
                request.session['id'] = u1
                return redirect(dephome)
            else:
                return HttpResponse('erorr')
        except Exception:
            return HttpResponse("Incorrect user name")
    return render(request, "departmentlogin.html")

#department logout
def deplogout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request, 'departmentlogin.html')

#department home
def dephome(request):
    if 'id' in request.session:
        x = request.session['id']
        d = Department.objects.filter(username=x)
        return render(request, "departmentprofile.html", {'c': d})
    else:
        return redirect(deplogin)

#user displya
def userdisplay(request):
        data = User.objects.all()
        return render(request, 'userdisplay.html', {'data': data})

#complaint register
# def complaintreg(request):
#     if 'id' in request.session:
#         x = request.session['id']
#         d = Department.objects.filter(username=x)
#         if request.method == 'POST':
#             form = fileUploadForm(request.POST, request.FILES)
#             if form.is_valid():
#                 a = form.cleaned_data['username']
#                 c = form.cleaned_data['department']
#                 d = form.cleaned_data['phone']
#                 e = form.cleaned_data['address']
#                 f = form.cleaned_data['issue']
#                 g = form.cleaned_data['file']
#                 data = Complaint(username=a, department=c, phone=d, address=e, issue=f, file=g)
#                 data.save()
#                 return render(request, "userhome.html" )
#
#             else:
#                 return HttpResponse("Error")
#         else:
#             return render(request, "complaintreg.html", {'c': d})

def complaintreg(request):
    if request.method == 'POST':
        form = fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.cleaned_data['username']
            c = form.cleaned_data['department']
            e = form.cleaned_data['address']
            f = form.cleaned_data['issue']
            g = form.cleaned_data['file']
            data = Complaint(username=a, department=c, address=e, issue=f, file=g)
            data.save()
            return render(request, "userhome.html")
        else:
            print(form.errors)  # Print form errors for debugging
            return HttpResponse("Error")
    else:
        return render(request, "complaintreg.html")


#complaint display
def complaintdisplay(request):
    if 'id' in request.session:
        department_username = request.session['id']
        department = Department.objects.get(username=department_username)
        complaints = Complaint.objects.filter(department=department.department)
        return render(request, "complaintdisplay.html", {'complaints': complaints})
    else:
        return HttpResponse("Error 401")


#test page
def test(request):
    images = Complaint.objects.all()
    return render(request,"test.html", {'i': images})

#user complaint display page
def usercomplaint(request):
    if request.member.is_authenticated:
        data = User.objects.filter(member=request.member)
        return render(request, 'userhome.html', {'data': data})

#gmail
def gmail(request):
    return redirect()


#-------------------ADMIN---------------------------

# admin profile
def adminlogin1(request):
    if 'id' in request.session:
        if request.method == 'GET':
            u = User.objects.all()
            d = Department.objects.all()
            c = Complaint.objects.all()
            return render(request, 'admin_profile.html', {'data': u, 'data1': d, 'data2': c})
        return render(request, 'admin_profile.html')
    else:
        return redirect(adminlogin)

#admin login
def adminlogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']
        try:
            d = Admin.objects.get(username=uname)

            if d.password == pword:
                request.session['id'] = uname
                return redirect(adminlogin1)
            else:
                return HttpResponse("Incorrect Password")
        except Exception:
            return HttpResponse("Incorrect username")
    return render(request, 'ADMIN.html')

#admin logout
def adminlogout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(adminlogin)


#about page
def about(request):
    return render(request, "about.html")

#support page
def support(request):
    return render(request, "support.html")

#contact page
def contact(request):
    return render(request,"contact.html")

#Terms and conditions page
def terms(request):
    return render(request,"terms.html")


# views.py

from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages


# ...
#passwordreset//////////////

@login_required
def admin_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password has been changed successfully.')
            update_session_auth_hash(request, user)  # Update the session to prevent the user from being logged out
            return redirect('admin_profile.html')  # Redirect to the admin profile page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'admin_change_password.html', {'form': form})


@login_required
def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password has been changed successfully.')
            update_session_auth_hash(request, user)  # Update the session to prevent the user from being logged out
            return redirect('userhome.html')  # Redirect to the user profile page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'user_change_password.html', {'form': form})


@login_required
def department_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password has been changed successfully.')
            update_session_auth_hash(request, user)  # Update the session to prevent the user from being logged out
            return redirect('departmentprofile.html')  # Redirect to the department profile page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'department_change_password.html', {'form': form})