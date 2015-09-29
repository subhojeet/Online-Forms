from django.db import models

# Create your models here.

class user_table(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(unique=True,max_length=100)
	password = models.CharField(max_length=100)
	def __str__(self):
		return self.username

class user_info(models.Model):
	user = models.ForeignKey(user_table)
	group = models.ForeignKey('group_table',primary_key=True)
	first_name = models.CharField(max_length=200,null=True)
	last_name = models.CharField(max_length=200,null=True)

class group_table(models.Model):
	group_id = models.AutoField(primary_key=True)
	permissions = models.IntegerField()

class form_table(models.Model):
	user = models.ForeignKey(user_table)
	form_id = models.AutoField(primary_key=True)
	form_permissions = models.IntegerField()
	def __str__(self):
		return str(self.form_id)

class form_object_table(models.Model):
	form = models.ForeignKey(form_table,primary_key=True)
	response_url = models.CharField(max_length=100,unique=True)
	form_url = models.CharField(max_length=100,unique=True)
	form_title = models.CharField(max_length=200)
	form_description = models.CharField(max_length=500)
	flag = models.BooleanField("Form is Active or Not",default=True)
	class Meta:
		verbose_name = 'Form'
		verbose_name_plural = 'Forms'

class elements_table(models.Model):
	form_object = models.ForeignKey('form_object_table')
	elements_id = models.AutoField(primary_key=True)
	parent_id = models.IntegerField()
	Input = models.ForeignKey('input_object_table')
	required = models.BooleanField(default=False)
	description = models.TextField();
	title = models.CharField(max_length=1000)
	priority = models.IntegerField()
	def __str__(self):
		return str(self.elements_id)

class input_object_table(models.Model):
	input_id = models.AutoField(primary_key=True)
	input_type = models.CharField(max_length=100)
	def __str__(self):
		return self.input_type

class response_object_table(models.Model):
	user = models.ForeignKey(user_table)
	form = models.ForeignKey(form_table)
	elements = models.ForeignKey(elements_table)
	response_string = models.TextField()
	response_time = models.DateTimeField()

class choice(models.Model):
	elements = models.ForeignKey('elements_table')
	choice_id = models.AutoField(primary_key=True)
	choice_description = models.CharField(max_length=500)
	
