from django.db import models

class File(models.Model):
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    created = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.file.name

class Folder(models.Model):

    owner = models.ForeignKey('auth.User', related_name='folders', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name