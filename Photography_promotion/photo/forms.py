from django import forms
from .models import Photographers, Appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['pname', 'date', 'time']
        labels = {'pname': 'Photographer', 'date': 'Date', 'time': 'Time'}
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
                   'time': forms.TimeInput(attrs={'type': 'time'})}
        '''This form is used to create a new appointment. 
        It is a ModelForm that will be used to create a new appointment object.
        It includes fields for the photographer, date, and time of the appointment. 
        The labels attribute is used to provide custom labels for the form fields, 
        and the widgets attribute is used to specify the input type for the date and time fields.
        The date field is rendered as a date input, and the time field is rendered as a time input. 
        This form will be used in the appointment creation view to allow users to schedule appointments with photographers.'''

