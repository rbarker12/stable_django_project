from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from results.models import Events
from django.utils import timezone

class Home(TemplateView):
    template_name = "index.html"
    
class EmailForm(forms.Form):
    subject = forms.CharField()
    
class EmailPage(FormView):
    template_name = "index.html"
    form_class = EmailForm
    success_url = ''
    
    def post(self,request,*args,**kwargs):
        form - self.get_form()
        if form.is_valid():
            print('form is valid')
            print(self.request.POST)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
   
