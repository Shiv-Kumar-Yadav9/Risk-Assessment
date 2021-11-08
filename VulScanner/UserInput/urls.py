from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('Home', views.home, name='home'),
	path('Team', views.team, name='team'),
	path('Assets', views.assets.as_view(), name='Vulnerability-Listing'),
	#path('add', AssetAddView.as_view(), name="add_asset"),
    #path('', AssetListView.as_view(), name="asset_list")
	#path('add', views.AssetAddView.as_view(), name="add_asset"),
    path('', views.AssetListView.as_view(), name="asset_list")
]