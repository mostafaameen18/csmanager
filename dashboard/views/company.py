from .__init__ import *

def company(request, company):
    company = Company.objects.get(user=request.user, subdomain=company)
    print(company.name)
    

    return HttpResponse('welcome')