from django import forms

class ValidateUserForm(forms.Form):
	def submit_form():
		#Search for user id in Active Directory
		#Check if they already have valid certificates
		#if they exist and don't have valid certificates, move to next step
		pass

class SubmitEnrollmentForm(forms.Form):
	user_id = forms.CharField(max_length=100)
	
	def submit_form():
		#Add the enrollment to the database
		#generate a pin that is emailed to the user
		pass


class CompleteEnrollmentForm(forms.Form):
	user_id = forms.CharField(max_length=100)

	def submit_to_ca():
		pass
