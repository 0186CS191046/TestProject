from django.db import models

# Create your models here.
highest_education=(
    ("grade 12", "Grade 12"),
    ("diploma", "Diploma"),
    ("bachelors degree", "Bachelors Degree"),
    ("masters degree", "Masters Degree"),
    ("phd", "PhD")   
)


radio_choices = (
   ('yes', 'Yes'),
   ('no', 'No')
)
class Form(models.Model):
    
    email                                       = models.EmailField()
    full_name                                   = models.CharField(max_length=30)
    age                                         = models.IntegerField()
    highest_level_of_education                  = models.CharField(max_length= 16, choices=highest_education,default="Choose")
    institute_where_you_completed_your_highest_level_of_education = models.CharField(max_length=100)
    what_did_you_study                          = models.CharField(max_length=20)
    do_you_have_any_relevant_work_experience    = models.CharField(max_length=20)
    what_institute_did_you_get_admitted_to_in_Canada = models.CharField(max_length=100)
    what_is_your_program_of_study_in_Canada                  = models.CharField(max_length=20)
    which_country_are_you_applying_from               = models.CharField(max_length=20)
    what_are_your_future_goals                                = models.CharField(max_length=30)
    english_scores_listening                           = models.CharField(max_length=5)
    english_scores_reading                             = models.CharField(max_length=5)
    english_scores_speaking                            = models.CharField(max_length=5)
    english_scores_writing                             = models.CharField(max_length=5)
    did_you_pay_your_first_year_tuition         = models.CharField(max_length= 5, choices=radio_choices,default="")
    how_much_tuition_fee_did_you_pay            = models.CharField(max_length=7)
    did_you_do_a_GIC                            = models.CharField(max_length= 5,choices=radio_choices,default="")
    how_much_did_you_pay_towards_GIC            = models.CharField(max_length=7)

    def __str__(self):
        return self.email


