from django.shortcuts import render
#from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from .models import Asset, Threat
from .forms import AssetFormSet, ThreatFormSet
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.
def index(request):
	return render(request, 'Index.html')

def home(request):
	return render(request, 'Home.html')

def team(request):
	return render(request, 'Team.html')
	
#def assets(request):
#	return render(request, 'Vulnerability-Listing.html')

class assets(TemplateView):
    template_name = "Vulnerability-Listing.html"

    def get(self, *args, **kwargs):
        formset = AssetFormSet(queryset=Asset.objects.none())
        return self.render_to_response({'asset_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = AssetFormSet(data=self.request.POST)
        
        if formset.is_valid():
            formset.save()
            print("Control saved")
            return redirect(reverse_lazy("Vulnerability"))
        print("Failure")
        return self.render_to_response({'asset_formset': formset})

class AssetListView(ListView):
    model = Asset
    template_name = "Vulnerability.html"

class threats(TemplateView):
    template_name = "Threat-Listing.html"

    def get(self, *args, **kwargs):
        formset = ThreatFormSet(queryset=Threat.objects.none())
        return self.render_to_response({'threat_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = ThreatFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("Threats"))

        return self.render_to_response({'threat_formset': formset})

class ThreatListView(ListView):
    model = Threat
    template_name = "Threats.html"

"""class AssetAddView(TemplateView):
    template_name = "add_asset.html"

    def get(self, *args, **kwargs):
        formset = AssetFormSet(queryset=Asset.objects.none())
        return self.render_to_response({'asset_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = AssetFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("Vulnerability"))

        return self.render_to_response({'asset_formset': formset})
"""