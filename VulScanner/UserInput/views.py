from django.shortcuts import render
#from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from .models import Asset
from .forms import AssetFormSet
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

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("asset_list"))

        return self.render_to_response({'asset_formset': formset})

class AssetListView(ListView):
    model = Asset
    template_name = "asset_list.html"

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
            return redirect(reverse_lazy("asset_list"))

        return self.render_to_response({'asset_formset': formset})
"""