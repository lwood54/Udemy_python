from django.shortcuts import render
# from newApp.models import User ----> from previous CHALLENGE
from newApp.forms import NewUserForm
# Create your views here.
def index(request):
    index_dict = {'ins_indx1':"Hello, from the index of newApp."}
    return render(request,'newApp/index.html',context=index_dict)

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR, FORM INVALID")

    return render(request, 'newApp/users.html', {'form':form})




    ### FROM ORIGINAL CHALLENGE:
    # user_list = User.objects.all()
    # users_dict = {'ins_user_list': user_list}
    # return render(request,'newApp/users.html',context=users_dict)
