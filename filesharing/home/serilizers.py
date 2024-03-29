from rest_framework import serializers
from home.models import *
import shutil




class FileListSerilizers(serializers.Serializer):
	files = serializers.ListField(child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False))


	#  create zip function
	def createzip(self , folder):
		shutil.make_archive(f'public/static/zip/{folder}' , 'zip' , f'public/static/{folder}')

	def create(self , validate_data):
		folder = Folder.objects.create()
		files = validate_data.pop('files')
		for file in files:
			file_obj = folder.files.create(folder = folder , file=file)
			file_obj.append(file_obj)
		self.createzip(folder.uuid)

		return {'files' : {} , folder : str(Folder.uuid)}