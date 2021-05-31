from datetime import datetime
from django import forms
from django.forms import widgets
import datetime

from .models import Employee, EmployeePersonalInfo,EmployeePosition,EmployeeWorkLocation, ChildBackground,SpouseBackground,FamilyMemberBackground,EducationalBackground,EmploymentHistory, EmergencyDetails, Document, Record
from django.contrib.admin.widgets import FilteredSelectMultiple
# create a ModelForm 

def checkmodel(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


#https://www.youtube.com/watch?v=I2-JYxnSiB0&ab_channel=PrettyPrinted
class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {
            'my_date_field': DateInput()
        }


class EmployeeDocument(forms.Form):
    recordfile = forms.FileField()
    preparedby = forms.CharField(max_length=20) 
    preparationdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    notedby = forms.CharField( max_length=20)  
    noteddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    approvedby = forms.CharField( max_length=20)  
    approveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    receivedby = forms.CharField(max_length=20)  
    receiveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  

class EditDocument(forms.Form):
    recordfile = forms.FileField(required = False)
    preparedby = forms.CharField(max_length=20) 
    preparationdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    notedby = forms.CharField( max_length=20)  
    noteddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    approvedby = forms.CharField( max_length=20)  
    approveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    receivedby = forms.CharField(max_length=20)  
    receiveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  

class RecordDocument(forms.Form):
    recordfile = forms.FileField()
    preparedby = forms.CharField(max_length=20) 
    preparationdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    notedby = forms.CharField( max_length=20)  
    noteddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    approvedby = forms.CharField( max_length=20)  
    approveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    receivedby = forms.CharField(max_length=20)  
    receiveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  

    # def clean(self):
    #     cd = super().clean()
       
    #     if cd.get('recordfile'):
    #         if not cd.get('preparedby') or not cd.get('preparationdate') or not cd.get('notedby') or not cd.get('noteddate') or not cd.get('approvedby') or not cd.get('approveddate') or not cd.get('receivedby') or not cd.get('receiveddate'):
    #             raise forms.ValidationError(('A document has been selected to upload, please fill in the other fields as well.'), code = 'filled')
    #     elif not cd.get('recordfile') and cd.get('preparedby') and cd.get('preparationdate') and cd.get('notedby') and cd.get('noteddate') and cd.get('approvedby') and cd.get('approveddate') and cd.get('receivedby') and cd.get('receiveddate'):
    #             raise forms.ValidationError(('Other fields have been filled, please upload a file as well. Empty the other fields to disregard the upload.'), code = 'nofile')
    #     return cd



class AwardsRecord(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=20)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recordfor = forms.ModelChoiceField(Employee.objects.all(), label = 'Awards Receiver')
    recorddescription = forms.CharField(required = False)  
    awardissuer = forms.CharField(max_length=20)  
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    awardpurpose = forms.CharField(max_length=20)  
    awardtype = forms.CharField( max_length=20)  
    
    def clean(self):
        cd = super().clean()
        
        if checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) != None:
            raise forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate')

        return cd



class AwardsRecordEdit(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=20)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recorddescription = forms.CharField(required = False)  
    awardissuer = forms.CharField(max_length=20)  
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    awardpurpose = forms.CharField(max_length=20)  
    awardtype = forms.CharField( max_length=20)  
    
    def clean(self):
        cd = super().clean()
        obj = checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) 
        if obj != None and Record.objects.get(memoreferencenumber = self.initial['memoreferencenumber']) != obj :
            raise forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate')

        return cd


class DisciplineRecord(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=20)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recordfor = forms.ModelChoiceField(Employee.objects.all(), label = 'NOAC Receiver')
    recorddescription = forms.CharField(required = False)  
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    remarks = forms.CharField(max_length=50, required = False)
    noactype = forms.ChoiceField( choices = (('Timekeeping', 'Timekeeping'), ('AWOL', 'AWOL'), ('Major', 'Major')))  
    sanction= forms.CharField(max_length=20)
    hearingdate = forms.DateTimeField(required = False, widget = DateInput)  
    noofoffense = forms.IntegerField(required = False) 
    
    def clean(self):
        cd = super().clean()
        
        if checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) != None:
            raise forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate')
        if (cd.get('noactype') == 'Timekeeping' or cd.get('noactype') == 'AWOL') and cd.get('noofoffense') == None:
            raise forms.ValidationError(('Number of Offense must be filled up for AWOL or Timekeeping!'), code = 'emptyfield')
        
        return cd


class DisciplineRecordEdit(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=20)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recorddescription = forms.CharField(required = False)  
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    remarks = forms.CharField(max_length=50, required = False)
    noactype = forms.ChoiceField( choices = (('Timekeeping', 'Timekeeping'), ('AWOL', 'AWOL'), ('Major', 'Major')))  
    sanction= forms.CharField(max_length=20)
    hearingdate = forms.DateTimeField(required = False, widget = DateInput)  
    noofoffense = forms.IntegerField(required = False) 
    
    def clean(self):
        cd = super().clean()
        obj = checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) 
        if obj != None and Record.objects.get(memoreferencenumber = self.initial['memoreferencenumber']) != obj :
            raise forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate')
        if (cd.get('noactype') == 'Timekeeping' or cd.get('noactype') == 'AWOL') and cd.get('noofoffense') == None:
            raise forms.ValidationError(('Number of Offense must be filled up for AWOL or Timekeeping!'), code = 'emptyfield')

        return cd
















class EmployeeRecordForm(forms.Form):
    #Employee Record
    employeeid = forms.IntegerField()  
    startdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    enddate = forms.DateTimeField(required = False, widget = DateInput)  
    employmentstatus = forms.ChoiceField( choices = (('Probationary', 'Probationary'), ('Seasonal', 'Seasonal'), ('Project-Based', 'Project-Based'), ('Reliever', 'Reliever')))  
    salarytype = forms.ChoiceField( choices = (('Monthly', 'Monthly'), ('Daily', 'Daily'), ('Piece Rate', 'Piece Rate')))  
    salary = forms.FloatField(min_value=0.00, max_value=100000000.00, initial=0.00)
    branch = forms.ModelChoiceField(EmployeeWorkLocation.objects.all())
    jobid = forms.ModelChoiceField(EmployeePosition.objects.all())

    def clean(self):
        cd = super().clean()
       
        if checkmodel(Employee, employeeid = int(cd.get('employeeid'))) != None:
            raise forms.ValidationError(('Employee ID Already exist in the system!'), code = 'duplicate')

        return cd

class EditRecordForm(forms.Form):
    #Employee Record
    employeeid = forms.IntegerField()  
    startdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    enddate = forms.DateTimeField(required = False, widget = DateInput)  
    employmentstatus = forms.ChoiceField( choices = (('Probationary', 'Probationary'), ('Seasonal', 'Seasonal'), ('Project-Based', 'Project-Based'), ('Reliever', 'Reliever')))  
    salarytype = forms.ChoiceField( choices = (('Monthly', 'Monthly'), ('Daily', 'Daily'), ('Piece Rate', 'Piece Rate')))  
    salary = forms.FloatField(min_value=0.00, max_value=100000000.00, initial=0.00)
    branch = forms.ModelChoiceField(EmployeeWorkLocation.objects.all())
    jobid = forms.ModelChoiceField(EmployeePosition.objects.all())

    
    #Emplyoee Personal Info
class EmployeePersonalForm(forms.Form):
    employeename = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}))
    gender = forms.ChoiceField( choices = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))  
    birthdate = forms.DateField(widget = DateInput)  
    civilstatus = forms.ChoiceField( choices = (('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Separated', 'Separated'), ('Widowed', 'Widowed')))   
    citizenship = forms.CharField(max_length=20)
    religion = forms.CharField(max_length=20, required= False)
    bloodtype = forms.ChoiceField( choices = (('Unknown', 'Unknown'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('OA-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')))  
    numberofdependent = forms.IntegerField(min_value=0, max_value=50, initial=0)  
    presentaddress = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    permanentaddress = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    contactnumber = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '09XX-XXX-YYYY'}))  
    #Emergency Details

class EmergencyForm(forms.Form):
    emergencycontactnumber = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '09XX-XXX-YYYY'}))  
    emergencycontactname = forms.CharField(max_length=20)  
    emergencyrelationship = forms.CharField(max_length=20, required = False)  
    emergencyaddress = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  

class JobsForm(forms.Form):
    position = forms.CharField(max_length=20)
    department = forms.CharField(max_length=20)

class BranchForm(forms.Form):
    branch = forms.CharField(max_length=20)
    region = forms.CharField(max_length=20)

class SpouseForm(forms.Form):
    spousename = forms.CharField(max_length=20,required = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}))  
    spousecompany = forms.CharField(max_length=20,required = False)  
    spousecompanyaddress = forms.CharField( max_length=20, required = False, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    numberofchildren = forms.IntegerField( required = False, min_value=0, max_value=20, initial=0)  

class EmploymentHistoryForm(forms.Form): 
    previouscompanyname = forms.CharField( max_length=20, required = False)  
    previousposition = forms.CharField( max_length=20, required = False)  
    reasonforleaving = forms.CharField( max_length=20, required = False)  
    companycontactnumber = forms.CharField( max_length=20, required = False, widget=forms.NumberInput(attrs={'placeholder': '09XX-XXX-YYYY'}))  
    withcoeorclearance = forms.ChoiceField( choices = (('WithCOE', 'With COE'), ('Clearance', 'With Clearance')))  

class EducationalBackgroundForm(forms.Form): 
    schooltypes = (('Grade School', 'Grade School'), ('High School', 'High School'), ('College', 'College'), ('Post Grad', 'Post Grad'), ('Vocational', 'Vocational'))
    highestdegree = forms.ChoiceField( choices = schooltypes)  
    schoolname = forms.CharField( max_length=20, required = False)  
    startingyearattended = forms.DateField(widget = DateInput, required = False)  
    endingyearattended = forms.DateField(widget = DateInput, required = False)  
    schooltype = forms.ChoiceField( choices = schooltypes)

class FamilyMemberBackgroundForm(forms.Form): 
    membername = forms.CharField( max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}), required = False)  
    memberage = forms.IntegerField( required = False)  
    memberrelationship = forms.ChoiceField( choices = (('Mother', 'Mother'), ('Father', 'Father'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Younger Brother', 'Younger Brother'), ('Younger Sister', 'Younger Sister')))  
    memberoccupation = forms.CharField( max_length=20, required = False)     


class ChildBackgroundForm(forms.Form): 
    childname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}), required = False)  
    childage = forms.IntegerField(required = False)  
    childoccupation = forms.CharField(max_length=20, required = False)  
