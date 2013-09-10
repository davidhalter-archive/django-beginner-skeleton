from django.shortcuts import render_to_response, redirect
from django import forms
from django.template import RequestContext

from . import models


class BankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Bank


def index(request):
    if request.method == 'POST':
        form = BankForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BankForm()  # An unbound form

    bank_list = models.Bank.objects.all().order_by('name')
    context = {'bank_form': form,
               'bank_list': bank_list,
               }
    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))


def show(request, id):
    bank = models.Bank.objects.get(id=id)

    return render_to_response('show.html', {'bank': bank},
                              context_instance=RequestContext(request))
