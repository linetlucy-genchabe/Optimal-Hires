from rest_framework import serializers
from .models import *


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('jobId','title', 'description', 'location', 'job_type', 'job_category','last_date', 'company_name', 'company_description', 'website','created_at',)

        
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('applicantId','fullname', 'image', 'gender',)


        
class ApplicantionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('applicationId','company','job','applicant','resume','apply_date')


        
class JobtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobtype
        fields = ('jobtypeId','name')


        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryId','name')

        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('companyId','name', 'contact', 'image','description',)