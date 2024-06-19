from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Title")
    description= models.TextField(max_length=500, default="", blank=True, null=True, verbose_name="Project Description")
    image = models.ImageField(upload_to='project', verbose_name="Project Image")
    github_link= models.CharField(max_length=1000, verbose_name= "Github LinK")
    demo_link=models.CharField(max_length=1000, verbose_name= "Demo LinK")

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField(max_length=254, verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    summary= models.CharField(max_length=250, verbose_name="Summary")
    facebook_link = models.CharField(max_length=1000, verbose_name="Facebook Link")
    instagram_link = models.CharField(max_length=1000, verbose_name="Instagram Link")
    twitter_link = models.CharField(max_length=1000, verbose_name="twitterLink")
    linkedin_link = models.CharField(max_length=1000, verbose_name="LinkedIn Link")
    github_link = models.CharField(max_length=1000, verbose_name="Github Link")
    resume = models.FileField(upload_to='resume', verbose_name="Resume")
    profile_image = models.ImageField(upload_to='profile', verbose_name="Profile Image")
    about_image = models.ImageField(upload_to='profile', verbose_name="About Image")

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField(max_length=254, verbose_name="Email")
    message = models.TextField(max_length=1000, verbose_name="Message")

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Service Title")
    description = models.TextField(max_length=500, verbose_name="Service Description")
    icon = models.CharField(max_length=100, verbose_name="Service Icon")

    def __str__(self):
        return self.title