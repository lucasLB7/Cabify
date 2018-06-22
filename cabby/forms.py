class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(froms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')