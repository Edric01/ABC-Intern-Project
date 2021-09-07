from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import KYCdetails,abcacc,RateofInterest
import os
import random
from datetime import date,timedelta


def home(request):
    return render(request,"index.html",)

def register(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return render(request,"login.html")
        else:
            messages.info(request,'Password not matching')
    
    return render(request,"register.html")    

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        else:
            messages.info(request,"*Invalid Credentials")
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def services(request):
   return render(request,'services.html') 

def feedback(request):
    pass
    #return render(request,os.read("shorturl.at/bpJZ5"))

def kyc(request):
    return render(request,'kyc.html')

def kyccreate(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        gender=request.POST['gender']
        add_line1=request.POST['aline1']
        add_line2=request.POST['aline2']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
        idtype=request.POST['idType']
        idnum=request.POST['idnum']
        issue_date=request.POST['issuedate']
        expiry_date=request.POST['expirydate']
        k=KYCdetails.objects.create(firstname=firstname,lastname=lastname,gender=gender,add_line1=add_line1,add_line2=add_line2,country=country,state=state,city=city,zipcode=zipcode,mobile=mobile,dob=dob,idtype=idtype,idnum=idnum,issue_date=issue_date,expiry_date=expiry_date)
        k.save()
        return render(request,'kyc.html')
    else:
        return render(request,'createform.html')

def searchkyc(request):
    if request.method=='POST':
        k=KYCdetails.objects.all()
        k_idnum=[]
        for i in k:
            k_idnum.append((i.idnum,i.idtype))
        id=request.POST['search']
        idtype=request.POST['radio']
        id=str(id)
        if (id,idtype) not in k_idnum:
            messages.info(request,"Enter valid Id number")
            return redirect('/searchkyc')
        a=KYCdetails.objects.get(idnum = id)
        if a.verify==True:
            messages.info(request,"Verified")
        else:
            messages.info(request,"Not Verified")
        return render(request,"viewkyc.html",{'a':a})
        
    else:
        return render(request,"searchkyc.html")

def research(request):
    if request.method=='POST':
        b=0
        k=KYCdetails.objects.all()
        k_idnum=[(i.idnum,i.idtype) for i in k]
        id=request.POST['search']
        idtype=request.POST['radio']
        verify=request.POST['verify']
        id=str(id)
        if (id,idtype) not in k_idnum:
            messages.info(request,"Enter valid Id number")
            return redirect('/reseach')
        a=KYCdetails.objects.get(idnum = id)
        if verify=="true":
            if a.abcno!="ABC202100000":
                messages.info(request,"Kyc has already been Verified and account number is Generated")
                return redirect('/searchkyc')
            a.verify=True
            accno="ABC2021"
            alst=[i.abcno for i in k]
            a_lst=[i[7:] for i in alst]
            a_lst=[int(i) for i in a_lst]
            lst=[i for i in range(1,99999)]
            for i in a_lst:
                if i in lst:
                    lst.remove(i)
            random.shuffle(lst)
            b=lst.pop()
            b=str(b)
            if len(b)<5:
                b=b.zfill(5)
            accno+=b
            a.abcno=accno
            messages.info(request,"Verified")
        else:
            a.verify=False
            messages.info(request,"Not Verified")
        a.save()
        return render(request,"verifykyc.html",{'a':a})
    else:
        return render(request,"research.html")

def verifysearch(request):
    if request.method=='POST':
        k=KYCdetails.objects.all()
        k_idnum=[]
        for i in k:
            k_idnum.append(i.idnum)
        id=request.POST['search']
        id=str(id)
        if id not in k_idnum:
            messages.info(request,"Enter valid Id number")
            return redirect('/reseach')
        a=KYCdetails.objects.get(idnum = id)
        if a.abcno!="ABC202100000":
            return render(request,"viewkyc.html",{'a':a})
        return render(request,"verifykyc.html",{'a':a})
    else:
        return render(request,"research.html")

def editkyc(request):
    k=KYCdetails.objects.all()
    k_idnum=[]
    for i in k:
        k_idnum.append(i.idnum)
    id=request.POST['idnum']
    id=str(id)
    if id not in k_idnum:
        message=""
        return redirect("searchkyc.html",{message:"Id Number Does not exists"})    
    a=KYCdetails.objects.get(idnum=id)
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    gender=request.POST['gender']
    add_line1=request.POST['aline1']
    add_line2=request.POST['aline1']
    country=request.POST['country']
    state=request.POST['state']
    city=request.POST['city']
    zipcode=request.POST['zipcode']
    mobile=request.POST['mobile']
    dob=request.POST['dob']
    idtype=request.POST['idType']
    idnum=request.POST['idnum']
    issue_date=request.POST['issuedate']
    expiry_date=request.POST['expirydate']
    if firstname is not None:
        a.firstname=firstname
    if lastname is None:
        a.lastname=lastname
    if gender is not None:
        a.gender=gender
    if add_line1 !='':
        a.add_line1=add_line1
    if add_line2 !='':
        a.add_line2=add_line2
    if country is not None:
        a.country=country
    if state is not None:
        a.state=state
    if city is not None:
        a.city=city
    if zipcode !='':
        a.zipcode=zipcode
    if mobile !='':
        a.mobile=mobile
    if dob !='':
        a.dob=dob
    if idtype !='':
        a.idtype=idtype
    if idnum !='':
        a.idnum=idnum
    if issue_date !='':
        a.issue_date=issue_date
    if expiry_date !='':
        a.expiry_date=expiry_date
    a.save()
    return render(request,'kyc.html')

def viewkyc(request):
    return render(request,"viewkyc.html")
def reset(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        k=User.objects.all()
        if password1!=password2:
            return redirect("/reset") 
        a=User.objects.get(username=username)
        a.set_password(password1)
        a.save()
        return redirect("/")
    else:    
        return render(request,"re.html")

def accounts(request):
    return render(request,"accounts.html")

def editsearch(request):
    if request.method=='POST':
        k=KYCdetails.objects.all()
        k_idnum=[]
        for i in k:
            k_idnum.append((i.idnum,i.idtype))
        id=request.POST['search']
        idtype=request.POST['radio']
        id=str(id)
        if (id,idtype) not in k_idnum:
            messages.info(request,"Enter valid Id number")
            return redirect('/editsearch')
        a=KYCdetails.objects.get(idnum = id)
        return render(request,"editkyc.html",{'a':a})
    else:
        return render(request,"editsearch.html")


def accsearch(request):
    if request.method=="POST":
        acno=request.POST['search']
        k=KYCdetails.objects.all()
        a=abcacc.objects.all()
        a_acno=[i.abcno for i in a]
        k_acno=[i.abcno for i in k]
        if acno not in k_acno  or acno[7:]=="00000":
            messages.info(request,"Account Number does not exists, Verify KYC to create an Account")
            return render(request,"accsearch.html")
        elif acno in a_acno:
            messages.info(request,"Account already Exists")
            return render(request,"accsearch.html")
        a=KYCdetails.objects.get(abcno = acno)
        return render(request,"createaccount.html",{'a':a})
    
    else:
        return render(request,"accsearch.html")

def acccreate(request):
    if request.method=="POST":
        idno=request.POST['idnum']
        a=KYCdetails.objects.get(pk=idno)
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        gender=request.POST['gender']
        add_line1=request.POST['aline1']
        add_line2=request.POST['aline1']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
        idtype=request.POST['idType']
        acctype=request.POST['typeofAc']
        balance=request.POST['deposit']
        duration=request.POST['duration']
        if firstname is not None:
            a.firstname=firstname
        if lastname is None:
            a.lastname=lastname
        if gender is not None:
            a.gender=gender
        if add_line1 !='':
            a.add_line1=add_line1
        if add_line2 !='':
            a.add_line2=add_line2
        if country is not None:
            a.country=country
        if state is not None:
            a.state=state
        if city is not None:
            a.city=city
        if zipcode !='':
            a.zipcode=zipcode
        if mobile !='':
            a.mobile=mobile
        if dob !='':
            a.dob=dob
        if idtype !='':
            a.idtype=idtype
        if acctype=="saving":
            duration=0
        duration=float(duration)
        today=date.today()
        if acctype=="Fixed":
            enddate=today+timedelta(days=duration)
        b=abcacc.objects.create(abcno=a.abcno,acctype=acctype,balance=balance,begindate=today,duration=duration,enddate=enddate)
        b.save()
        return redirect('/accounts')
    else:
        return render(request,"createaccount.html")

def accresrch(request):
    if request.method=="POST":
        acno=request.POST['search']
        k=KYCdetails.objects.all()
        c=abcacc.objects.all()
        c_acno=[i.abcno for i in c]
        k_acno=[i.abcno for i in k if i.abcno!="ABC202100000"]
        if acno not in c_acno and acno in k_acno:
            a=KYCdetails.objects.get(abcno=acno)
            messages.info(request,"Account does not exists, Create an account")
            return render(request,"createaccount.html",{'a':a})
        elif acno not in k_acno:
            messages.info(request,"Account Number does not exists, Verify KYC to create an Account")
            return render(request,"accsearch.html")
        a=KYCdetails.objects.get(abcno=acno)
        b=abcacc.objects.get(pk=acno)
        creation_date=b.begindate
        creation_date=creation_date[:10]
        duration=b.duration
        duration=duration//365
        address=a.add_line1+" "+a.add_line2
        return render(request,"viewaccount.html",{'a':a,'b':b,'date':creation_date,'duration':duration,'address':address})
    else:
        return render(request,"accsear.html")
        
def rate(request):
    if request.method=="POST":
        typeofacc=request.POST['typeofacc']
        duration=request.POST['duration']
        rate=request.POST['RateofI']
        duration=int(duration)
        rate=float(rate)
        a=RateofInterest.objects.create(typeofacc=typeofacc,duration=duration,rate=rate)
        a.save()
        return render(request,"rateofinterest.html")
    else:
        return render(request,"rateofinterest.html")