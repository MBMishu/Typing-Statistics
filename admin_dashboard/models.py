from django.db import models
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import FileExtensionValidator

# Create your models here.


class AdminUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    role = models.ForeignKey(
        Group, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class GuestUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    role = models.ForeignKey(
        Group, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class UserData(models.Model):
    # user = models.ForeignKey(
    #     GuestUser, null=True, blank=True, on_delete=models.SET_NULL)

    # pdf_name = models.CharField(max_length=200, null=True)
    word_count = models.CharField(max_length=200, null=True)
    character_count = models.CharField(max_length=200, null=True)
    typing_time = models.CharField(max_length=200, null=True)
    inactive_time = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


def upload_to(instance, filename):
    return 'pdf_files/{0}'.format(filename)


class PDFFile(models.Model):
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to=upload_to, validators=[
                            FileExtensionValidator(allowed_extensions=['pdf'])])
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def PdfURL(self):
        try:
            url = self.file.url
        except:
            url = ''

        return url

    def __str__(self):
        return self.file.name


class FormData(models.Model):
    user = models.ForeignKey(
        GuestUser, null=True, blank=True, on_delete=models.SET_NULL)

    pdf_name = models.ForeignKey(
        PDFFile, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    typingTime = models.IntegerField()
    inactiveTime = models.IntegerField()
    wordCount = models.IntegerField()
    charCount = models.IntegerField()
