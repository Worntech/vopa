from django.db import models
from statistics import mode
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# user table--------------------------------------------------------------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

     

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

# end user table -------------


# Create your models here.
class News(models.Model):
    Title = models.CharField(max_length=200, null=True)
    Content = models.CharField(max_length=3000, null=True)
    Image =models.ImageField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('News', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
class Annouce(models.Model):
    Title = models.CharField(max_length=200, null=True)
    Content = models.CharField(max_length=3000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Comment1(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Annouce', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
class Contact(models.Model):
    Full_Name = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=200, null=True)
    Country = models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=100, null=True)
    Message = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Subscribe(models.Model):
    Email = models.EmailField(max_length=200, null=True)

    
class Constitution(models.Model):
    constitution = models.FileField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Myfile(models.Model):
    Upload_Book = models.FileField(max_length=100, null=True)
    Book_Name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)