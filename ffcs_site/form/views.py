from django.shortcuts import render_to_response, redirect
from forms import ProjectForm, askForm, AcademicRecordForm, PersonalInfoForm
from django.template import RequestContext
def InitialView(request):
	if request.method == 'POST':
		form = askForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/step2/')
	else:
		form = askForm()
		return render_to_response("initial.html", 
				{'form': form},
				RequestContext(request)
			)

def ProjectView(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.Interest = request.Interest
			obj.save()
			return redirect('/step3/')
	else:
		form = ProjectForm()
		return render_to_response(
				'step2.html',
				{'form': form},
				RequestContext(request)
			)
def AcademicView(request):
	if request.method == 'POST':
		form = AcademicRecordForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/thank/')
	else:
		form = AcademicRecordForm()
		return render_to_response(
				'step3.html',
				{'form': form},
				RequestContext(request)
			)

	
def PersonalView(request):
	if request.method == 'POST':
		form = PersonalInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/initial/')
	else:
		form = PersonalInfoForm()
		return render_to_response(
				'info.html',
				{'form': form},
				RequestContext(request)
			)

def ThanksView(request):
	return render_to_response('thank.html', RequestContext(request))
