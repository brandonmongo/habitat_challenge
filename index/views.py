from django.shortcuts import render
from .models import tender_result
# Create your views here.


def index(request):

    tender_results = tender_result.objects.all()

    context = {
        "tender_results": tender_results,
    }

    return render(request, "index/index.html", context)

