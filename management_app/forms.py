from django import forms
from .models import FeedBackStudent, FeedBackStaff


class FeedBackStudentForm(forms.ModelForm):
    theme = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Тема обращения',
                                                                    'class': 'form-control'}))
    feedback = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Ваш отзыв',
                                                                      'rows': 3, 'cols': 50,
                                                                      'class': 'form-control'}))

    class Meta:
        model = FeedBackStudent
        fields = ('theme', 'feedback',)


class FeedBackStaffForm(forms.ModelForm):
    class Meta:
        model = FeedBackStaff
        fields = ('theme', 'feedback',)
