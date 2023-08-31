from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from . models import *
from . forms import *


from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView


# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Registered succesefull.')
                return redirect('signin')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'web/signup.html')
def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Incorrect information')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')



# Create your views here.
def home(request):
    return render(request, 'web/home.html')






def news(request):
    newspost = News.objects.all().order_by("-id")
    context={
        
        "newspost":newspost
    }
    return render(request, 'web/news.html',context)
def newspost(request):
    newspost = NewsForm()
    if request.method == "POST":
        newspost = NewsForm(request.POST, files=request.FILES)
        if newspost.is_valid():
            newspost.save()
            messages.info(request, 'News posted succesefull.')
            return redirect('news')
    context={
        "newspost":newspost
    }
    return render(request, 'web/newspost.html',context)


# def viewnews(request, id):
#     new = News.objects.get(id=id)
#     form = CommentForm
    
#     context = {"new":new}
#     return render(request, 'web/viewnews.html', context)





class viewnews(DetailView):
    model = News
    template_name = 'web/viewnews.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()
            messages.success(request, "message sent successfully")

            return redirect(reverse("viewnews", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #to count number of comment
       # post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
#kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Comment.objects.all().filter(Title=self.object.id)
#zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context







def updatenews(request, id):
    e = News.objects.get(id=id)
    new = NewsForm(instance=e)
    if request.method == "POST":
        new = NewsForm(request.POST, files=request.FILES, instance=e)
        if new.is_valid():
            new.save()
            return redirect('news')
    context = {"new":new}
    return render(request, 'web/updatenews.html', context)
def deletenews(request, id):
    new = News.objects.get(id=id)
    if request.method == "POST":
        new.delete()
        messages.info(request, 'News deleted succesefull.')
        return redirect('news')
    
    context = {"new":new}
    return render(request, 'web/deletenews.html', context)


#   for Annoucement functions


def annouce(request):
    annoucepost = Annouce.objects.all().order_by("-id")
    context={
        
        "annoucepost":annoucepost
    }
    return render(request, 'web/annouce.html',context)
def annoucepost(request):
    annoucepost = AnnouceForm()
    if request.method == "POST":
        annoucepost = AnnouceForm(request.POST, files=request.FILES)
        if annoucepost.is_valid():
            annoucepost.save()
            messages.info(request, 'Annoucement posted succesefull.')
            return redirect('annouce')
    context={
        "annoucepost":annoucepost
    }
    return render(request, 'web/annoucepost.html',context)


# def viewnews(request, id):
#     new = News.objects.get(id=id)
#     form = CommentForm
    
#     context = {"new":new}
#     return render(request, 'web/viewnews.html', context)





class viewannouce(DetailView):
    model = Annouce
    template_name = 'web/viewannouce.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form1 = Comment1Form

    def post(self, request, *args, **kwargs):
        form1 = Comment1Form(request.POST)
        if form1.is_valid():
            Title = self.get_object()
            form1.instance.user = request.user
            form1.instance.Title = Title
            form1.save()
            messages.success(request, "message sent successfully")

            return redirect(reverse("viewannouce", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #to count number of comment
       # post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
#kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments1 = Comment1.objects.all().filter(Title=self.object.id)
#zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form1':self.form1,
                'post_comments1':post_comments1,
                # 'post_comments_count':post_comments_count,
            })
        return context


def updateannouce(request, id):
    e = Annouce.objects.get(id=id)
    annouc = AnnouceForm(instance=e)
    if request.method == "POST":
        annouc = AnnouceForm(request.POST, files=request.FILES, instance=e)
        if annouc.is_valid():
            annouc.save()
            return redirect('annouce')
    context = {"annouc":annouc}
    return render(request, 'web/updateannouce.html', context)
def deleteannouce(request, id):
    annouc = Annouce.objects.get(id=id)
    if request.method == "POST":
        annouc.delete()
        messages.info(request, 'Annoucement deleted succesefull.')
        return redirect('annouce')
    
    context = {"annouce":annouce}
    return render(request, 'web/deleteannouce.html', context)
    
#   end of Annoucement functions
    
    
def books(request):
    return render(request, 'web/books.html')
def constitution(request):
    return render(request, 'web/constitution.html')
def contact(request):
    return render(request, 'web/contact.html')
def about(request):
    return render(request, 'web/about.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('Full_Name')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')
        Country = request.POST.get('Country')
        Phone = request.POST.get('Phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            messages.info(request, 'Message sent succesefull.')
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
def contactlist(request):
    contactlist = Contact.objects.all().order_by("-id")
    count= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "count":count
    }
    return render(request, 'web/contactlist.html', context)

def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)

def deletecontact(request, id):
    contactdelete = Contact.objects.get(id=id)
    # if request.method == "POST":
    contactdelete.delete()
    messages.info(request, 'Message deleted succesefull.')
    return redirect('contactlist')

def uploadconstitution(request):
    uploadconstitution = ConstitutionForm()
    if request.method == "POST":
        uploadconstitution = ConstitutionForm(request.POST, files=request.FILES)
        if uploadconstitution.is_valid():
            uploadconstitution.save()
            messages.info(request, 'Constitution uploaded succesefull.')
            return redirect('uploadconstitution')
        return redirect("uploadconstitution")
    context={
        "uploadconstitution":uploadconstitution
    }
    return render(request, 'web/uploadconstitution.html',context)

def constitution(request):
    constitution = Constitution.objects.all().order_by("-id")
    context={
        "constitution":constitution
    }
    return render(request, 'web/constitution.html', context)

def deleteconstitution(request, id):
    constitutiondelete = Constitution.objects.get(id=id)
    constitutiondelete.delete()
    messages.info(request, 'Constitution deleted succesefull.')
    return redirect('constitution')

def files(request):
    files = MyfileForm()
    if request.method == "POST":
        files = MyfileForm(request.POST, files=request.FILES)
        if files.is_valid():
            files.save()
            messages.info(request, 'Book added succesefull.')
            return redirect('files')
        return redirect("home")
    context={
        "files":files
    }
    return render(request, 'web/files.html',context)


def filesdisplay(request):
    filesdisplay = Myfile.objects.all().order_by("-id")
    countfile= Myfile.objects.all().count()
    context={
        "filesdisplay":filesdisplay,
        "countfile":countfile
    }
    return render(request, 'web/filesdisplay.html', context)


def viewfiles(request, id):
    fileview = Myfile.objects.get(id=id)
    
    context = {"fileview":fileview}
    return render(request, 'web/viewfiles.html', context)


def deletefiles(request, id):
    filesdelete = Myfile.objects.get(id=id)
    filesdelete.delete()
    messages.info(request, 'Book deleted succesefull.')
    return redirect('filesdisplay')

def leader(request):
    return render(request, 'web/leader.html')

def subscribers(request):
    return render(request, 'web/subscribers.html')

