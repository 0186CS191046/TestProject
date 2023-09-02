from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SubmitForm
from .models import Form
from django. contrib import messages
import smtplib
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    if request.method == "POST":
        form = SubmitForm(request.POST)
        if form.is_valid():
            form_data = SubmitForm(
                email = form.cleaned_data['email'] ,
                full_name= form.cleaned_data['full_name'] ,
                age= form.cleaned_data['age'],
                highest_level_of_education = form.cleaned_data['highest_level_of_education'],
                institute_where_you_completed_your_highest_level_of_education = form.cleaned_data['institute_where_you_completed_your_highest_level_of_education'],
                what_did_you_study = form.cleaned_data['what_did_you_study'],
                do_you_have_any_relevant_work_experience = form.cleaned_data['do_you_have_any_relevant_work_experience'],
                what_institute_did_you_get_admitted_to_in_Canada = form.cleaned_data['what_institute_did_you_get_admitted_to_in_Canada'],
                what_is_your_program_of_study_in_Canada = form.cleaned_data['what_is_your_program_of_study_in_Canada'],
                which_country_are_you_applying_from = form.cleaned_data['which_country_are_you_applying_from'],
                what_are_your_future_goals = form.cleaned_data['what_are_your_future_goals'],
                english_scores_listening = form.cleaned_data['english_scores_listening'],
                english_scores_reading = form.cleaned_data['english_scores_reading'],
                english_scores_speaking = form.cleaned_data['english_scores_speaking'],
                english_scores_writing = form.cleaned_data['english_scores_writing'],
                did_you_pay_your_first_year_tuition = form.cleaned_data['did_you_pay_your_first_year_tuition'],
                how_much_tuition_fee_did_you_pay = form.cleaned_data['how_much_tuition_fee_did_you_pay'],
                did_you_do_a_GIC = form.cleaned_data['did_you_do_a_GIC'],
                how_much_did_you_pay_towards_GIC = form.cleaned_data['how_much_did_you_pay_towards_GIC'],
            )
            form_data.save()
            print("kaajal")
            # form_data = SubmitForm(
            #     email = email,
            #     full_name = full_name,
            #     age = age,
            #     highest_level_of_education = highest_level_of_education,
            #     institute_where_you_completed_your_highest_level_of_education = institute_where_you_completed_your_highest_level_of_education ,
            #     what_did_you_study = what_did_you_study,
            #     do_you_have_any_relevant_work_experience = do_you_have_any_relevant_work_experience,
            #     what_institute_did_you_get_admitted_to_in_Canada = what_institute_did_you_get_admitted_to_in_Canada,
            #     what_is_your_program_of_study_in_Canada = what_is_your_program_of_study_in_Canada,
            #     which_country_are_you_applying_from = which_country_are_you_applying_from,
            #     what_are_your_future_goals = what_are_your_future_goals,
            #     english_scores_listening = english_scores_listening,
            #     english_scores_reading = english_scores_reading,
            #     english_scores_speaking = english_scores_speaking,
            #     english_scores_writing = english_scores_writing,
            #     did_you_pay_your_first_year_tuition = did_you_pay_your_first_year_tuition,
            #     how_much_tuition_fee_did_you_pay = how_much_tuition_fee_did_you_pay,
            #     did_you_do_a_GIC = did_you_do_a_GIC,
            #     how_much_did_you_pay_towards_GIC = how_much_did_you_pay_towards_GIC
            #     )
            # form_data.save()

            # Create and send the email
            # subject = "Reagarding Form Data" 
            # email_message =  f'Email : {email}\nFull_Name : {full_name}\nAge : {age}\nHighest Level of Education : {highest_level_of_education}\nInstitute where you completed your highest level of education : {institute_where_you_completed_your_highest_level_of_education}\nWhat did you study : {what_did_you_study}\nDo you have any relevant work experience? : {do_you_have_any_relevant_work_experience}\nWhat institute did you get admitted to in Canada? : {what_institute_did_you_get_admitted_to_in_Canada}\nWhat is your program of study in Canada? : {what_is_your_program_of_study_in_Canada}\nWhich country are you applying from? : {which_country_are_you_applying_from}\nWhat are your future goals? : {what_are_your_future_goals}\nEnglish Scores - Listening : {english_scores_listening}\nEnglish Scores - Reading : {english_scores_reading}\nEnglish Scores - Speaking : {english_scores_speaking}\nEnglish Scores - Writing : {english_scores_speaking}\nDid you pay your first year tuition? : {did_you_pay_your_first_year_tuition}\nHow much tuition fee did you pay? : {how_much_tuition_fee_did_you_pay}\nDid you do a GIC? : {did_you_do_a_GIC}\nHow much did you pay towards GIC? : {how_much_did_you_pay_towards_GIC}'
            # from_email = "kumarikajal89681@gmail.com"
            # recipient_email = f'{email}'
            # try:
            #     send_mail(subject, email_message, from_email, recipient_email) 
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            # return redirect('thanks')
        # messages.success(request,"Data has been saved.")
        
    form = SubmitForm()
    return render(request, "form.html", {'form':form})

        
    # return render(request,'form.html',)

def thanks(request):
    return render(request,'thanks.html')


# email = request.POST['email']
        # full_name = request.POST['full_name']
        # age = request.POST['age']
        # highest_level_of_education = request.POST['education']
        # institute_where_you_completed_your_highest_level_of_education = request.POST['institute']
        # what_did_you_study = request.POST['study']
        # do_you_have_any_relevant_work_experience = request.POST['relevant_experience']
        # what_institute_did_you_get_admitted_to_in_Canada = request.POST['admit_in_institute']
        # what_is_your_program_of_study_in_Canada = request.POST['program_of_study']
        # which_country_are_you_applying_from = request.POST['apply_in_country']
        # what_are_your_future_goals = request.POST['future_goals']
        # english_scores_listening = request.POST['english_listening']
        # english_scores_reading =request.POST['english_reading']
        # english_scores_speaking = request.POST['english_speaking']
        # english_scores_writing = request.POST['english_writing']
        # did_you_pay_your_first_year_tuition = request.POST['pay']
        # how_much_tuition_fee_did_you_pay = request.POST['amount'] 
        # did_you_do_a_GIC = request.POST['gic']
        # how_much_did_you_pay_towards_GIC = request.POST['pay_towards_gic']

        # form = Form.objects.create(
        #     email = email,
        #     full_name = full_name,
        #     age = age,
        #     highest_level_of_education = highest_level_of_education,
        #     institute_where_you_completed_your_highest_level_of_education = institute_where_you_completed_your_highest_level_of_education ,
        #     what_did_you_study = what_did_you_study,
        #     do_you_have_any_relevant_work_experience = do_you_have_any_relevant_work_experience,
        #     what_institute_did_you_get_admitted_to_in_Canada = what_institute_did_you_get_admitted_to_in_Canada,
        #     what_is_your_program_of_study_in_Canada = what_is_your_program_of_study_in_Canada,
        #     which_country_are_you_applying_from = which_country_are_you_applying_from,
        #     what_are_your_future_goals = what_are_your_future_goals,
        #     english_scores_listening = english_scores_listening,
        #     english_scores_reading = english_scores_reading,
        #     english_scores_speaking = english_scores_speaking,
        #     english_scores_writing = english_scores_writing,
        #     did_you_pay_your_first_year_tuition = did_you_pay_your_first_year_tuition,
        #     how_much_tuition_fee_did_you_pay = how_much_tuition_fee_did_you_pay,
        #     did_you_do_a_GIC = did_you_do_a_GIC,
        #     how_much_did_you_pay_towards_GIC = how_much_did_you_pay_towards_GIC
        # )