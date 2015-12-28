from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Enrollment

class EnrollmentCreate(CreateView):
	model = Enrollment

class CompleteEnrollment(TemplateView):
	template_name = "CertIssuance/complete_enrollment.html"

	def get_context_data(self, **kwargs):
		context = super(CompleteEnrollment, self).get_context_data(**kwargs)
		return context


class ValidateUser(TemplateView):
	template_name = "CertIssuance/validate_user.html"

	def get_context_data(self, **kwargs):
		context = super(ValidateUser, self).get_context_data(**kwargs)
		context['message'] = "Hello, World"
		return context
