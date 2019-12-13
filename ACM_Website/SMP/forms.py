from django import forms
from acm.models import SIG


class PasswordForm(forms.Form):
    key = forms.CharField(max_length=100)


class SMPForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SMPForm, self).__init__(*args, **kwargs)
        MY_CHOICES = ()
        x = len(SIG.objects.all())
        for i in range(x):
            MY_CHOICES += ((i+1, str(SIG.objects.get(pk=i+1).name)),)
        print(MY_CHOICES)
        self.fields['SIG'] = forms.ChoiceField(choices=MY_CHOICES)
        self.fields['Name'] = forms.CharField(max_length=150)
        self.fields['Mentors'] = forms.CharField(max_length=150)
        self.fields['Overview'] = forms.CharField(max_length=400)
        self.fields['Platform'] = forms.CharField(max_length=100)

        self.fields['exercise_freq'] = forms.IntegerField(
            initial=1, widget=forms.HiddenInput())
        for i in range(10):
            self.fields['Exercise_' +
                        str(i+1)] = forms.CharField(max_length=200, required=False)
            if i is not 0:
                self.fields['Exercise_'+str(i+1)].widget = forms.HiddenInput()

        self.fields['prerequisite_freq'] = forms.IntegerField(
            initial=1, widget=forms.HiddenInput())
        for i in range(10):
            self.fields['Prerequisite_' +
                        str(i+1)] = forms.CharField(max_length=200, required=False)
            if i is not 0:
                self.fields['Prerequisite_' +
                            str(i+1)].widget = forms.HiddenInput()

        self.fields['course-content_freq'] = forms.IntegerField(
            initial=1, widget=forms.HiddenInput())
        for i in range(10):
            self.fields['Course-content_' +
                        str(i+1)] = forms.CharField(max_length=100, required=False)
            if i is not 0:
                self.fields['Course-content_' +
                            str(i+1)].widget = forms.HiddenInput()

        # for 8 weeks
        self.fields['week_freq'] = forms.IntegerField(
            initial=1, widget=forms.HiddenInput())
        for i in range(8):
            self.fields['week_' +
                        str(i+1) + '_description_freq'] = forms.IntegerField(initial=1, widget=forms.HiddenInput())

            for j in range(5):
                self.fields['Week_'+str(i+1)+'_Description_' +
                            str(j+1)] = forms.CharField(max_length=300, required=False)

                if (j is not 0):
                    self.fields['Week_'+str(i+1)+'_Description_' +
                                str(j+1)].widget = forms.HiddenInput()
