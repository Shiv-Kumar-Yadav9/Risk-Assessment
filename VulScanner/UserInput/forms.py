from django.forms import modelformset_factory
from .models import Asset

AssetFormSet = modelformset_factory(
    Asset, fields=("asset_name", "asset_version"), extra=1
)