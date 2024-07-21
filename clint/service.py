from clint.models import Clint_management

def clint_details(request):
    detail = Clint_management(

            name                                = request.POST["name"],
            address                             = request.POST["address"],
            contact                             = request.POST["contact"],
            email                               = request.POST["email"],
            pan                                 = request.POST["pan"],
            company_id                          = request.POST["company_id"]

    )


def new_func():
    clint_details.save()
    return "success"