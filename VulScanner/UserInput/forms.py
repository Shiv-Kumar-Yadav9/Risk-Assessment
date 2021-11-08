from django.forms import modelformset_factory
from .models import Asset, Threat

AssetFormSet = modelformset_factory(
    Asset, fields=("asset_name", "asset_version"), extra=1
)

ThreatFormSet = modelformset_factory(
    Threat, fields=("threat_name",), extra=1
)