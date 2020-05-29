from django.shortcuts import render,redirect
from .models import Liberian,Book,Genre,Author,Book_Allotment,Series,Language,Publisher,Member,Settings
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index0(request):
    context = {"categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    return render(request,'index0.html', context)
@login_required
def index(request):
    context = {"categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    return render(request,'index.html', context)
@login_required
def book_list(request):
    book=Book.objects.all()
    paginator= Paginator(book,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj, "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all(), "reviews":range(0,Book.objects.all().values_list('review')[0][0])}
    if request.method == 'POST':
        image = request.FILES['image']
        isbn = request.POST['isbn']
        title = request.POST['title']
        summary = request.POST['summary']
        author = request.POST['author']
        genre = request.POST['genre']
        total_copies = request.POST['total_copies']
        avail_copies= request.POST['avail_copies']
        position=request.POST['position']
        book_id = title


        if Book.objects.filter(title=title).exists():
            context = {"page_obj":page_obj,"message": "Book Already Exist", "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all(), "reviews":range(0,Book.objects.all().values_list('review')[0][0])}
            return render(request, 'book-list.html', context)
        else:
            book = Book.objects.create(pic=image, isbn=isbn,title=title, summary=summary, author=author, genre=genre, total_copies=total_copies, available_copies=avail_copies, position=position)
            book.save()
            context = {"page_obj":page_obj,"messages": "Book Added", "reviews":range(0,Book.objects.all().values_list('review')[0][0])}
            if Genre.objects.filter(name=name).exists():
                pass
            else:
                new_genre=Genre.objects.create(name=genre)
                new_genre.save()
            if Author.objects.filter(name=name).exists():
                pass
            else:
                new_author=Author.objects.create(full_name=author, email="nil")
                new_author.save()
            return redirect("book-list.html",context)
    return render(request,'book-list.html', context)
@login_required
def book_allotment(request):
    context = {"books": Book_Allotment.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        if request.POST.get("no_del")=="False":
            book_title=request.POST['book_title']
            book_number=request.POST['book_number']
            member=request.POST['member']
            email=request.POST['email']
            issue_date=request.POST['issue_date']
            return_date=request.POST['return_date']
            book_status=request.POST['status']
            allotment=Book_Allotment.objects.create(book_title=book_title, book_number=book_number,book_status=book_status, member=member, email=email, issue_date=issue_date, return_date=return_date)
            allotment.save()

            alot_remove=Book.objects.get(title=book_title).available_copies
            number=Book_Allotment.objects.filter(book_title=book_title).count()
            quantity=alot_remove-number
            data=Book.objects.get(title=book_title)
            data.available_copies=quantity
            data.save()
            return redirect('book-allotment.html', context)
        elif request.POST.get("del")=="True":
            title=request.POST['home']
            member=request.POST['real']
            data=Book_Allotment.objects.filter(member=member)
            data.delete()
            number=Book.objects.get(title=title)
            alot_remove=Book.objects.get(title=title).available_copies
            quantity=alot_remove+1
            number.available_copies=quantity
            number.save()
            return render(request,'book-allotment.html', context)
        else:
            return redirect('book-allotment.html', context)
    return render(request,'book-allotment.html', context)
@login_required
def book_series(request):
    context = {"books": Series.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        name=request.POST['name']
        if Series.objects.filter(name=name).exists():
            return redirect("series.html", context)
        else:
            series=Series.objects.create(name=name)
            series.save()
            return redirect("series.html", context)
    return render(request,'series.html', context)
@login_required
def book_genre(request):
    context = {"books": Genre.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        name=request.POST['name']
        if Genre.objects.filter(name=name).exists():
            return redirect("genre.html", context)
        else:
            genre=Genre.objects.create(name=name)
            genre.save()
            return redirect("genre.html", context)
        return redirect("genre.html", context)
    return render(request,'genre.html', context)
@login_required
def book_lang(request):
    context = {"books":Language.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        name=request.POST['name']
        code=request.POST['code']
        if Language.objects.filter(name=name).exists():
            return redirect("language.html", context)
        else:
            lang=Language.objects.create(name=name, code=code)
            lang.save()
            return redirect("language.html", context)
        return redirect("language.html", context)
    return render(request,'languages.html', context)
@login_required
def members(request):
    context = {"books": Member.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        address=request.POST['address']
        phone_number=request.POST['phone_number']
        if Member.objects.filter(full_name=full_name).exists() or Member.objects.filter(email=email).exists():
            return redirect("members.html", context)
        else:
            member=Member.objects.create(full_name=full_name, email=email, address=address,phone_number=phone_number)
            member.save()
            return redirect("members.html", context)
    return render(request,'members.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index.html")
        else:
            return render(request, 'login.html', {"message": "The user does not exist"})
    else:
        return render(request,'login.html')
@login_required
def roles(request):
    context = {"liberians": Liberian.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        Liberian_id = username

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                context = {"liberians": Liberian.objects.all(),"message": "User Already Exist", "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
                return render(request, 'roles.html', context)
            else:
                user = User.objects.create(
                    username=username, password=password1, email=email)
                user.set_password(user.password)
                user.save()
                profile = Liberian.objects.create(user=user, name=full_name,username=username, address=address, phone_number=phone_number)
                profile.save()
                context = {"liberians": Liberian.objects.all(),"messages": "User Added", "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}

                return redirect("roles.html",context)
    return render(request,'roles.html', context)
@login_required
def publisher(request):
    context = {"books": Publisher.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        if Publisher.objects.filter(full_name=full_name).exists() or Publisher.objects.filter(email=email).exists():
            return redirect("publishers.html", context)
        else:
            publisher=Publisher.objects.create(full_name=full_name, email=email)
            publisher.save()
            return redirect("publishers.html", context)
    return render(request,'publishers.html',context)
@login_required
def author(request):
    context = {"books": Author.objects.all(), "categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    if request.method == 'POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        if Author.objects.filter(full_name=full_name).exists() or Author.objects.filter(email=email).exists():
            return redirect("authors.html", context)
        else:
            author=Author.objects.create(full_name=full_name, email=email)
            author.save()
            return redirect("authors.html", context)
    return render(request,'authors.html', context)
@login_required
def e_settings(request):
    context= {"categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    settings=Settings.objects.get()
    if request.method == 'POST':
        image = request.FILES.get('image')
        name= request.POST.get("name")

        settings.image=image
        settings.name=name
        settings.save()
        return redirect('settings.html',context)
    return render(request,'settings.html',context)
@login_required
def logout(request):
    auth.logout(request)
    return redirect("login.html")

@login_required
def contact(request):
    context= {"categ":Genre.objects.all(), "lists":Genre.objects.all(), "details":Settings.objects.all()}
    return render(request, 'contacts.html',context)
@login_required
def search_book(request):
    context= {"categ":Genre.objects.all(), "lists":Genre.objects.all()}
    found_entries = None
    if request.method=='POST':
        if request.POST.get('search')=='search':
            entry_query = request.POST['q']
            context={"categ":Genre.objects.all(), "lists":Genre.objects.all(),"book_list":Book.objects.all().filter(title=entry_query),"authors":Author.objects.all().filter(full_name=entry_query),"allotments":Book_Allotment.objects.all().filter(book_title=entry_query),"genres":Genre.objects.all().filter(name=entry_query),"languages":Language.objects.all().filter(name=entry_query),"members":Member.objects.all().filter(full_name=entry_query),"publishers":Publisher.objects.all().filter(full_name=entry_query),"series":Series.objects.all().filter(name=entry_query),"roles":Liberian.objects.all().filter(name=entry_query)}
            return render(request,'search.html',context)

        return render(request,'search.html',context)
    return render(request,'search.html',context)


def anon_search(request):
    context= {"categ":Genre.objects.all(), "lists":Genre.objects.all()}
    found_entries = None
    if request.method=='POST':
        if request.POST.get('search')=='search':
            entry_query = request.POST['q']
            context={"categ":Genre.objects.all(), "lists":Genre.objects.all(),"book_list":Book.objects.all().filter(title=entry_query)}
            return render(request,'search-free.html',context)

        return render(request,'search-free.html',context)
    return render(request,'search-free.html',context)
