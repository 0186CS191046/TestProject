from django import forms
from .models import *

class SubmitForm(forms.Form):
    email                                       = forms.EmailField()
    full_name                                   = forms.CharField(max_length=30)
    age                                         = forms.IntegerField()
    highest_level_of_education                           = forms.ChoiceField(choices=highest_education)
    institute_where_you_completed_your_highest_level_of_education = forms.CharField(max_length=100)
    what_did_you_study                                       = forms.CharField(max_length=20)
    do_you_have_any_relevant_work_experience          = forms.CharField(max_length=20)
    what_institute_did_you_get_admitted_to_in_Canada = forms.CharField(max_length=100)
    what_is_your_program_of_study_in_Canada                  = forms.CharField(max_length=20)
    which_country_are_you_applying_from               = forms.CharField(max_length=20)
    what_are_your_future_goals                                = forms.CharField(max_length=30)
    english_scores_listening                           = forms.CharField(max_length=5)
    english_scores_reading                             = forms.CharField(max_length=5)
    english_scores_speaking                            = forms.CharField(max_length=5)
    english_scores_writing                           = forms.CharField(max_length=5)
    did_you_pay_your_first_year_tuition         = forms.ChoiceField(choices=radio_choices)
    how_much_tuition_fee_did_you_pay           = forms.CharField(max_length=7)
    did_you_do_a_GIC                              = forms.ChoiceField(choices=radio_choices)
    how_much_did_you_pay_towards_GIC            = forms.CharField(max_length=7)

    
    