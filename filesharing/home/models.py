from django.db import models
import uuid
import os

# Create your models here.
class Folders(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)

def getupload(instance,filename):
	return os.path.join(str(instance.folder.uuid),filename)

class files(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	file = models.FileField(upload_to=getupload)
	folder = models.ForeignKey(Folders, on_delete=models.CASCADE)