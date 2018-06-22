from django import forms

class ChooseForm(forms.Form):
    CHOICES=[("Driver","Driver"),("Passenger","Passenger")]
    choice=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())