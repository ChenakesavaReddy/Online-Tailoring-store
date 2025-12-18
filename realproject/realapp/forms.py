from django import forms
from .models import Contact, Admin, AddNotification, Registration, Designer, DesignerGallery, DesignerService, Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields='__all__'

class AddNotificationForm(forms.ModelForm):
    class Meta:
        model=AddNotification
        exclude=['dataandtime']

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model=Registration
#         exclude = ['status']



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = Registration
        exclude = ['status']



class DesignerForm(forms.ModelForm):
    SPECIALIZATION_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
    ]

    specialization = forms.MultipleChoiceField(
        choices=SPECIALIZATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Designer
        exclude = ['status', 'otp']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_specialization(self):
        specializations = self.cleaned_data.get('specialization', [])
        return ','.join(specializations)


class DesignerGalleryForm(forms.ModelForm):
    class Meta:
        model = DesignerGallery
        fields = ['image']

class DesignerServiceForm(forms.ModelForm):
    class Meta:
        model = DesignerService
        fields = ['title', 'category', 'timeperiod', 'price', 'image']

class BookingForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Booking
        fields = ["scheduled_date", "notes"]

from .models import Review

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=0, max_value=5,
        widget=forms.NumberInput(attrs={'type': 'number', 'step': '1'})
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
