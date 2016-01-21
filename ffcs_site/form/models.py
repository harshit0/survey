from django.db import models

class PersonalInfo(models.Model):
	Gender_Choices = (('M','Male'),('F','Female'))
	First_Name = models.CharField(max_length = 30)
	Middle_Name = models.CharField(max_length = 30)
	Last_Name = models.CharField(max_length = 30)
	sex = models.CharField(max_length = 1, choices= Gender_Choices)
	Registration_ID = models.CharField(max_length = 9, 
				unique = True, 
				help_text = 'Your College ID')

	def __str__(self):
		return ('%s %s' % (Registration_ID,First_Name))

class AcademicRecord(models.Model):
	Class_X = models.DecimalField(
			max_digits = 2, 
			decimal_places= 2
		)
	Class_XII = models.DecimalField(
				max_digits = 2, 
				decimal_places= 2
		)
	UG = models.DecimalField(
				max_digits = 2, 
				decimal_places= 2, 
				help_text = 'CGPA upto 1 decimal place'
		)
	PG = models.DecimalField(
				max_digits = 2, 
				decimal_places = 2
		)
	Resume = models.FileField(
				upload_to = '/home/ubuntu/djcode/ffcs_site/',
				help_text = 'Upload your updated resume'
		)

class TopicOfInterest(models.Model):
	Topics = models.CharField(max_length = 300)

class Project(models.Model):
	Title_Of_Project = models.TextField()
	Abstract = models.TextField()
	Keywords = models.TextField(
			help_text = 'Keywords related to your peoject separated by comma'
		)
	Interest = models.ManyToManyField(TopicOfInterest)

class ask(models.Model):
	answer = (('Y','Yes'),('N','No'))
	Project_Status = models.CharField(
			max_length = 1,
			choices = answer,
			help_text = 'choose yes if you have already done your project',
		)
