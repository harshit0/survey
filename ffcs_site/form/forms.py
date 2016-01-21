from models import PersonalInfo, Project, AcademicRecord, TopicOfInterest, ask
from django.forms import ModelForm
from django import forms
class PersonalInfoForm(ModelForm):
	class Meta:
		model = PersonalInfo
		fields = '__all__'
class ProjectForm(ModelForm):
	Interest = forms.ModelMultipleChoiceField(
			queryset = TopicOfInterest.objects.all(), 
			required = False,
			widget = forms.CheckboxSelectMultiple,
		)

	class Meta:
		model = Project
		fields = '__all__'
class AcademicRecordForm(ModelForm):
	class Meta:
		model = AcademicRecord
		fields = '__all__'
class askForm(ModelForm):
	#Project_Status = forms.ModelChoiceField(
	#			choices = answer,
	#			empty_label = None,
	#			widget = forms.Select
	#)
	class Meta:
		model = ask
		fields = "__all__"
		widgets = {'Project_Status': forms.Select}
