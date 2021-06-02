from datetime import datetime
from django import forms
from django.forms import widgets
import datetime
import re
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
    preparedby = forms.CharField(max_length=100) 
    preparationdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    notedby = forms.CharField( max_length=100)  
    noteddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    approvedby = forms.CharField( max_length=100)  
    approveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    receivedby = forms.CharField(max_length=100)  
    receiveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if cd.get('preparedby'):
            if re.search(r'\d', cd.get('preparedby')):
                error.append(forms.ValidationError(('Prepared by should not contain a number!'), code = 'prep'))
                errors = True
        if cd.get('notedby'):
            if re.search(r'\d', cd.get('notedby')):
                error.append(forms.ValidationError(('Noted by should not contain a number!'), code = 'note'))
                errors = True
        if cd.get('approvedby'):
            if re.search(r'\d', cd.get('approvedby')):
                error.append(forms.ValidationError(('Approved by should not contain a number!'), code = 'approve'))
                errors = True
        if cd.get('receivedby'):
            if re.search(r'\d', cd.get('receivedby')):
                error.append(forms.ValidationError(('Received by should not contain a number!'), code = 'receive'))
                errors = True
        if errors:
            print(errors)
            raise forms.ValidationError(error)
        
        return cd

class EditDocument(forms.Form):
    recordfile = forms.FileField(required = False)
    preparedby = forms.CharField(max_length=100) 
    preparationdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    notedby = forms.CharField( max_length=100)  
    noteddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    approvedby = forms.CharField( max_length=100)  
    approveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    receivedby = forms.CharField(max_length=100)  
    receiveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if cd.get('preparedby'):
            if re.search(r'\d', cd.get('preparedby')):
                error.append(forms.ValidationError(('Prepared by should not contain a number!'), code = 'prep'))
                errors = True
        if cd.get('notedby'):
            if re.search(r'\d', cd.get('notedby')):
                error.append(forms.ValidationError(('Noted by should not contain a number!'), code = 'note'))
                errors = True
        if cd.get('approvedby'):
            if re.search(r'\d', cd.get('approvedby')):
                error.append(forms.ValidationError(('Approved by should not contain a number!'), code = 'approve'))
                errors = True
        if cd.get('receivedby'):
            if re.search(r'\d', cd.get('receivedby')):
                error.append(forms.ValidationError(('Received by should not contain a number!'), code = 'receive'))
                errors = True
        if errors:
            print(errors)
            raise forms.ValidationError(error)
        
        return cd

class RecordDocument(forms.Form):
    recordfile = forms.FileField()
    preparedby = forms.CharField(max_length=100) 
    preparationdate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    notedby = forms.CharField( max_length=100)  
    noteddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    approvedby = forms.CharField( max_length=100)  
    approveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    receivedby = forms.CharField(max_length=100)  
    receiveddate = forms.DateTimeField(widget = DateInput, initial=datetime.datetime.now())  
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if cd.get('preparedby'):
            if re.search(r'\d', cd.get('preparedby')):
                error.append(forms.ValidationError(('Prepared by should not contain a number!'), code = 'prep'))
                errors = True
        if cd.get('notedby'):
            if re.search(r'\d', cd.get('notedby')):
                error.append(forms.ValidationError(('Noted by should not contain a number!'), code = 'note'))
                errors = True
        if cd.get('approvedby'):
            if re.search(r'\d', cd.get('approvedby')):
                error.append(forms.ValidationError(('Approved by should not contain a number!'), code = 'approve'))
                errors = True
        if cd.get('receivedby'):
            if re.search(r'\d', cd.get('receivedby')):
                error.append(forms.ValidationError(('Received by should not contain a number!'), code = 'receive'))
                errors = True
        if errors:
            raise forms.ValidationError(error)
        
        return cd





class AwardsRecord(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=100)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recordfor = forms.ModelChoiceField(Employee.objects.all(), label = 'Awards Receiver')
    recorddescription = forms.CharField(required = False, widget=forms.Textarea)
    awardissuer = forms.CharField(max_length=100)  
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    awardpurpose = forms.CharField(max_length=100)  
    awardtype = forms.CharField( max_length=20)  
    
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) != None:
            error.append(forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate'))
            errors = True
        if cd.get('issuingbranch'):
            if re.search(r'\d', cd.get('issuingbranch')):
                error.append(forms.ValidationError(('Issuing branch should not contain a number!'), code = 'ib'))
                errors = True
        if cd.get('issuingdepartment'):
            if re.search(r'\d', cd.get('issuingdepartment')):
                error.append(forms.ValidationError(('Issuing department should not contain a number!'), code = 'idp'))
                errors = True
        if cd.get('awardpurpose'):
            if re.search(r'\d', cd.get('awardpurpose')):
                error.append(forms.ValidationError(('Award Purpose should not contain a number!'), code = 'ap'))
                errors = True
        # if cd.get('awardtype'):
        #     if re.search(r'\d', cd.get('awardtype')):
        #         error.append(forms.ValidationError(('Award Type should not contain a number!'), code = 'at'))
        #         errors = True
        if errors:
            raise forms.ValidationError(error)
        
        return cd
    
  



class AwardsRecordEdit(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=100)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recorddescription = forms.CharField(required = False, widget=forms.Textarea) 
    awardissuer = forms.CharField(max_length=100)  
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    awardpurpose = forms.CharField(max_length=100)  
    awardtype = forms.CharField( max_length=20)  
    
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        obj = checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) 
        if obj != None and Record.objects.get(memoreferencenumber = self.initial['memoreferencenumber']) != obj :
            error.append(forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate'))
            errors = True
        if cd.get('issuingbranch'):
            if re.search(r'\d', cd.get('issuingbranch')):
                error.append(forms.ValidationError(('Issuing branch should not contain a number!'), code = 'ib'))
                errors = True
        if cd.get('issuingdepartment'):
            if re.search(r'\d', cd.get('issuingdepartment')):
                error.append(forms.ValidationError(('Issuing department should not contain a number!'), code = 'idp'))
                errors = True
        if cd.get('awardpurpose'):
            if re.search(r'\d', cd.get('awardpurpose')):
                error.append(forms.ValidationError(('Award Purpose should not contain a number!'), code = 'ap'))
                errors = True
        # if cd.get('awardtype'):
        #     if re.search(r'\d', cd.get('awardtype')):
        #         error.append(forms.ValidationError(('Award Type should not contain a number!'), code = 'at'))
        #         errors = True
        if errors:
            raise forms.ValidationError(error)
        return cd


class DisciplineRecord(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=100)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recordfor = forms.ModelChoiceField(Employee.objects.all(), label = 'NOAC Receiver')
    recorddescription = forms.CharField(required = False, widget=forms.Textarea)
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    remarks = forms.CharField(required = False, widget=forms.Textarea)
    noactype = forms.ChoiceField( choices = (('Timekeeping', 'Timekeeping'), ('AWOL', 'AWOL'), ('Major', 'Major')))  
    sanction= forms.CharField(max_length=20)
    hearingdate = forms.DateTimeField(required = False, widget = DateInput)  
    noofoffense = forms.IntegerField(required = False) 
    
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) != None:
            error.append(forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate'))
            errors = True
        if (cd.get('noactype') == 'Timekeeping' or cd.get('noactype') == 'AWOL') and cd.get('noofoffense') == None:
            error.append(forms.ValidationError(('Number of Offense must be filled up for AWOL or Timekeeping!'), code = 'emptyfield'))
            errors = True
        if cd.get('issuingbranch'):
            if re.search(r'\d', cd.get('issuingbranch')):
                error.append(forms.ValidationError(('Issuing branch should not contain a number!'), code = 'ib'))
                errors = True
        if cd.get('issuingdepartment'):
            if re.search(r'\d', cd.get('issuingdepartment')):
                error.append(forms.ValidationError(('Issuing department should not contain a number!'), code = 'idp'))
                errors = True
        
        if errors:
            raise forms.ValidationError(error)
        
        return cd


class DisciplineRecordEdit(forms.Form):
    memoreferencenumber = forms.IntegerField()  
    recordname = forms.CharField(max_length=100)  
    memodate = forms.DateField(required = False, widget = DateInput)  
    recorddescription = forms.CharField(required = False, widget=forms.Textarea)
    issuingbranch = forms.CharField(max_length=20)  
    issuingdepartment = forms.CharField(max_length=20)  
    remarks = forms.CharField(required = False, widget=forms.Textarea)
    noactype = forms.ChoiceField( choices = (('Timekeeping', 'Timekeeping'), ('AWOL', 'AWOL'), ('Major', 'Major')))  
    sanction= forms.CharField(max_length=20)
    hearingdate = forms.DateTimeField(required = False, widget = DateInput)  
    noofoffense = forms.IntegerField(required = False) 
    
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        obj = checkmodel(Record, memoreferencenumber = int(cd.get('memoreferencenumber'))) 
        if obj != None and Record.objects.get(memoreferencenumber = self.initial['memoreferencenumber']) != obj :
            error.append(forms.ValidationError(('Memo Reference Number already exist in the system!'), code = 'duplicate'))
            errors = True
        if (cd.get('noactype') == 'Timekeeping' or cd.get('noactype') == 'AWOL') and cd.get('noofoffense') == None:
            error.append(forms.ValidationError(('Number of Offense must be filled up for AWOL or Timekeeping!'), code = 'emptyfield'))
            errors = True
        if cd.get('issuingbranch'):
            if re.search(r'\d', cd.get('issuingbranch')):
                error.append(forms.ValidationError(('Issuing branch should not contain a number!'), code = 'ib'))
                errors = True
        if cd.get('issuingdepartment'):
            if re.search(r'\d', cd.get('issuingdepartment')):
                error.append(forms.ValidationError(('Issuing department should not contain a number!'), code = 'idp'))
                errors = True
        
        if errors:
            raise forms.ValidationError(error)
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
    employeename = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}))
    gender = forms.ChoiceField( choices = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))  
    birthdate = forms.DateField(widget = DateInput)  
    civilstatus = forms.ChoiceField( choices = (('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Separated', 'Separated'), ('Widowed', 'Widowed')))   
    citizenship = forms.CharField(max_length=20)
    religion = forms.CharField(max_length=20, required= False)
    bloodtype = forms.ChoiceField( choices = (('Unknown', 'Unknown'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('OA-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')))  
    numberofdependent = forms.IntegerField(min_value=0, max_value=50, initial=0)  
    presentaddress = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    permanentaddress = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    contactnumber = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': '09XX-XXX-YYYY'}))  
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if cd.get('contactnumber'):
            if re.search('[a-zA-Z]',cd.get('contactnumber')):
                error.append(forms.ValidationError(('Contact number should not contain a letter!'), code = 'letter'))
                errors = True
            if len(cd.get('contactnumber')) < 7:
                error.append(forms.ValidationError(('Contact number should be longer than 7 numbers!'), code = 'length'))
                errors = True
        if cd.get('employeename'):
            if re.search(r'\d', cd.get('employeename')):
                error.append(forms.ValidationError(('Employee name should not contain a number!'), code = 'number'))
                errors = True
        if errors:
            raise forms.ValidationError(error)
        return cd
    
    
    
    
    #Emergency Details

class EmergencyForm(forms.Form):
    emergencycontactnumber = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': '09XX-XXX-YYYY'}))  
    emergencycontactname = forms.CharField(max_length=100)  
    emergencyrelationship = forms.CharField(max_length=20, required = False)  
    emergencyaddress = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if cd.get('emergencycontactnumber'):
            if re.search('[a-zA-Z]',cd.get('emergencycontactnumber')):
                error.append(forms.ValidationError(('Emergency Contact number should not contain a letter!'), code = 'letter'))
                errors = True
            if len(cd.get('emergencycontactnumber')) < 7:
                error.append(forms.ValidationError(('Contact number should be longer than 7 numbers!'), code = 'length'))
                errors = True
        if cd.get('emergencycontactname'):
            if re.search(r'\d', cd.get('emergencycontactname')):
                error.append(forms.ValidationError(('Emergency Contact name should not contain a number!'), code = 'number'))
                errors = True
        if errors:
            raise forms.ValidationError(error)
        return cd

class JobsForm(forms.Form):
    position = forms.CharField(max_length=20)
    department = forms.CharField(max_length=20)

class BranchForm(forms.Form):
    branch = forms.CharField(max_length=20)
    region = forms.CharField(max_length=20)

class SpouseForm(forms.Form):
    spousename = forms.CharField(max_length=100,required = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}))  
    spousecompany = forms.CharField(max_length=20,required = False)  
    spousecompanyaddress = forms.CharField( max_length=255, required = False, widget=forms.TextInput(attrs={'placeholder': 'Unit No., Bldg., Street, Village, Brgy., City, Province'}))  
    numberofchildren = forms.IntegerField( required = False, min_value=0, max_value=20, initial=0)  

    def clean(self):
        cd = super().clean()
        if cd.get('spousename'):
            if re.search(r'\d', cd.get('spousename')):
                raise forms.ValidationError(('Spouse name should not contain a number!'), code = 'number')
        return cd

class EmploymentHistoryForm(forms.Form): 
    previouscompanyname = forms.CharField( max_length=100, required = False)  
    previousposition = forms.CharField( max_length=20, required = False)  
    reasonforleaving = forms.CharField( max_length=255, required = False)  
    companycontactnumber = forms.CharField( max_length=20, required = False, widget=forms.TextInput(attrs={'placeholder': '09XX-XXX-YYYY'}))  
    withcoeorclearance = forms.ChoiceField( choices = (('WithCOE', 'With COE'), ('Clearance', 'With Clearance')))  
    def clean(self):
        cd = super().clean()
        error = []
        errors = False
        if cd.get('companycontactnumber'):
            if re.search('[a-zA-Z]',cd.get('companycontactnumber')):
                error.append(forms.ValidationError(('Contact number should not contain a letter!'), code = 'letter'))
                errors = True
            if len(cd.get('companycontactnumber')) < 7:
                error.append(forms.ValidationError(('Contact number should be longer than 7 numbers!'), code = 'length'))
                errors = True
        if errors:
            raise forms.ValidationError(error)
        
        return cd

class EducationalBackgroundForm(forms.Form): 
    schooltypes = (('Grade School', 'Grade School'), ('High School', 'High School'), ('College', 'College'), ('Post Grad', 'Post Grad'), ('Vocational', 'Vocational'))
    highestdegree = forms.ChoiceField( choices = schooltypes)  
    schoolname = forms.CharField( max_length=100, required = False)  
    startingyearattended = forms.DateField(widget = DateInput, required = False)  
    endingyearattended = forms.DateField(widget = DateInput, required = False)  
    schooltype = forms.ChoiceField( choices = schooltypes)

class FamilyMemberBackgroundForm(forms.Form): 
    membername = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}), required = False)  
    memberage = forms.IntegerField( required = False)  
    memberrelationship = forms.ChoiceField( choices = (('Mother', 'Mother'), ('Father', 'Father'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Younger Brother', 'Younger Brother'), ('Younger Sister', 'Younger Sister')))  
    memberoccupation = forms.CharField( max_length=20, required = False)    
    def clean(self):
        cd = super().clean()
        if cd.get('membername'):
            if re.search(r'\d', cd.get('membername')):
                raise forms.ValidationError(('Family member name should not contain a number!'), code = 'number')
        return cd 


class ChildBackgroundForm(forms.Form): 
    childname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name, First Name M.I.'}), required = False)  
    childage = forms.IntegerField(required = False)  
    childoccupation = forms.CharField(max_length=20, required = False)  
    def clean(self):
        cd = super().clean()
        
        if cd.get('childname'):
            if re.search(r'\d', cd.get('childname')):
                raise forms.ValidationError(('Child name should not contain a number!'), code = 'childnumber')
        return cd 
