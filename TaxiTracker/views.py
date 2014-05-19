from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpRequest, QueryDict, HttpResponseRedirect
from .forms import SubmitForm
from django.template import RequestContext
from .models import taximap
from django.db.models import Q
from django.utils import simplejson

def QueryMap(request):
    return render_to_response('querymap.html', locals())

def ajax_checks_area(request):
    if request.is_ajax():
      q = request.GET.get('q') #lat
      x = request.GET.get('x') #lng
      if q is not None: #Makes sure something is sent
        results = taximap.objects.filter(nelat__gte=q ,nelng__gte=x, swlat__lte=q, swlng__lte=x).order_by('companyname') #queries to see if marker location is in a service area
        return render_to_response("results.html", {"results":results})  #return results dictionary + results template
    return render_to_response('results.html', context_instance = RequestContext(request)) 

def MarkMap(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST  or None)
        if form.is_valid():
            new_publisher=form.save
            companyname = form.cleaned_data['companyname']
            nelat = form.cleaned_data['nelat']
            nelng = form.cleaned_data['nelng']
            swlat = form.cleaned_data['swlat']
            swlng = form.cleaned_data['swlng']
            p=taximap( #Contents of the new row taken from form on markmap.html
                companyname=companyname,
                nelat=nelat,
                nelng=nelng,
                swlat=swlat,
                swlng=swlng
                )
            p.save() #Adds row to database
            return HttpResponseRedirect('')
        else:
            form.errors
    return render_to_response('markmap.html', locals(), context_instance = RequestContext(request))
