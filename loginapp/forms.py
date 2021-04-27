from django import forms

from .models import Employee, EmployeePersonalInfo,EmployeePosition,EmployeeWorkLocation, ChildBackground,SpouseBackground,FamilyMemberBackground,EducationalBackground,EmploymentHistory, EmergencyDetails
  
# create a ModelForm 




class EmployeeRequiredRecordForm(forms.Form):
    #Employee Record
    employeeid = forms.IntegerField()  
    startdate = forms.DateTimeField()  
    enddate = forms.DateTimeField(required = False)  
    employmentstatus = forms.ChoiceField( choices = (('Probationary', 'Probationary'), ('Seasonal', 'Seasonal'), ('Project-Based', 'Project-Based'), ('Reliever', 'Reliever')))  
    salarytype = forms.ChoiceField( choices = (('Monthly', 'Monthly'), ('Daily', 'Daily'), ('Piece Rate', 'Piece Rate')))  
    salary = forms.FloatField()
    branch = forms.ModelChoiceField(EmployeeWorkLocation.objects.all())
    jobid = forms.ModelChoiceField(EmployeePosition.objects.all())
    #Emplyoee Personal Info
    employeename = forms.CharField(max_length=20)  
    gender = forms.ChoiceField( choices = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))  
    birthdate = forms.DateField()  
    civilstatus = forms.CharField( max_length=10)  
    citizenship = forms.CharField(max_length=20)
    religion = forms.CharField(max_length=20, required= False)
    bloodtype = forms.ChoiceField( choices = (('Unknown', 'Unknown'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('OA-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')))  
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
    withcoeorclearance = forms.ChoiceField( choices = (('WithCOE', 'With COE'), ('Clearance', 'With Clearance')))  


class EducationalBackgroundForm(forms.Form): 
    schooltypes = (('Grade School', 'Grade School'), ('High School', 'High School'), ('College', 'College'), ('Post Grad', 'Post Grad'), ('Vocational', 'Vocational'))
    highestdegree = forms.ChoiceField( choices = schooltypes, required = False)  
    schoolname = forms.CharField( max_length=20)  
    startingyearattended = forms.DateField()  
    endingyearattended = forms.DateField()  
    schooltype = forms.ChoiceField( choices = schooltypes)  
class FamilyMemberBackgroundForm(forms.Form): 
    membername = forms.CharField( max_length=20)  
    memberage = forms.IntegerField( required = False)  
    memberrelationship = forms.ChoiceField( choices = (('Mother', 'Mother'), ('Father', 'Father'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Younger Brother', 'Younger Brother'), ('Younger Sister', 'Younger Sister')))  
    memberoccupation = forms.CharField( max_length=20, required = False)     


class ChildBackgroundForm(forms.Form): 
    childname = forms.CharField(max_length=20)  
    childage = forms.IntegerField(required = False)  
    childoccupation = forms.CharField(max_length=20, required = False)  
