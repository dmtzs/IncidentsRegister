from django.shortcuts import render
from .models import PageModel

# Create your views here.
def PageReq(request, slug):
    PagePy= PageModel.objects.get(slug=slug)
    return render(request, "pages/page.html",{
        "PagePy": PagePy
    })