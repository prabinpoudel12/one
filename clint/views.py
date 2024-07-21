from django.shortcuts import redirect, render

# Create your views here.
# Create your views here.
from clint import service

def create_somthing(request):
    return render(request,"clint/index.html")

def clint_save(request):
    store =service.clint_details(request)
    return redirect("somthing_listing")






# def list_somthing(request):
#     clin = personlData.objects.all()  # Use 'all()' to get all records
#     data = {
#         'students': students,  # Update the key to plural form to reflect multiple records
#     }
#     return render(request, "curd/list.html", data)

