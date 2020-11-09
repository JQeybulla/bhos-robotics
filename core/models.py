from django.db import models

# Create your models here.

class Greeting(models.Model):
    title = models.CharField(max_length = 500)
    img = models.ImageField(upload_to='media')
    club_name = models.CharField(max_length = 500, default='Robotics Club')
    department_name = models.CharField(max_length=250, default='Process Automation Engineering')
    about_department = models.TextField(default='This is Department')
    about_club = models.TextField(default='This is club')
    about_teachers = models.TextField(default='This is techhers')
    about_students = models.TextField(default='This is students')
    students_count = models.PositiveIntegerField(default=0)
    teacher_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default='New event')
    date = models.DateField()

    def __str__(self):
        return self.title

class Social_Media_Link(models.Model):
    facebook = models.TextField()
    instagram = models.TextField()
    youtube = models.TextField()
    linkedin = models.TextField()

    def __str__(self):
        return "Media Links"

class Research(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField(default="This is body")
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=250)
    background_img = models.ImageField(upload_to='media')
    main_img = models.ImageField(upload_to='media')
    body = models.TextField(default='Body')
    partner_1_img = models.ImageField(upload_to='media')
    partner_1_link = models.TextField()
    partner_2_img = models.ImageField(upload_to='media')
    partner_2_link = models.TextField()
    partner_3_img = models.ImageField(upload_to='media')
    partner_3_link = models.TextField()
    faculty_text = models.TextField(default='Faculty')

class Vision(models.Model):
    title = models.CharField(max_length=250)
    background_img = models.ImageField(upload_to='media')

    goal_1_title = models.CharField(max_length=250)
    goal_1_body = models.TextField()
    goal_1_img = models.ImageField(upload_to='media')

    goal_2_title = models.CharField(max_length=250)
    goal_2_body = models.TextField()
    goal_2_img = models.ImageField(upload_to='media')

    goal_3_title = models.CharField(max_length=250)
    goal_3_body = models.TextField()
    goal_3_img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=250)
    background_img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=250)
    background_img = models.ImageField(upload_to='media')
    img = models.ImageField(upload_to='media')

    mail = models.EmailField()
    phone = models.CharField(max_length=500)
    


    
    def __str__(self):
        return self.title