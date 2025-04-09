from django.db import models

# Create your models here.
class BookModel(models.Model):
    bookname=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    price=models.IntegerField()
    
    
    def __str__ (self):
        return "Book Name is {0}".format(self.bookname,self.subject,self.price)
    
    
class StudentId(models.Model):
        name=models.CharField(max_length=100)
        roll=models .IntegerField()
        branch=models.CharField(max_length=100)
        
        def __str__ (self):
            return "name={0}, roll={1}, branch={2}".format(self.name,self.roll,self.branch)


class coll(models.Model):
    name=models.CharField(max_length=200)
    classroom=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    
    def __str__(self):
        return " collage name is {0}".format(self.name,self.classroom,self.address)
    
    
    
    
subjects = (
    (1, "C"),
    (2, "Java"),
    (3, "Python"),
)
        # HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".

class Bookshop(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.IntegerField(choices=subjects, default=1)

    price = models.IntegerField()
    cover = models.ImageField(upload_to="static/")

    def __str__(self):
        return "Book Name={0}, Subject={1}, Price={2} ".format( self.bookname,self.subject,self.price)
    
    
    

class Reader(models.Model):
    bookname=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    #  new 
    
class Showroom(models.Model):
    car=models.CharField(max_length=200)
    bike=models.CharField(max_length=200)
    
    def __str__(self):
        return "car={0},bike{1}".format(self.car,self.bike)





class Union(models.Model):
    accountno=models.IntegerField()
    name=models.CharField(max_length=200)
    balance=models.IntegerField()
    
    def __str__(self):
        return "bank detail{0}".format(self.accountno,self.name,self.balance)
