from django.contrib import admin
from django.shortcuts import HttpResponse,render, redirect
from django.urls import path
from .models import Reader,BookModel,Bookshop,StudentId,coll,Showroom,Union
from django.db.models import Avg,Max,Min,Sum,Count
from .movies import df
from .bank import  readfromexcel,getAccount as gt 


def test(request):
    df=readfromexcel()
    print(df)
    account=df["name"]
    # print(account)
    return HttpResponse("Test<br>" + str(df))

def GetAccount(request):
    accountno=""
    if request.GET:
        accountno=request.GET["acccountno"]
        x=gt(101)
        print(x)

    
    return HttpResponse('GetAccount')










def index(request):
    return HttpResponse('hi')

def book(request):
    bookname=""
    subject=""
    price=""
    print("test")
    detail=BookModel.objects.all()
    # bookname=detail.bookname
    # subject=detail.subject
    # price=detail.price
    
    # print(bookname)
    # print(subject)
    # print(price)
    # return render(request,"allbook.html",{"bookname":bookname,"subject":subject,"price":price})
    return render(request,"book.html",{"books":detail,"title":"All Books"})



def between(request):
    # data = BookModel.objects.all().order_by('bookname')
    # data = BookModel.objects.all().order_by(Lower('bookname').desc())

    # data = BookModel.objects.all().order_by(Coalesce('bookname','bookname').desc())


    data = BookModel.objects.filter(price__lt =1000) & BookModel.objects.filter(price__gt =100)  .order_by('bookname').reverse()
    return render(request, "book.html", {'books': data, "title": "Less than and greater than"})


def searchbooks(request):
    data = Bookshop.objects.filter(subject="2")
    return render(request, "book.html", {'books': data, "title": "Search Subject"})



def searchor(request):
    data = Bookshop.objects.filter(subject="2") | Bookshop.objects.filter(subject="1")
    return render(request, "book.html", {'books': data, "title": "Search Subject Or"})


def aggregates(request):
    print("Aggregates")
    data = (BookModel.objects.filter(subject="django") | BookModel.objects.filter(subject="1")) #.aggregate(Avg('price'))
    print(data)
    # data = BookModel.objects.aggregate(Avg('price'), Max('price'), Min('price'),Sum('price'),Count('price'))
    return render(request, "book.html", {'books': data, "title": "Aggregatess"})

#  price name search................

def betweens(request):
    lower=""
    if request.GET:
         lower=request.GET["lower"]

         data = BookModel.objects.filter(price__lt =lower) & BookModel.objects.filter(price__gt =100)  .order_by('bookname').reverse()
         print(data)
    return render(request, "betweens.html", {'lower':lower})


# subject name search........

def allbooks(request):
    subject="2"
    print("test")
    if request.GET:
       data = Bookshop.objects.filter(subject=2)
       print("data")
       print(data)
    return render(request, "allbook.html", {'subject':subject})

# subject name search........

def aggregate(request):
    subject=""
    print("Aggregates")
    if request.GET:
        subject=request.GET["subject"]
        data = (BookModel.objects.filter(subject=subject) | BookModel.objects.filter(subject="1")) #.aggregate(Avg('price'))
        print("test")
        print(data)
        print("test")
    return render(request, "books.html", {'subject': subject})


# bookname search .........
def books(request):
    bookname=""
    data=""
    if request.GET:
        bookname=request.GET["bookname"]
        data=(Bookshop.objects.filter(bookname=bookname)) 
        print(data)
    return render(request,"combin.html",{"bookname":bookname,"data":data})



# dropdown...........

def drop(request):
    subjects=""
    data=""
    if request.GET:
        subjects= request.GET["subjects"]
        data = Bookshop.objects.filter(subject=subjects)
        print(data)
    return render(request, "select.html", {'subjects':subjects,"data":data})




# delete........................

def delete(request):
    bookname=""
    data=""
    if request.GET:
        bookname=request.GET["bookname"]
        data=BookModel.objects.filter(bookname=bookname).first()
        data.delete()
        print(data)
    return render(request,"rendar.html",{"bookname":bookname,"data":data})





# new........................
def insert(request):
    car=""
    bike=""
    if request.GET:
        car=request.GET["car"]
        bike=request.GET["bike"]
        q=Showroom()
        q.car=car
        q.bike=bike
        q.save()
    return render(request,'insert.html',{"bike":bike,"car":car})






def search1(request):
    car=""
    data=""
    if request.GET:
        car=request.GET["car"]
        data=Showroom.objects.filter(car=car)
        print(data)
    return render(request,'search1.html',{"car":car,"data":data})






def remove(request):
    bike=""
    data=""
    result=''
    if request.GET:
        bike=request.GET["bike"]
        data=Showroom.objects.filter(bike=bike)
        x=len(data)
        print(x)
        if(x<=0):
            result="No record found"
        else:
            result='{0} records deleted'.format(x)
            print(result)
            while x>0:
                data.first().delete()
                x-=1
        print(data)
    return render(request,'remove.html',{"data":data,"bike":bike,"result":result})







def update(request):
    car=""
    data=""
    if request.GET:
        car=request.GET["car"]
        # bike=request.GET["bike"]
        data=Showroom.objects.filter(car=car)
        x=data.first()
        x.car="9090"
        x.bike="oimniooiuhu"
        x.save()
        print(data)
    return render(request,"update.html",{"car":car,"data":data})




# bank ....................

def bank(request):
    accountno=""
    name=""
    balance=""
    if request.GET:
        accountno=request.GET["accountno"]
        name=request.GET["name"]
        balance=request.GET["balance"]
        q=Union()
        q.accountno=accountno
        q.name=name
        q.balance=balance
        q.save()
    return render(request,"insert1.html",{"accountno":accountno,"name":name,"balance":balance})



def searchbank(request):
    accountno=""
    name=""
    balance=""
    data=""
    result=""
    if request.GET:
        accountno=request.GET["accountno"]

        name=request.GET["name"]
        balance=request.GET["balance"]
        data=Union.objects.filter(accountno=accountno,name=name,balance=balance)
    return render(request,"searchbank.html",{"accountno":accountno,"name":name,"balance":balance,"data":data,"result":result})


def searchaccount(request):
    accountno=""
    data=""
    result=""
    if request.GET:
        accountno=request.GET["accountno"]
        data=Union.objects.filter(accountno=accountno)
        x=len(data)
        print(x)
        if x<=0:
            result="no account"
        else:
            result="found"
    return render(request,"searchaccount.html",{"accountno":accountno,"data":data,"result":result})



def deleteaccount(request):
    accountno=""
    data=""
    if request.GET:
        accountno=request.GET["accountno"]
        data=Union.objects.filter(accountno=accountno)
        x=len(data)
        if x<=0:
            result="no record"
        else:
            result="{0} record deleted".format(x)
            print(result)
            while x>0:
                data.first().delete()
                x-=1
        print(data)
    return render(request,"deleteaccount.html",{"accountno":accountno,"data":data,"result":result})



def updateaccount(request):
    accountno=""
    data=""
    if request.GET:
        accountno=request.GET["accountno"]
        data=Union.objects.filter(accountno=accountno)
        x=data.first()
        x.name="sushil"
        x.save()
    return render(request,"updateaccount.html",{"accountno":accountno,"data":data})




# pandas.....................

def moviesearch(request):
    name=""
    data=""
    if request.GET:
        name=request.GET["name"]
        # print(name)   
        data=df[df['name'].str.contains('Man',case=False)]
        print(data)
    # return HttpResponse('movie')

    return render(request,"pandas.html",{"name":name,"data":data})


# excle................

def readexcle(request):
    pf=pd.read_excel("data/bank.xlsx" ,index_col=0)
    print(pf)
    return HttpResponse("pd")




   

    






