import form
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import Form, UserQuery
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

def index(request):

    if request.method=="POST":
        name = request.POST.get('name_')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        course = request.POST.get('course')

        form_object = Form(name=name, mobile=mobile, email=email,gender=gender,course=course)
        form_object.save()
        return redirect('forms')
    else:
        return render(request,'form/form.html')

    
class FormListView(ListView):
     model = Form
     template_name = 'form/form_list.html'
     context_object_name = 'forms'

class FormDetailView(DetailView):
    model = Form
    template_name = 'form/form_detail.html'
    context_object_name = 'form'

class FormUpdate(UpdateView):
    model = Form
    fields = ['name','mobile','email','gender','course']
    success_url = reverse_lazy('forms')

class FormDelete(DeleteView):
    model = Form
    success_url = reverse_lazy('forms')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserQueryList(ListView):
    model = UserQuery
    context_object_name = 'queries'

class UserQueryDetailView(DetailView):
    model = UserQuery
    template_name = 'form/userquery_detail.html'
    context_object_name = 'query'

