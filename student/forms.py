from django import forms 


class StudentForm(forms.Form):
    id=forms.IntegerField(label='student id')
    f_name=forms.CharField(max_length=30)
    l_name=forms.CharField(max_length=30)
    age=forms.IntegerField()