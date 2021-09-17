from django.shortcuts import render
from .models import TenderResult
# Create your views here.


def index(request):

    tender_results = TenderResult.objects.all()

    context = {
        "tender_results": tender_results,
    }

    return render(request, "index/index.html", context)

