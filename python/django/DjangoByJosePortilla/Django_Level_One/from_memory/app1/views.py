from django.shortcuts import render


# Create your views here.

def index(request):
    index_dict = {
        'ins_indx': "<em>Inserting Part 1</em>",
        'ins_indx2': "Inserting Part 2",
    }
    return render(request,'app1/index.html',context=index_dict)
