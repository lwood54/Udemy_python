from django.shortcuts import render


# Create your views here.

def index(request):
    ## I guess I can't add something like <em></em> unless
    ## it's an HttpResponse???
    my_dict = {'ins_cont': "Content from chal_proj/index.html!"}
    return render(request,'chal_proj_app/index.html',context=my_dict)
    # return HttpResponse("<em>Hello World!</em>")

def help(request):
    help_dict = {'ins_help': "Help Page!"}
    return render(request, 'chal_proj_app/help.html',context=help_dict)
