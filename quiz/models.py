from __future__ import unicode_literals
from django.db import models, transaction
from django.contrib.auth.models import (
AbstractBaseUser, PermissionsMixin, BaseUserManager

)
class School(models.Model):
    school_name = models.CharField(max_length=50)
    add_date= models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.school_name

class StudentManager(BaseUserManager):

    def _create_user(self, email_id, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email_id:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email_id, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stud_class = models.CharField(max_length=20)
    email_id = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    add_date = models.DateTimeField(auto_created=True)
    school_name = models.OneToOneField('School', on_delete=models.CASCADE)

    objects = StudentManager()

    USERNAME_FILED = 'email_id'

    def __str__(self):
        return self.roll_no+": "+self.first_name+" "+ self.last_name

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        return self

    constraints = [
        models.UniqueConstraint(fields=['email_id, phone_number'], name='Email Phone')
    ]

    class Meta:
        db_table='tbl_students'

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=20, blank=False)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    question = models.TextField(blank=False, max_length=500)
    options1 = models.TextField()
    options2 = models.TextField()
    options3 = models.TextField()
    options4 = models.TextField()
    correct_option = models.TextField()
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def  __str__(self):
        return self.question

class Feedback(models.Model):
    f_name = models.CharField(max_length=50)
    feedback = models.TextField()

    def __str__(self):
        return self.f_name


    # Superuser: laksh
    # Laksh@123
