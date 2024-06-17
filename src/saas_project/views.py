from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(requests,*args,**kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=requests.path)

    my_title="My Page"
    my_context= {
        "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count":qs.count()
    }
    path=requests.path
    print("path",path)
    html_template="home.html"
    PageVisit.objects.create(path=path)
    return render(requests,html_template,my_context)