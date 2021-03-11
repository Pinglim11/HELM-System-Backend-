from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import EmployeeRequiredRecordForm,JobsForm, BranchForm, SpouseForm, EmploymentHistoryForm,EducationalBackgroundForm,FamilyMemberBackgroundForm,ChildBackgroundForm 
from .models import Employee, EmployeePersonalInfo,EmployeePosition,EmployeeWorkLocation, ChildBackground,SpouseBackground,FamilyMemberBackground,EducationalBackground,EmploymentHistory, EmergencyDetails
from django.forms import formset_factory

    # Redirect to a success page.
def checkmodel(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

def checkmodelq(classmodel, arg):
    try:
        return classmodel.objects.get(arg)
    except classmodel.DoesNotExist:
        return None

# Create your views here.
@login_required
def employeeform(request):
    return render(request, 'loginapp/employee_masterlist.html')


def testing(request):

    record = EmployeeRequiredRecordForm(request.POST) 
    worklocation = BranchForm(request.POST) 
    position = JobsForm(request.POST)
    spouse = SpouseForm(request.POST) 
    emphistory = formset_factory(EmploymentHistoryForm, extra = 1)
    education = EducationalBackgroundForm(request.POST) 
    family = FamilyMemberBackgroundForm(request.POST) 
    child = ChildBackgroundForm (request.POST) 

    # check if form data is valid 
    if request.method == "POST":
        


        if record.is_valid(): 
            branch = None
            job = None
            spousetemp = None
            emergency = None
            informationid = None
            #Check if worklocation already exist, These are temporary, can be a dropdown foreign key thing in the future if ever
            if worklocation.is_valid():
                branchcheck = checkmodel(EmployeeWorkLocation, branch = worklocation.cleaned_data['branch'])
                if branchcheck == None:
                    workstore = EmployeeWorkLocation.objects.create(branch = worklocation.cleaned_data['branch'], region = worklocation.cleaned_data['region'])
                    branch = workstore
                else:
                    branch = branchcheck
                

            if position.is_valid():
                deptarg = Q(department__contains = position.cleaned_data['department'])
                jobarg = Q(position__contains = position.cleaned_data['position'])
                positioncheck = checkmodelq(EmployeePosition, deptarg & jobarg)
                if positioncheck == None:
                    posstore = EmployeePosition.objects.create(position = position.cleaned_data['position'], department = position.cleaned_data['department'])
                    job = posstore
                else:
                    job = positioncheck
            
            if spouse.is_valid():
                spousenamearg = Q(spousename__contains = spouse.cleaned_data['spousename'])
                spousecomparg = Q(spousecompany__contains = spouse.cleaned_data['spousecompany'])
                spousechildren = Q(numberofchildren__contains = spouse.cleaned_data['numberofchildren'])
                spousecheck = checkmodelq(SpouseBackground, spousenamearg & spousecomparg & spousechildren) 
                if spousecheck == None:
                    spousestore = SpouseBackground.objects.create(spousename = spouse.cleaned_data['spousename'], spousecompany = spouse.cleaned_data['spousecompany'], spousecompanyaddress = spouse.cleaned_data['spousecompanyaddress'], numberofchildren = spouse.cleaned_data['numberofchildren'])
                    spousetemp = spousestore
                else:
                    spousetemp = spousecheck

            
            emergencycheck = checkmodel(EmergencyDetails,emergencycontactnumber = record.cleaned_data['emergencycontactnumber'])

            if  emergencycheck == None:
                emergencystore = EmergencyDetails.objects.create(emergencycontactnumber = record.cleaned_data['emergencycontactnumber'], emergencycontactname= record.cleaned_data['emergencycontactname'], emergencyrelationship= record.cleaned_data['emergencyrelationship'],emergencyaddress=record.cleaned_data['emergencyaddress'])
                emergency = emergencystore
            else:
                emergency = emergencycheck

            pinfostore = EmployeePersonalInfo.objects.create(emergencycontactnumber= emergency,
            employeename= record.cleaned_data['employeename'], 
            gender = record.cleaned_data['gender'], 
            birthdate = record.cleaned_data['birthdate'],
            civilstatus = record.cleaned_data['civilstatus'],
            citizenship = record.cleaned_data['citizenship'],
            religion = record.cleaned_data['religion'],
            bloodtype = record.cleaned_data['bloodtype'],
            numberofdependent = record.cleaned_data['numberofdependent'],
            presentaddress = record.cleaned_data['presentaddress'],
            permanentaddress = record.cleaned_data['permanentaddress'],
            contactnumber = record.cleaned_data['contactnumber'],
            spouseid = spousetemp)
            informationid = pinfostore
            
            recordstore = Employee.objects.create(
                informationid= informationid,
                employeeid=  record.cleaned_data['employeeid'],
                branch = branch,
                startdate = record.cleaned_data['startdate'],
                enddate = record.cleaned_data['enddate'],
                employmentstatus = record.cleaned_data['employmentstatus'],
                salarytype = record.cleaned_data['salarytype'],
                salary = record.cleaned_data['salary'],
                jobid = job
            )



            if emphistory.is_valid():
                for histories in emphistory:
                    emphistorystore = EmploymentHistory.objects.create(
                    informationid=informationid, 
                    previouscompanyname= histories.cleaned_data['previouscompanyname'],
                    previousposition= histories.cleaned_data['previousposition'],
                    reasonforleaving= histories.cleaned_data['reasonforleaving'],
                    companycontactnumber= histories.cleaned_data['companycontactnumber'],
                    withcoeorclearance= histories.cleaned_data['withcoeorclearance']
                    )



            if education.is_valid():
                educationstore = EducationalBackground.objects.create(
                informationid=informationid,
                highestdegree= education.cleaned_data['highestdegree'],
                schoolname=education.cleaned_data['schoolname'],
                startingyearattended=education.cleaned_data['startingyearattended'],
                endingyearattended=education.cleaned_data['endingyearattended'],
                schooltype=education.cleaned_data['schooltype']
                )
  

            if family.is_valid():
                familystore = FamilyMemberBackground.objects.create(
                    informationid= informationid,
                    membername= family.cleaned_data['membername'],
                    memberage= family.cleaned_data['memberage'],
                    memberrelationship= family.cleaned_data['memberrelationship'],
                    memberoccupation= family.cleaned_data['memberoccupation']
                )
                

            if child.is_valid():
                childstore = ChildBackground.objects.create(
                childname= child.cleaned_data['childname'],
                childage= child.cleaned_data['childage'],
                childoccupation= child.cleaned_data['childoccupation'],
                informationid= informationid
                )
                
                
    
       
  
    context = {
    'record': record,
    'worklocation': worklocation,
    'position': position,
    'spouse': spouse,
    'emphistory': emphistory,
    'education': education ,
    'family': family,
    'child': child 
    } 
    return render(request, 'loginapp/test.html',context)

@login_required
def createrecord(request):
     # create object of form 
    record = EmployeeRequiredRecordForm(request.POST) 
    worklocation = BranchForm(request.POST) 
    position = JobsForm(request.POST)
    spouse = SpouseForm(request.POST) 
    emphistory = EmploymentHistoryForm(request.POST) 
    education = EducationalBackgroundForm(request.POST) 
    family = FamilyMemberBackgroundForm(request.POST) 
    child = ChildBackgroundForm (request.POST) 

    # check if form data is valid 
    if request.method == "POST":
        


        if record.is_valid(): 
            branch = None
            job = None
            spousetemp = None
            emergency = None
            informationid = None
            #Check if worklocation already exist, These are temporary, can be a dropdown foreign key thing in the future if ever
            if worklocation.is_valid():
                branchcheck = checkmodel(EmployeeWorkLocation, branch = worklocation.cleaned_data['branch'])
                if branchcheck == None:
                    workstore = EmployeeWorkLocation.objects.create(branch = worklocation.cleaned_data['branch'], region = worklocation.cleaned_data['region'])
                    branch = workstore
                else:
                    branch = branchcheck
                

            if position.is_valid():
                deptarg = Q(department__contains = position.cleaned_data['department'])
                jobarg = Q(position__contains = position.cleaned_data['position'])
                positioncheck = checkmodelq(EmployeePosition, deptarg & jobarg)
                if positioncheck == None:
                    posstore = EmployeePosition.objects.create(position = position.cleaned_data['position'], department = position.cleaned_data['department'])
                    job = posstore
                else:
                    job = positioncheck
            
            if spouse.is_valid():
                spousenamearg = Q(spousename__contains = spouse.cleaned_data['spousename'])
                spousecomparg = Q(spousecompany__contains = spouse.cleaned_data['spousecompany'])
                spousechildren = Q(numberofchildren__contains = spouse.cleaned_data['numberofchildren'])
                spousecheck = checkmodelq(SpouseBackground, spousenamearg & spousecomparg & spousechildren) 
                if spousecheck == None:
                    spousestore = SpouseBackground.objects.create(spousename = spouse.cleaned_data['spousename'], spousecompany = spouse.cleaned_data['spousecompany'], spousecompanyaddress = spouse.cleaned_data['spousecompanyaddress'], numberofchildren = spouse.cleaned_data['numberofchildren'])
                    spousetemp = spousestore
                else:
                    spousetemp = spousecheck

            
            emergencycheck = checkmodel(EmergencyDetails,emergencycontactnumber = record.cleaned_data['emergencycontactnumber'])

            if  emergencycheck == None:
                emergencystore = EmergencyDetails.objects.create(emergencycontactnumber = record.cleaned_data['emergencycontactnumber'], emergencycontactname= record.cleaned_data['emergencycontactname'], emergencyrelationship= record.cleaned_data['emergencyrelationship'],emergencyaddress=record.cleaned_data['emergencyaddress'])
                emergency = emergencystore
            else:
                emergency = emergencycheck

            pinfostore = EmployeePersonalInfo.objects.create(emergencycontactnumber= emergency,
            employeename= record.cleaned_data['employeename'], 
            gender = record.cleaned_data['gender'], 
            birthdate = record.cleaned_data['birthdate'],
            civilstatus = record.cleaned_data['civilstatus'],
            citizenship = record.cleaned_data['citizenship'],
            religion = record.cleaned_data['religion'],
            bloodtype = record.cleaned_data['bloodtype'],
            numberofdependent = record.cleaned_data['numberofdependent'],
            presentaddress = record.cleaned_data['presentaddress'],
            permanentaddress = record.cleaned_data['permanentaddress'],
            contactnumber = record.cleaned_data['contactnumber'],
            spouseid = spousetemp)
            informationid = pinfostore
            
            recordstore = Employee.objects.create(
                informationid= informationid,
                employeeid=  record.cleaned_data['employeeid'],
                branch = branch,
                startdate = record.cleaned_data['startdate'],
                enddate = record.cleaned_data['enddate'],
                employmentstatus = record.cleaned_data['employmentstatus'],
                salarytype = record.cleaned_data['salarytype'],
                salary = record.cleaned_data['salary'],
                jobid = job
            )



            if emphistory.is_valid():
                emphistorystore = EmploymentHistory.objects.create(
                informationid=informationid, 
                previouscompanyname= emphistory.cleaned_data['previouscompanyname'],
                previousposition= emphistory.cleaned_data['previousposition'],
                reasonforleaving= emphistory.cleaned_data['reasonforleaving'],
                companycontactnumber= emphistory.cleaned_data['companycontactnumber'],
                withcoeorclearance= emphistory.cleaned_data['withcoeorclearance']
                )



            if education.is_valid():
                educationstore = EducationalBackground.objects.create(
                informationid=informationid,
                highestdegree= education.cleaned_data['highestdegree'],
                schoolname=education.cleaned_data['schoolname'],
                startingyearattended=education.cleaned_data['startingyearattended'],
                endingyearattended=education.cleaned_data['endingyearattended'],
                schooltype=education.cleaned_data['schooltype']
                )
  

            if family.is_valid():
                familystore = FamilyMemberBackground.objects.create(
                    informationid= informationid,
                    membername= family.cleaned_data['membername'],
                    memberage= family.cleaned_data['memberage'],
                    memberrelationship= family.cleaned_data['memberrelationship'],
                    memberoccupation= family.cleaned_data['memberoccupation']
                )
                

            if child.is_valid():
                childstore = ChildBackground.objects.create(
                childname= child.cleaned_data['childname'],
                childage= child.cleaned_data['childage'],
                childoccupation= child.cleaned_data['childoccupation'],
                informationid= informationid
                )
                
                
    
       
  
    context = {
    'record': record,
    'worklocation': worklocation,
    'position': position,
    'spouse': spouse,
    'emphistory': emphistory,
    'education': education ,
    'family': family,
    'child': child 
    } 
    return render(request, 'loginapp/create_record.html',context)



def logoutuser(request):
    logout(request)  
