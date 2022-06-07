from urllib import response
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import PdfForm , CreateUserForm
from .models import Pdf
from django.http import HttpResponse , HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'pdf\ჭაბურღილი1.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response['content-Disposition'] = 'attachment; filename="pdf\ჭაბურღილი1.pdf'
            return response
    else:
        return HttpResponseNotFound('the requested pdf was not found in our server')


@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload_pdf.html', context)

@login_required
def pdf_list(request):
    pdfs = Pdf.objects.all()
    return render(request, 'pdf_list.html', {'pdfs': pdfs})


@login_required
def upload_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('class_pdf_list')
    else:
        form = PdfForm()
    return render(request, 'upload_pdf.html', {
        'form': form
    })

@login_required
def delete_pdf(request, pk):
    if request.method == 'POST':
        pdf = Pdf.objects.get(pk=pk)
        pdf.delete()
    return redirect('class_pdf_list')


class PdfListView(LoginRequiredMixin,ListView):
    model = Pdf
    template_name = 'class_pdf_list.html'
    context_object_name = 'pdfs'


class UploadPdfView(LoginRequiredMixin,CreateView):
    model = Pdf
    form_class = PdfForm
    success_url = reverse_lazy('class_pdf_list')
    template_name = 'upload_pdf.html'

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('class_pdf_list')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('class_pdf_list')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('login')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

