from django.shortcuts import render
from . import forms
# or... from basicapp import forms (this is essentially the same as line 2)

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE HERE
            # Example, but probably never normally do is print...
            print("VALIDATION SUCCESS!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'basicapp/form_page.html',{'form':form})
