from django import forms

class UserUpdateForm(forms.ModelForm)
    class Meta:
        model = User
        fields = ['username','email']
        

