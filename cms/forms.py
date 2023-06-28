from django import forms
from .models import TimeSlot
from datetime import date

#
class DateInput(forms.DateInput):
    input_type = "date"
    
    
class AddTimeSlot(forms.Form):
    TIME_CHOICES = (
    ("8 AM", "8 AM"),
    ("8:30 AM", "8:30 AM"),
    ("9 AM", "9 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10 AM", "10 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11 AM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2 PM", "2 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    )

    POST_GRADUATE_TIME = (
        ("8 AM - 9 AM", "8 AM - 9 AM"),
        ("9 AM - 10 AM", "9 AM - 10 AM"),
        ("10 AM - 11 AM", "10 AM - 11 AM"),
        ("11 AM - 12 PM", "11 AM - 12 PM"),
        ("12 PM - 1 PM", "12 PM - 1 PM"),
        ("1 PM - 2 PM", "1 PM - 2 PM"),
        ("2 PM - 3 PM", "2 PM - 3 PM"),
        ("3 PM - 4 PM", "3 PM - 4 PM"),
        ("4 PM - 5 PM", "4 PM - 5 PM"),
        ("5 PM - 6 PM", "5 PM - 6 PM"),
    )
    Education_level = (
        ('Select Education level...', 'Select Education level...'),
        ('undergraduate', 'undergraduate'),
        ('postgraduate', 'postgraduate'),
    )
    slot_date = forms.CharField(label="Date", widget=forms.TextInput(
        attrs={"class": "form-control", "id": "slot_date", "value": date.today()}))
    education_level = forms.ChoiceField(label="Education Level", choices=Education_level,
                                        widget=forms.Select(attrs={"class": "form-control", "id": "levels"}))
    undergraduate_time = forms.ChoiceField(label="Undergraduate Time Slot", choices=TIME_CHOICES, widget=forms.Select(
        attrs={"class": "form-control", "id": "under_graduate"}))
    postgraduate_time = forms.ChoiceField(label="Postgraduate Time Slot", choices=POST_GRADUATE_TIME,
                                          widget=forms.Select(attrs={"class": "form-control", "id": "post_graduate"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['undergraduate_time'].required = False
        self.fields['postgraduate_time'].required = False