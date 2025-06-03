from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'short_description',  'live_url', 'github_url','is_featured']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 3}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields:
            if field not in ['is_featured']:  # Skip checkbox since we styled it above
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            
        
        # # Customize specific fields if needed
        # self.fields['featured_image'].widget.attrs.update({'class': 'form-control-file'})
        # self.fields['short_description'].widget = forms.Textarea(attrs={
        #     'class': 'form-control',
        #     'rows': 3
        # })

