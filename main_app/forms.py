from django.forms import ModelForm
from .models import GrabbedItem

class GrabForm(ModelForm):
    class Meta:
        model = GrabbedItem
        fields = ['item', 'rarity']