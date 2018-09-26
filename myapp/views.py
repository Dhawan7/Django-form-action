from django.shortcuts import render
from myapp.forms import MyForm
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def userForm(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            e = form.cleaned_data['email']
            c = form.cleaned_data['Contact']
            return render(request,'form.html',{'n':name,'e':e,'c':c})
    return render(request,'form.html',{'uform':MyForm})
#
# def ajaxform(request):
#     if request.method == "POST":
#         n = request.POST['name']
#         p = request.POST['pwd']
#         d = request.POST['date']
#
#         data = ajax(name=n, password=p, dob=d)
#         data.save()
#         return HttpResponse("success")
#     return render(request,'register.html')

# def ajaxsubmit(request):
