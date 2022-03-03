from django.forms import ModelForm
from .models import Preferences, Status

class UpdateStatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['current_tab', 'keyboard_activity']

class UpdatePreferencesForm(ModelForm):
    class Meta:
        model = Preferences
        fields = ['show_current_tab', 'show_keyboard_activity']