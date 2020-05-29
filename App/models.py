from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title=models.TextField()
    isbn = models.IntegerField()
    summary= models.TextField()
    author = models.TextField()
    position=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    language=models.TextField()
    total_copies=models.IntegerField()
    available_copies=models.IntegerField()
    pic=models.ImageField(blank=True, null=True)
    review=models.IntegerField()
    paginate_by = 2

    def __str__(self):
        return self.title

class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")
    code=models.CharField(max_length=200,
                            help_text="Enter the book's natural language code")

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book that is a Series")

    def __str__(self):
        return self.name

class Book_Allotment(models.Model):
    book_title=models.TextField()
    book_number=models.IntegerField()
    member=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    issue_date=models.TextField(null=True,blank=True)
    return_date=models.TextField(null=True,blank=True)
    book_status=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.book_title

class Member(models.Model):
    full_name=models.TextField()
    address=models.TextField()
    email=models.CharField(max_length=100)
    phone_number=models.IntegerField()


    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    full_name=models.TextField()
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Author(models.Model):
    full_name=models.TextField()
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Liberian(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    username=models.CharField(max_length=100, null=True,blank=True)
    name= models.CharField(max_length=100)
    address= models.TextField()
    phone_number=models.IntegerField()

class Settings(models.Model):
    image=models.ImageField(null=True,blank=True)
    name=models.TextField(null=True,blank=True)
