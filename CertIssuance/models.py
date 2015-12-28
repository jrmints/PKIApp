from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod
from django.db import models

class RemoteService(models.Model):
	ip_address = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False)
	port = models.SmallIntegerField()

class CertificateAuthority(RemoteService):

	name = models.CharField(max_length=50)

	class Meta:
	   abstract = True

	@abstractmethod
	def submit_csr(self):
	   pass

	@abstractmethod
	def revoke_certificate(certificate):
		pass

	@abstractmethod
	def is_certificate_revoked(certificate):
		pass

class DefaultCertificateAuthority(CertificateAuthority):
	#return a certificate
	def submit_csr(self):
	   return "test"

	def revoke_certificate(certificate):
		return "test"

	def is_certificate_revoked(certificate):
		return "test"

class DirectoryServer(RemoteService):
	name = models.CharField(max_length=50)
	
	def search_for_identity(search):
		pass

	def add_certificate_to_identity():
		pass
	


class Role(models.Model):
        role_name = models.CharField(max_length=50)
        

class User(models.Model):
	username = models.CharField(max_length=100)

        def get_enrollments():
                return false
        
	def is_elligible(self):
	        return false
   
class PinNumber(models.Model):
        pin = models.CharField(max_length=50)
        generated_for_user = models.ForeignKey(User, on_delete=models.CASCADE)

        def create_new_pin():
                pass

class IssuedCertificate(models.Model):
        base64_certificate = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
        #issuing_ca = models.ForeignKey(CertificateAuthority, on_delete=models.CASCADE)
	def revoke(self):
		return true

	def is_revoked():
		#return issuing_ca.is_certificate_revoked(self)
		pass   

class BaseRequest(models.Model):
	pass

class CertificateRequest(BaseRequest):
	pass

class Enrollment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def is_complete():
		pass

class RevocationRequest(BaseRequest):
	pass

class CertificateAuthorityServerRequest(models.Model):
	pass

class CertificateAuthorityServerResponse(models.Model):
	pass
