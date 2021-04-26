from django.shortcuts import render 
from django.shortcuts import redirect 
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
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

@login_required
def employeeprof(request,empid):
    record = get_object_or_404(Employee, employeeid=empid)
    return render(request, 'loginapp/prof.html', {'employee': record})

@login_required
def employeedelete(request,empid):
    Employee.objects.filter(pk=empid).delete()
    return redirect('viewtest') #change for final product
    

@login_required
def employeeedit(request,empid):
    employee = get_object_or_404(Employee, employeeid=empid)
    information = employee.informationid
    emergency = information.emergencycontactnumber
    spouse = information.spouseid
    emphistory = EmploymentHistory.objects.filter(informationid=information)
    education = EducationalBackground.objects.filter(informationid=information)
    family = FamilyMemberBackground.objects.filter(informationid=information)
    children = ChildBackground.objects.filter(informationid=information)
    requiredData = {
    'employeeid': employee.employeeid,
    'startdate': employee.startdate,
    'enddate' : employee.enddate,
    'employmentstatus' : employee.employmentstatus,
    'salarytype' : employee.salarytype,
    'salary': employee.salary,
    'branch': employee.branch,
    'jobid': employee.jobid,
    'employeename'  : information.employeename,
    'gender' : information.gender,
    'birthdate' : information.birthdate,
    'civilstatus' : information.civilstatus,
    'citizenship' : information.citizenship,
    'religion' : information.religion,
    'bloodtype' : information.bloodtype,
    'numberofdependent' : information.numberofdependent,
    'presentaddress' : information.presentaddress,
    'permanentaddress' : information.permanentaddress,
    'contactnumber' : information.contactnumber,
    #Emergency Details
    'emergencycontactnumber' : emergency.emergencycontactnumber,
    'emergencycontactname' : emergency.emergencycontactname,
    'emergencyrelationship' : emergency.emergencyrelationship,
    'emergencyaddress' : emergency.emergencyaddress,
    }
    spouseData = {}
    emphistoryData = []
    educationData = []
    familyData = []
    childrenData = []
    if spouse != None:
        spouseData['spousename'] = spouse.spousename
        spouseData['spousecompany'] = spouse.spousecompany
        spouseData['spousecompanyaddress'] = spouse.spousecompanyaddress
        spouseData['numberofchildren'] = spouse.numberofchildren
    
    for history in emphistory:
        dic = {
            'previouscompanyname': history.previouscompanyname,
            'previousposition'  : history.previousposition,
            'reasonforleaving'   : history.reasonforleaving,
            'companycontactnumber' : history.companycontactnumber,
            'withcoeorclearance' : history.withcoeorclearance,
        }
        emphistoryData.append(dic)
    
    for background in education:
        dic = {
            'highestdegree': background.highestdegree,
            'schoolname'  : background.schoolname,
            'startingyearattended'   : background.startingyearattended,
            'endingyearattended' : background.endingyearattended,
            'schooltype' : background.schooltype,
        }
        educationData.append(dic)


    for member in family:
        dic = {
            'membername': member.membername,
            'memberage'  : member.memberage,
            'memberrelationship'   : member.memberrelationship,
            'memberoccupation' : member.memberoccupation,
        }
        familyData.append(dic)

    for child in children:
        dic = {
            'childname': child.childname,
            'childage'  : child.childage,
            'childoccupation'   : child.childoccupation,
        }
        childrenData.append(dic)
    recordform = EmployeeRequiredRecordForm(requiredData) 
    spouseform = SpouseForm(spouseData) 
    emphistoryform = formset_factory(EmploymentHistoryForm )(initial = emphistoryData)
    educationform = formset_factory(EducationalBackgroundForm )(initial = educationData)
    familyform = formset_factory(FamilyMemberBackgroundForm )(initial = familyData)
    childform = formset_factory(ChildBackgroundForm)(initial = childrenData)

    context = {
    'employee': employee,
    'record': recordform,
    'spouse': spouseform,
    'emphistory': emphistoryform,
    'education': educationform ,
    'family': familyform,
    'child': childform 
    } 
    return render(request, 'loginapp/edit.html', context)

@login_required
def viewtest(request):
    employees = Employee.objects.all().order_by('employeeid')
    context = {
    'employees': employees,
    } 
    return render(request, 'loginapp/viewtest.html',context)


def testing(request):

    record = EmployeeRequiredRecordForm() 
    #worklocation = BranchForm() 
    #position = JobsForm()
    spouse = SpouseForm() 
    emphistory = formset_factory(EmploymentHistoryForm)
    education = formset_factory(EducationalBackgroundForm)
    family = formset_factory(FamilyMemberBackgroundForm)
    child = formset_factory(ChildBackgroundForm)

    # check if form data is valid 
    if request.method == "POST":
        record = EmployeeRequiredRecordForm(request.POST) 
        #worklocation = BranchForm(request.POST) 
       # position = JobsForm(request.POST)
        spouse = SpouseForm(request.POST)    


        if record.is_valid(): 
            branch = record.cleaned_data['branch']
            job = record.cleaned_data['jobid']
            spousetemp = None
            emergency = None
            informationid = None
            #Check if worklocation already exist, These are temporary, can be a dropdown foreign key thing in the future if ever
            # if worklocation.is_valid():
            #     branchcheck = checkmodel(EmployeeWorkLocation, branch = worklocation.cleaned_data['branch'])
            #     if branchcheck == None:
            #         workstore = EmployeeWorkLocation.objects.create(branch = worklocation.cleaned_data['branch'], region = worklocation.cleaned_data['region'])
            #         branch = workstore
            #     else:
            #         branch = branchcheck
                

            # if position.is_valid():
            #     deptarg = Q(department__contains = position.cleaned_data['department'])
            #     jobarg = Q(position__contains = position.cleaned_data['position'])
            #     positioncheck = checkmodelq(EmployeePosition, deptarg & jobarg)
            #     if positioncheck == None:
            #         posstore = EmployeePosition.objects.create(position = position.cleaned_data['position'], department = position.cleaned_data['department'])
            #         job = posstore
            #     else:
            #         job = positioncheck
            
            if spouse.is_valid():
                if spouse.cleaned_data['spousename'] != None and spouse.cleaned_data['spousecompany'] != None and spouse.cleaned_data['numberofchildren'] != None:
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


            emphistory = emphistory(request.POST)
            education = education(request.POST)
            family = family(request.POST)
            child = child(request.POST)
            #if emphistory.is_valid():
            for histories in emphistory:
                if histories.is_valid():
                    emphistorystore = EmploymentHistory.objects.create(
                    informationid=informationid, 
                    previouscompanyname= histories.cleaned_data['previouscompanyname'],
                    previousposition= histories.cleaned_data['previousposition'],
                    reasonforleaving= histories.cleaned_data['reasonforleaving'],
                    companycontactnumber= histories.cleaned_data['companycontactnumber'],
                    withcoeorclearance= histories.cleaned_data['withcoeorclearance']
                    )


            for educations in education:
                if educations.is_valid():
                    educationstore = EducationalBackground.objects.create(
                    informationid=informationid,
                    highestdegree= educations.cleaned_data['highestdegree'],
                    schoolname=educations.cleaned_data['schoolname'],
                    startingyearattended=educations.cleaned_data['startingyearattended'],
                    endingyearattended=educations.cleaned_data['endingyearattended'],
                    schooltype=educations.cleaned_data['schooltype']
                    )
  
            for fammembers in family:
                if fammembers.is_valid():
                    familystore = FamilyMemberBackground.objects.create(
                        informationid= informationid,
                        membername= fammembers.cleaned_data['membername'],
                        memberage= fammembers.cleaned_data['memberage'],
                        memberrelationship= fammembers.cleaned_data['memberrelationship'],
                        memberoccupation= fammembers.cleaned_data['memberoccupation']
                    )
                
            for children in child:
                if children.is_valid():
                    childstore = ChildBackground.objects.create(
                    childname= children.cleaned_data['childname'],
                    childage= children.cleaned_data['childage'],
                    childoccupation= children.cleaned_data['childoccupation'],
                    informationid= informationid
                    )
                
                
    
       
  
    context = {
    'record': record,
    #'worklocation': worklocation,
   # 'position': position,
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
