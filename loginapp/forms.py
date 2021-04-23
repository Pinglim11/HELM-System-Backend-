from django import forms

from .models import Employee, EmployeePersonalInfo,EmployeePosition,EmployeeWorkLocation, ChildBackground,SpouseBackground,FamilyMemberBackground,EducationalBackground,EmploymentHistory, EmergencyDetails
  
# create a ModelForm 




class EmployeeRequiredRecordForm(forms.Form):
    #Employee Record
    employeeid = forms.IntegerField()  
    startdate = forms.DateTimeField()  
    enddate = forms.DateTimeField(required = False)  
    employmentstatus = forms.CharField(max_length=15)  
    salarytype = forms.CharField(max_length=10)  
    salary = forms.FloatField()
    branch = forms.ModelChoiceField(EmployeeWorkLocation.objects.all())
    jobid = forms.ModelChoiceField(EmployeePosition.objects.all())
    #Emplyoee Personal Info
    employeename = forms.CharField(max_length=20)  
    gender = forms.CharField(max_length=10)
    birthdate = forms.DateField()  
    civilstatus = forms.CharField( max_length=10)  
    citizenship = forms.CharField(max_length=20)
    religion = forms.CharField(max_length=20, required= False)
    bloodtype = forms.CharField( max_length=10)  
    numberofdependent = forms.IntegerField()  
    presentaddress = forms.CharField(max_length=100)  
    permanentaddress = forms.CharField(max_length=100)  
    contactnumber = forms.IntegerField()  
    #Emergency Details
    emergencycontactnumber = forms.IntegerField()  
    emergencycontactname = forms.CharField(max_length=20)  
    emergencyrelationship = forms.CharField(max_length=20, required = False)  
    emergencyaddress = forms.CharField(max_length=50)  

class JobsForm(forms.Form):
    position = forms.CharField(max_length=20)
    department = forms.CharField(max_length=20)

class BranchForm(forms.Form):
    branch = forms.CharField(max_length=20)
    region = forms.CharField(max_length=20)

class SpouseForm(forms.Form):
    spousename = forms.CharField(max_length=20,required = False)  
    spousecompany = forms.CharField(max_length=20,required = False)  
    spousecompanyaddress = forms.CharField( max_length=20, required = False)  
    numberofchildren = forms.IntegerField( required = False)  

class EmploymentHistoryForm(forms.Form): 
    previouscompanyname = forms.CharField( max_length=20)  
    previousposition = forms.CharField( max_length=20, required = False)  
    reasonforleaving = forms.CharField( max_length=20, required = False)  
    companycontactnumber = forms.CharField( max_length=20, required = False)  
    withcoeorclearance = forms.CharField( max_length=10)  


class EducationalBackgroundForm(forms.Form): 
    highestdegree = forms.CharField( max_length=20, required = False)  
    schoolname = forms.CharField( max_length=20)  
    startingyearattended = forms.DateField()  
    endingyearattended = forms.DateField()  
    schooltype = forms.CharField( max_length=15)  

class FamilyMemberBackgroundForm(forms.Form): 
    membername = forms.CharField( max_length=20)  
    memberage = forms.IntegerField( required = False)  
    memberrelationship = forms.CharField( max_length=20)  
    memberoccupation = forms.CharField( max_length=20, required = False)     


class ChildBackgroundForm(forms.Form): 
    childname = forms.CharField( max_length=20)  
    childage = forms.IntegerField( required = False)  
    childoccupation = forms.CharField( max_length=20, required = False)  
