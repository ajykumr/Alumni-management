from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AlumniForm, StaffAccountForm, CreateStaffForm, AlumniUpdateForm, EmployerFormset

from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Alumni, StaffAccount,Employer
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# views starts here

def home(request):
	return render(request, 'appcore/home.html', {'title':"Home - Alumni"})


def humanstxt(request):
	return render(request, 'appcore/humans.txt')


def registraion_success(request):
	return render(request, 'appcore/success_registration.html', {'title':"Success - Alumni"})


def account_success(request):
	return render(request, 'appcore/success_account.html', {'title':"Success - Alumni"})


class BookListView(generic.ListView):
    model = Alumni
    context_object_name = 'Alumnis'
    print(context_object_name)
    template_name = 'appcore/a.html'


def registerform(request):
    if request.method == 'POST':
        alumniForm = AlumniForm(request.POST, request.FILES)
        employerFormset = EmployerFormset(request.POST)
        if alumniForm.is_valid() and employerFormset.is_valid():
            alumni = alumniForm.save()
            for form in employerFormset:
                employer = form.save(commit=False)
                employer.alumni = alumni
                employer.save()
                return redirect('/success')
    alumniForm = AlumniForm()
    employerFormset = EmployerFormset()
    context = {'Alumniform': alumniForm,'EmployerFormset': employerFormset,'title':"Alumni Registration - Alumni"}
    return render(request, 'appcore/form_registration1.html', context)


# need authentication pages
@login_required(login_url='login')
def documentation(request):
    return render(request, 'appcore/documentation.html', {'title':"Documentation - Alumni"})


def logoutUser(request):
	logout(request)
	return redirect('login')


@unauthenticated_user
def signin_page(request):
    form =  CreateStaffForm()
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.is_active = False
            user.save()
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            StaffAccount.objects.create(
                user=user,
                name=user.username,
                 )
            return redirect('account_success')
    context = {'form' : form,'title':"Sign in - Alumni"}
    return render(request, 'appcore/form_signin.html', context)
    
@unauthenticated_user
def staff_signin_page(request):
    form =  CreateStaffForm()
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            StaffAccount.objects.create(
                user=user,
                name=user.username,
                 )
            return redirect('account_success')
    context = {'form' : form,'title':"Sign in - Alumni"}
    return render(request, 'appcore/form_signin.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
           login(request, user)
           return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect (or) contact Admin if both are correct')

    context = {'title':"Login - Alumni"}
    return render(request, 'appcore/form_login.html', context)


@login_required(login_url='login')
def dashboard(request):
    alumni = Alumni.objects.all()
    total_alumni = alumni.count()
    approved_alumni = alumni.filter(status='Accepted').count()
    rejected_alumni = alumni.filter(status='Rejected').count()
    pending_alumni = alumni.filter(status='Pending').count()

    branches = ['CS', 'CV', 'EC', 'ME']
    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022,2023]
    # years = alumni.values_list('pass_year', flat=True).distinct().order_by('pass_year')
    tablevaluess = []

    for year in years:
        locallist = []
        yearBool = True
        for branch in branches:
            if yearBool :
                locallist.append(year)
                yearBool = False
            localitem = alumni.filter(pass_year=year, branch=branch).count()
            locallist.append(localitem)
        tablevaluess.append(locallist)


    userName = request.user
    staffAccount = StaffAccount.objects.get(user=request.user.id)
    print(staffAccount.name)

    context = {'total_alumni':total_alumni, 'approved_alumni':approved_alumni,
    'rejected_alumni':rejected_alumni,'pending_alumni':pending_alumni,'title':"Dashboard - Alumni", 'userName':userName, 'tablevaluess' : tablevaluess}
    return render(request, 'appcore/dashboard_stats.html', context)


@login_required(login_url='login')
def dashboard_all(request):
    filter_dict = {}
    userName = request.user;
    alumni = []

    if request.method == 'POST':
        if 'filterSubmit' in request.POST:
            filter_list = ('pass_year', 'branch', 'gender', 'status')
            for filter in filter_list:
                val = request.POST.get(filter)
                if not (val == '') :
                    filter_dict[filter] = val

        if 'searchNormalWithCategory' in request.POST:
            search_catogery = request.POST.get('search_catogery')
            search_word = request.POST.get('search_word')
            filter_dict[search_catogery] = search_word

        alumni = Alumni.objects.filter(**filter_dict ).order_by('usn')

    else:
        alumni = Alumni.objects.all().order_by('usn')

    paginator = Paginator(alumni, 60) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    userName = request.user;
    context = {'page_obj': page_obj,'title':"All registered - Alumni", 'highlight_menu':'dash_bar_list_all_registered', 'userName':userName,  'filter_dict': filter_dict}
    return render(request, 'appcore/dashboard_approved.html',context )


@login_required(login_url='login')
def dashboard_approved(request):
    alumni = Alumni.objects.filter(status="Accepted").order_by('usn')
    paginator = Paginator(alumni, 60) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    userName = request.user;
    context = {'page_obj': page_obj,'title':"dashboard - Alumni", 'highlight_menu':'dash_bar_list_approved', 'userName':userName}
    return render(request, 'appcore/dashboard_approved.html',context )


@login_required(login_url='login')
def dashboard_pending(request):
    alumni = Alumni.objects.filter(status="Pending").order_by('usn')
    paginator = Paginator(alumni, 60) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    userName = request.user;
    return render(request, 'appcore/dashboard_approved.html',{'page_obj': page_obj,'title':"dashboard - Alumni", 'highlight_menu':'dash_bar_list_pending', 'userName':userName})


@login_required(login_url='login')
def dashboard_rejected(request):
    alumni = Alumni.objects.filter(status="Rejected").order_by('usn')
    paginator = Paginator(alumni, 60,orphans=10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    userName = request.user
    return render(request, 'appcore/dashboard_approved.html',{'page_obj': page_obj,'title':"dashboard - Alumni", 'highlight_menu':'dash_bar_list_rejected', 'userName' : userName})


@login_required(login_url='login')
def update_alumni(request, pk):
    alumni =  Alumni.objects.get(usn=pk)
    userName = request.user;
    form = AlumniUpdateForm(initial={'staff': userName}, instance=alumni)

    if request.method == 'POST':
        form = AlumniUpdateForm(request.POST,request.FILES, instance=alumni)
        if form.is_valid():
           form.save()
           message_text = alumni.firstname + alumni.lastname + '('+ alumni.usn + ')' + ' is updated'
           messages.info(request, message_text)
           return redirect(reverse('view_alumni',args=[alumni.usn]))
    context = {'form': form,'alumni':alumni.usn,'title':"Update Alumni - Alumni", 'userName': userName }
    return render(request, 'appcore/alumni_update.html',context )


@login_required(login_url='login')
def view_alumni(request, pk):
    alumni =  Alumni.objects.get(usn=pk)
    print(alumni)
    employers = Employer.objects.filter(alumni_id=alumni.usn).order_by("Employer_join_year")
    print(employers)
    for employ in employers:
        print("---------------------------------")
        print(employ.Employer_name)
        print(employ.Employer_Designation)
        print(employ.Employer_join_year)
        print(employ.alumni_id)
        print("---------------------------------")
    return render(request, 'appcore/alumni_view.html', {'alumni':alumni,"employers":employers ,'title':"View Alumni - Alumni"})


@login_required(login_url='login')
def accountview(request):
    staffAccount = StaffAccount.objects.get(user=request.user.id)
    context = {'staffAccount':staffAccount, 'title':"Account - Alumni"}
    return render(request, 'appcore/account_view.html', context)
    
@login_required(login_url='login')
def studentview(request):
    staffAccount = StaffAccount.objects.get(user=request.user.id)
    context = {'staffAccount':staffAccount, 'title':"Account - Alumni"}
    return render(request, 'appcore/account_view.html', context)


@login_required(login_url='login')
def accountUpdate(request):
    staffAccount = StaffAccount.objects.get(user=request.user.id)
    form = StaffAccountForm(instance=staffAccount)
    userName = staffAccount.name
    if request.method == 'POST':
        form = StaffAccountForm(request.POST, request.FILES,instance=staffAccount)
        if form.is_valid():
           form.save()
           message_text = userName + ' updated'
           messages.info(request, message_text)
           return redirect('accountView')
    context = {'form':form,'title': "Account Update - Alumni"}
    return render(request, 'appcore/account_update.html', context)


login_required(login_url='login')
def delete_alumni(request, pk):
    alumni = Alumni.objects.get(usn=pk)
    if request.method == "POST":
        alumni.delete()
        message_text = alumni.firstname + alumni.lastname + '('+ alumni.usn + ')' + ' is deleted'
        messages.info(request, message_text)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def records(request, id=None):
    if request.method == 'POST':
        usn_list = request.POST.getlist('selectedCheckBox')
        list_length = len(usn_list)

        if 'deleteAlumniList' in request.POST:
            for val in usn_list:
                Alumni.objects.filter(pk=val).delete()
            message_text = str(list_length) + ' alumni(us) are deleted'
            messages.info(request, message_text)

        elif 'approveAlumniList' in request.POST:
            for val in usn_list:
                Alumni.objects.filter(pk=val).update(status='Accepted', staff=str(request.user))
            message_text = str(list_length) + ' alumni(us) are Approved'
            messages.info(request, message_text)

        elif 'updateAlumniList' in request.POST:
            bulkUpdateCategory = request.POST.get('bulkUpdateCategory')
            bulkUpdateCategoryInput = request.POST.get('bulkUpdateCategoryInput')
            dictCont = {bulkUpdateCategory : bulkUpdateCategoryInput}
            for val in usn_list:
                Alumni.objects.filter(pk=val).update(**dictCont)
            message_text = str(list_length) + ' alumni(us) are Updated'
            messages.info(request, message_text)

        elif 'rejectAlumniList' in request.POST:
            for val in usn_list:
                Alumni.objects.filter(pk=val).update(status='Rejected', staff=str(request.user))
            message_text = str(list_length) + ' alumni(us) are Rejected'
            messages.info(request, message_text)

        return redirect(request.META.get('HTTP_REFERER'))
