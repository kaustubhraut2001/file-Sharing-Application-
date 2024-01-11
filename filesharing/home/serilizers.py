from rest_framework import serializers
from .models import Folder




class FileListSerilizers(serializers.Serializer):
	files = serializers.ListField(child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False))

	def create(self , validate_data):
		folder = Folder.objects.create()
		files = validate_data.pop('files')
		for file in files:
			file_obj = folder.files.create(folder = folder , file=file)
			file_obj.append(file_obj)

		return file_obj