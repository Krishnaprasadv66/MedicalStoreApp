from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required , user_passes_test
from .forms import signupModelFOrm,LoginModelForm,medicineForm
from .models import login_details,signup_details,medicine_details
from django.core.paginator import Paginator



# HOME PAGE

def homepage(request):
    return render(request,'homepage.html')


# SIGNUP PAGE

def signup_page(request):
    if request.method == 'POST':
        form = signupModelFOrm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



# LOGIN PAGE



def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})






# CRUD SECTION



@login_required(login_url='home')
def add_medicine(request):
    if request.method == 'POST':
        form = medicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =medicineForm()
    return render(request, 'add_medicine.html', {'form': form})




# function for read data

def view_medicine(request):
    product_list=medicine_details.objects.all()
    return render(request,'pageview.html',{'product_list':product_list})



# function for edit datas

@login_required(login_url='home')

def edit_datas(request, id):
    product = medicine_details.objects.get(pk=id)
    if request.method == 'POST':
        form = medicineForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =medicineForm(instance=product)           
    return render(request, 'edit.html', {'form': form})



# function for delete datas

@login_required(login_url='home')

def delete_data(request,pk):
    product=medicine_details.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'product':product})





def listing(request):
    product_list = medicine_details.objects.all()
    paginator = Paginator(product_list, 3)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})






# LOG OUT PAGE


@login_required(login_url='home')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)












