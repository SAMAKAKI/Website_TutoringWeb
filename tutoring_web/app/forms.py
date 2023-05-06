# from django import forms
# from .models import *

# class CreateOpinionsForm(forms.ModelForm):
#     star_5 = forms.ChoiceField(widget=forms.RadioSelect(attrs={
#         'name': 'star',
#         'id': 'star-5',
#         'class': 'd-none star',
#         'value': '5',
#         'checked': True
#     }))
#     star_4 = forms.ChoiceField(widget=forms.RadioSelect(attrs={
#         'name': 'star',
#         'id': 'star-4',
#         'class': 'd-none star',
#         'value': '4',
#     }))
#     star_3 = forms.ChoiceField(widget=forms.RadioSelect(attrs={
#         'name': 'star',
#         'id': 'star-3',
#         'class': 'd-none star',
#         'value': '3',
#     }))
#     star_2 = forms.ChoiceField(widget=forms.RadioSelect(attrs={
#         'name': 'star',
#         'id': 'star-2',
#         'class': 'd-none star',
#         'value': '2',
#     }))
#     star_1 = forms.ChoiceField(widget=forms.RadioSelect(attrs={
#         'name': 'star',
#         'id': 'star-1',
#         'class': 'd-none star',
#         'value': '1',
#     }))
#     text_opinion = forms.CharField(widget=forms.Textarea(attrs={
#         'name': 'text-opinion',
#         'class': 'form-control resize',
#         'placeholder': 'Leave a comment here',
#         'id': 'floatingTextarea',
#     }))
    
#     class Meta:
#         model = Opinion