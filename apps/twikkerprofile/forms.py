from django import forms

from .models import TwikkerProfile

class TwikkerProfileForm(forms.ModelForm):
    class Meta:
        model = TwikkerProfile
        fields = ('avatar',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['avatar'].widget.attrs.update({'class': 'form-control'})
    #
    # def save(self, commit=True):
    #     twikkerprofile = super(TwikkerProfileForm, self).save(commit=False)
    #     twikkerprofile.user = self.user
    #     if commit:
    #         twikkerprofile.save()
    #     return twikkerprofile
    #
    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']
    #     if avatar:
    #         if avatar.size > 2 * 1024 * 1024:
    #             raise forms.ValidationError('Avatar file size may not exceed 2MB.')
    #     return avatar