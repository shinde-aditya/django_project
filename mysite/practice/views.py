from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'name':'Prashant',
        'EMPID':'EMP01',
        'Mobile_No':123456789,
        'Email_Id':'abc123@hmail.com'
    }
    return render(request,'index.html',context)

def aboutUs(request):
    return render(request,'about.html')

def contactUs(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def add(request):
    if request.method=='GET':
        val1=int(request.GET['fvalue'])
        val2=int(request.GET['svalue'])
        sum=val1+val2


    return render(request,'result.html',{'sum':sum})

