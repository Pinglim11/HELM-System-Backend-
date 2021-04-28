from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
from .forms import EmployeeRequiredRecordForm,JobsForm, BranchForm, SpouseForm, EmploymentHistoryForm,EducationalBackgroundForm,FamilyMemberBackgroundForm,ChildBackgroundForm 
from .models import Employee, EmployeePersonalInfo,EmployeePosition,EmployeeWorkLocation, ChildBackground,SpouseBackground,FamilyMemberBackground,EducationalBackground,EmploymentHistory, EmergencyDetails, Document
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
    employees = Employee.objects.all().order_by('employeeid')
    context = {
    'employees': employees,
    'count': employees.count()
    } 
    return render(request, 'loginapp/employee_masterlist.html',context)

@login_required
def employeeprof(request,empid):
    employee = get_object_or_404(Employee, employeeid=empid)
    information = employee.informationid
    emergency = information.emergencycontactnumber
    spouse = information.spouseid
    emphistory = EmploymentHistory.objects.filter(informationid=information)
    education = EducationalBackground.objects.filter(informationid=information)
    family = FamilyMemberBackground.objects.filter(informationid=information)
    children = ChildBackground.objects.filter(informationid=information)
    degree = None
    if education.count() >= 1:
        degree = education[0].highestdegree
    context = {
        'employee': employee,
        'information': information,
        'emergency': emergency,
        'spouse': spouse,
        'degree': degree,
        'emphistory' :emphistory,
        'education':education,
        'family' :family,
        'children':children,

    }
    return render(request, 'loginapp/prof.html', context)

@login_required
def employeedelete(request,empid):
    employee = get_object_or_404(Employee, employeeid=empid)
    information = EmployeePersonalInfo.objects.get(pk = employee.informationid.informationid)
    emergency = EmergencyDetails.objects.get(pk = information.emergencycontactnumber.emergencycontactnumber)
    spouse = SpouseBackground.objects.get(pk = information.spouseid.spouseid)
    emphistory = EmploymentHistory.objects.filter(informationid=information)
    education = EducationalBackground.objects.filter(informationid=information)
    family = FamilyMemberBackground.objects.filter(informationid=information)
    children = ChildBackground.objects.filter(informationid=information)

    
    employee.delete()

    for history in emphistory:
        history.delete()
    
    for background in education:
        background.delete()


    for member in family:
        member.delete()

    for child in children:
        child.delete()
    
    information.delete()
    emergency.delete()

    if spouse:
        spouse.delete()
    
    


    return redirect('employeeform') #change for final product

@login_required
def employeeedit(request,empid):
    employee = get_object_or_404(Employee, employeeid=empid)
    information = employee.informationid
    emergency = EmergencyDetails.objects.get(pk = information.emergencycontactnumber.emergencycontactnumber)
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
    counts = [1,1,1,1]
    if spouse != None:
        spouseData['spousename'] = spouse.spousename
        spouseData['spousecompany'] = spouse.spousecompany
        spouseData['spousecompanyaddress'] = spouse.spousecompanyaddress
        spouseData['numberofchildren'] = spouse.numberofchildren
    
    for history in emphistory:
        counts[0] = 0
        dic = {
            'previouscompanyname': history.previouscompanyname,
            'previousposition'  : history.previousposition,
            'reasonforleaving'   : history.reasonforleaving,
            'companycontactnumber' : history.companycontactnumber,
            'withcoeorclearance' : history.withcoeorclearance,
        }
        emphistoryData.append(dic)
    
    for background in education:
        counts[1] = 0
        dic = {
            'highestdegree': background.highestdegree,
            'schoolname'  : background.schoolname,
            'startingyearattended'   : background.startingyearattended,
            'endingyearattended' : background.endingyearattended,
            'schooltype' : background.schooltype,
        }
        educationData.append(dic)


    for member in family:
        counts[2] = 0
        dic = {
            'membername': member.membername,
            'memberage'  : member.memberage,
            'memberrelationship'   : member.memberrelationship,
            'memberoccupation' : member.memberoccupation,
        }
        familyData.append(dic)

    for child in children:
        counts[3] = 0
        dic = {
            'childname': child.childname,
            'childage'  : child.childage,
            'childoccupation'   : child.childoccupation,
        }
        childrenData.append(dic)
    recordform = EmployeeRequiredRecordForm(requiredData) 
    recordform.fields['employeeid'].widget.attrs['readonly'] = True
    spouseform = SpouseForm(spouseData) 
    emphistoryform = formset_factory(EmploymentHistoryForm, extra = counts[0] )
   
    educationform = formset_factory(EducationalBackgroundForm, extra = 1 )
    
    familyform = formset_factory(FamilyMemberBackgroundForm, extra = counts[2] )
   
    childform = formset_factory(ChildBackgroundForm, extra = counts[3])
    


    if request.method == "POST":
        recordform = EmployeeRequiredRecordForm(request.POST) 
        spouseform = SpouseForm(request.POST)   
        emphistoryform = emphistoryform(request.POST)
        educationform = educationform(request.POST)
        familyform = familyform(request.POST)
        childform = childform(request.POST)
        print(educationform)
        if recordform.is_valid() and spouseform.is_valid() and emphistoryform.is_valid() and educationform.is_valid() and familyform.is_valid() and childform.is_valid():

            employee.startdate = recordform.cleaned_data['startdate']
            employee.enddate = recordform.cleaned_data['enddate']
            employee.employmentstatus = recordform.cleaned_data['employmentstatus']
            employee.salarytype = recordform.cleaned_data['salarytype']
            employee.salary = recordform.cleaned_data['salary']
            employee.branch = recordform.cleaned_data['branch']
            employee.jobid = recordform.cleaned_data['jobid']
            employee.save()


            information.employeename= recordform.cleaned_data['employeename']
            information.gender = recordform.cleaned_data['gender']
            information.birthdate = recordform.cleaned_data['birthdate']
            information.civilstatus = recordform.cleaned_data['civilstatus']
            information.citizenship = recordform.cleaned_data['citizenship']
            information.religion = recordform.cleaned_data['religion']
            information.bloodtype = recordform.cleaned_data['bloodtype']
            information.numberofdependent = recordform.cleaned_data['numberofdependent']
            information.presentaddress = recordform.cleaned_data['presentaddress']
            information.permanentaddress = recordform.cleaned_data['permanentaddress']
            information.contactnumber = recordform.cleaned_data['contactnumber']

            
            
            if spouse:
                spouse.spousename = spouseform.cleaned_data['spousename']
                spouse.spousecompany = spouseform.cleaned_data['spousecompany']
                spouse.spousecompanyaddress = spouseform.cleaned_data['spousecompanyaddress']
                spouse.numberofchildren = spouseform.cleaned_data['numberofchildren']
            elif spouseform.cleaned_data['spousename'] != None and spouseform.cleaned_data['spousecompany'] != None and spouseform.cleaned_data['numberofchildren'] != None:
                temp = SpouseBackground.objects.create(spousename = spouseform.cleaned_data['spousename'], spousecompany = spouseform.cleaned_data['spousecompany'], spousecompanyaddress = spouseform.cleaned_data['spousecompanyaddress'], numberofchildren = spouseform.cleaned_data['numberofchildren'])
                information.spouseid = temp
            
            if checkmodel(EmergencyDetails, emergencycontactnumber = recordform.cleaned_data['emergencycontactnumber']) != emergency and checkmodel(EmergencyDetails, emergencycontactnumber = recordform.cleaned_data['emergencycontactnumber']) != None:
                information.emergencycontactnumber = EmergencyDetails.objects.get(emergencycontactnumber = recordform.cleaned_data['emergencycontactnumber'])
                information.save()
                emergency.delete()
            else:
                emergency.emergencycontactnumber = recordform.cleaned_data['emergencycontactnumber']
                emergency.emergencycontactname= recordform.cleaned_data['emergencycontactname']
                emergency.emergencyrelationship= recordform.cleaned_data['emergencyrelationship']
                emergency.emergencyaddress=recordform.cleaned_data['emergencyaddress']
                emergency.save()
                information.save()


            counts = [0,0,0,0]
            totals = [0,0,0,0]
            

            for histories in emphistoryform:
                totals[0] += 1
            
            if totals[0] < emphistory.count():
                for x in range(1, totals[0], 1):
                    todel = emphistory[-x]
                    todel.delete()

            for histories in emphistoryform:
                counts[0] += 1
                if counts[0] <= emphistory.count():
                    curhistory = emphistory[counts[0] - 1]
                    if histories['previouscompanyname'].value() and histories['withcoeorclearance'].value():
                        curhistory.previouscompanyname= histories.cleaned_data['previouscompanyname']
                        curhistory.previousposition= histories.cleaned_data['previousposition']
                        curhistory.reasonforleaving= histories.cleaned_data['reasonforleaving']
                        curhistory.companycontactnumber= histories.cleaned_data['companycontactnumber']
                        curhistory.withcoeorclearance= histories.cleaned_data['withcoeorclearance']
                        curhistory.save()
                else:
                    if histories['previouscompanyname'].value() and histories['withcoeorclearance'].value():
                        EmploymentHistory.objects.create(
                        informationid=informationid, 
                        previouscompanyname= histories.cleaned_data['previouscompanyname'],
                        previousposition= histories.cleaned_data['previousposition'],
                        reasonforleaving= histories.cleaned_data['reasonforleaving'],
                        companycontactnumber= histories.cleaned_data['companycontactnumber'],
                        withcoeorclearance= histories.cleaned_data['withcoeorclearance']
                        )

            for educations in educationform:
                totals[1] += 1
            
            if totals[1] < education.count():
                for x in range(1, totals[1], 1):
                    todel = education[-x]
                    todel.delete()

            highest = None
            for educations in educationform:
                counts[1] += 1
                if counts[1] <= education.count():
                    cureducation = education[counts[1] - 1]
                    if educations['schoolname'].value() and educations['startingyearattended'].value() and educations['endingyearattended'].value():
                        if educationform[0] == educations:
                            highest = educations.cleaned_data['highestdegree']
                        cureducation.highestdegree= highest
                        cureducation.schoolname=educations.cleaned_data['schoolname']
                        cureducation.startingyearattended=educations.cleaned_data['startingyearattended']
                        cureducation.endingyearattended=educations.cleaned_data['endingyearattended']
                        cureducation.schooltype=educations.cleaned_data['schooltype']
                        cureducation.save()
                else:
                    if educations['schoolname'].value() and educations['startingyearattended'].value() and educations['endingyearattended'].value():
                        if educationform[0] == educations:
                            highest = educations.cleaned_data['highestdegree']
                        EducationalBackground.objects.create(
                        informationid=informationid,
                        highestdegree= highest,
                        schoolname=educations.cleaned_data['schoolname'],
                        startingyearattended=educations.cleaned_data['startingyearattended'],
                        endingyearattended=educations.cleaned_data['endingyearattended'],
                        schooltype=educations.cleaned_data['schooltype']
                        )

            for fammembers in familyform:
                totals[2] += 1
            
            if totals[2] < family.count():
                for x in range(1, totals[2], 1):
                    todel = family[-x]
                    todel.delete()
            
            for fammembers in familyform:
                counts[2] += 1
                if counts[2] <= family.count():
                    if fammembers['membername'].value():
                        curfam = family[counts[2] - 1]
                        curfam.membername= fammembers.cleaned_data['membername']
                        curfam.memberage= fammembers.cleaned_data['memberage']
                        curfam.memberrelationship= fammembers.cleaned_data['memberrelationship']
                        curfam.memberoccupation= fammembers.cleaned_data['memberoccupation']
                        curfam.save()
                        
                else:    
                    if fammembers['membername'].value():
                        FamilyMemberBackground.objects.create(
                            informationid= informationid,
                            membername= fammembers.cleaned_data['membername'],
                            memberage= fammembers.cleaned_data['memberage'],
                            memberrelationship= fammembers.cleaned_data['memberrelationship'],
                            memberoccupation= fammembers.cleaned_data['memberoccupation']
                        )
            for x in childform:
                totals[3] += 1
            
            if totals[3] < children.count():
                for x in range(1, totals[3], 1):
                    todel = child[-x]
                    todel.delete()
        
            for child in childform:
                counts[3] += 1
                if counts[3] <= children.count():
                    if child['childname'].value():
                        curchild = children[counts[3] - 1]
                        curchild.childname= child.cleaned_data['childname']
                        curchild.childage= child.cleaned_data['childage']
                        curchild.childoccupation= child.cleaned_data['childoccupation']
                        curchild.save()
                else:
                    if child['childname'].value():
                        ChildBackground.objects.create(
                        childname= child.cleaned_data['childname'],
                        childage= child.cleaned_data['childage'],
                        childoccupation= child.cleaned_data['childoccupation'],
                        informationid= informationid
                        )
    else:
        emphistoryform = emphistoryform(initial = emphistoryData)
   
        educationform = educationform(initial = educationData)
    
        familyform = familyform(initial = familyData)
   
        childform = childform(initial = childrenData)

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

@login_required
def viewtest_awards(request):
    employees = Employee.objects.all()
    documents = Document.objects.all()
    context = {
    'employees': employees,
    'documents': documents,
    } 
    return render(request, 'loginapp/viewtest_awards.html',context)

def testing(request):
    branch = formset_factory(BranchForm)
    if request.method == "POST":
        branch = branch(request.POST)

        if branch.is_valid():
            for branches in branch:
                EmployeeWorkLocation.objects.create(branch = branches.cleaned_data['branch'], region = branches.cleaned_data['region'])
    
    return render(request, 'loginapp/testing.html',{'branch' : branch})



def createrecord(request):

    record = EmployeeRequiredRecordForm() 
    #worklocation = BranchForm() 
    #position = JobsForm()
    spouse = SpouseForm() 
    emphistory = formset_factory(EmploymentHistoryForm, extra = 1 )
    education = formset_factory(EducationalBackgroundForm, extra = 1)
    family = formset_factory(FamilyMemberBackgroundForm, extra = 1)
    child = formset_factory(ChildBackgroundForm, extra = 1)

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


            if emphistory.is_valid():
                for histories in emphistory:
                    if histories['previouscompanyname'].value() and histories['withcoeorclearance'].value():
                        EmploymentHistory.objects.create(
                        informationid=informationid, 
                        previouscompanyname= histories.cleaned_data['previouscompanyname'],
                        previousposition= histories.cleaned_data['previousposition'],
                        reasonforleaving= histories.cleaned_data['reasonforleaving'],
                        companycontactnumber= histories.cleaned_data['companycontactnumber'],
                        withcoeorclearance= histories.cleaned_data['withcoeorclearance']
                        )
            if education.is_valid():
                highest = None
                for educations in education:
                    if educations['schoolname'].value() and educations['startingyearattended'].value() and educations['endingyearattended'].value():
                        if education[0] == educations:
                            highest = educations.cleaned_data['highestdegree']
                        EducationalBackground.objects.create(
                        informationid=informationid,
                        highestdegree= highest,
                        schoolname=educations.cleaned_data['schoolname'],
                        startingyearattended=educations.cleaned_data['startingyearattended'],
                        endingyearattended=educations.cleaned_data['endingyearattended'],
                        schooltype=educations.cleaned_data['schooltype']
                        )
            if family.is_valid():
                for fammembers in family:
                    if fammembers['membername'].value():
                        FamilyMemberBackground.objects.create(
                            informationid= informationid,
                            membername= fammembers.cleaned_data['membername'],
                            memberage= fammembers.cleaned_data['memberage'],
                            memberrelationship= fammembers.cleaned_data['memberrelationship'],
                            memberoccupation= fammembers.cleaned_data['memberoccupation']
                        )
            
            if child.is_valid():
                for children in child:
                    if children['childname'].value():
                        ChildBackground.objects.create(
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

# @login_required
# def createrecord(request):
#      # create object of form 
#     record = EmployeeRequiredRecordForm(request.POST) 
#     worklocation = BranchForm(request.POST) 
#     position = JobsForm(request.POST)
#     spouse = SpouseForm(request.POST) 
#     emphistory = EmploymentHistoryForm(request.POST) 
#     education = EducationalBackgroundForm(request.POST) 
#     family = FamilyMemberBackgroundForm(request.POST) 
#     child = ChildBackgroundForm (request.POST) 

#     # check if form data is valid 
#     if request.method == "POST":
        


#         if record.is_valid(): 
#             branch = None
#             job = None
#             spousetemp = None
#             emergency = None
#             informationid = None
#             #Check if worklocation already exist, These are temporary, can be a dropdown foreign key thing in the future if ever
#             if worklocation.is_valid():
#                 branchcheck = checkmodel(EmployeeWorkLocation, branch = worklocation.cleaned_data['branch'])
#                 if branchcheck == None:
#                     workstore = EmployeeWorkLocation.objects.create(branch = worklocation.cleaned_data['branch'], region = worklocation.cleaned_data['region'])
#                     branch = workstore
#                 else:
#                     branch = branchcheck
                

#             if position.is_valid():
#                 deptarg = Q(department__contains = position.cleaned_data['department'])
#                 jobarg = Q(position__contains = position.cleaned_data['position'])
#                 positioncheck = checkmodelq(EmployeePosition, deptarg & jobarg)
#                 if positioncheck == None:
#                     posstore = EmployeePosition.objects.create(position = position.cleaned_data['position'], department = position.cleaned_data['department'])
#                     job = posstore
#                 else:
#                     job = positioncheck
            
#             if spouse.is_valid():
#                 spousenamearg = Q(spousename__contains = spouse.cleaned_data['spousename'])
#                 spousecomparg = Q(spousecompany__contains = spouse.cleaned_data['spousecompany'])
#                 spousechildren = Q(numberofchildren__contains = spouse.cleaned_data['numberofchildren'])
#                 spousecheck = checkmodelq(SpouseBackground, spousenamearg & spousecomparg & spousechildren) 
#                 if spousecheck == None:
#                     spousestore = SpouseBackground.objects.create(spousename = spouse.cleaned_data['spousename'], spousecompany = spouse.cleaned_data['spousecompany'], spousecompanyaddress = spouse.cleaned_data['spousecompanyaddress'], numberofchildren = spouse.cleaned_data['numberofchildren'])
#                     spousetemp = spousestore
#                 else:
#                     spousetemp = spousecheck

            
#             emergencycheck = checkmodel(EmergencyDetails,emergencycontactnumber = record.cleaned_data['emergencycontactnumber'])

#             if  emergencycheck == None:
#                 emergencystore = EmergencyDetails.objects.create(emergencycontactnumber = record.cleaned_data['emergencycontactnumber'], emergencycontactname= record.cleaned_data['emergencycontactname'], emergencyrelationship= record.cleaned_data['emergencyrelationship'],emergencyaddress=record.cleaned_data['emergencyaddress'])
#                 emergency = emergencystore
#             else:
#                 emergency = emergencycheck

#             pinfostore = EmployeePersonalInfo.objects.create(emergencycontactnumber= emergency,
#             employeename= record.cleaned_data['employeename'], 
#             gender = record.cleaned_data['gender'], 
#             birthdate = record.cleaned_data['birthdate'],
#             civilstatus = record.cleaned_data['civilstatus'],
#             citizenship = record.cleaned_data['citizenship'],
#             religion = record.cleaned_data['religion'],
#             bloodtype = record.cleaned_data['bloodtype'],
#             numberofdependent = record.cleaned_data['numberofdependent'],
#             presentaddress = record.cleaned_data['presentaddress'],
#             permanentaddress = record.cleaned_data['permanentaddress'],
#             contactnumber = record.cleaned_data['contactnumber'],
#             spouseid = spousetemp)
#             informationid = pinfostore
            
#             recordstore = Employee.objects.create(
#                 informationid= informationid,
#                 employeeid=  record.cleaned_data['employeeid'],
#                 branch = branch,
#                 startdate = record.cleaned_data['startdate'],
#                 enddate = record.cleaned_data['enddate'],
#                 employmentstatus = record.cleaned_data['employmentstatus'],
#                 salarytype = record.cleaned_data['salarytype'],
#                 salary = record.cleaned_data['salary'],
#                 jobid = job
#             )



#             if emphistory.is_valid():
#                 emphistorystore = EmploymentHistory.objects.create(
#                 informationid=informationid, 
#                 previouscompanyname= emphistory.cleaned_data['previouscompanyname'],
#                 previousposition= emphistory.cleaned_data['previousposition'],
#                 reasonforleaving= emphistory.cleaned_data['reasonforleaving'],
#                 companycontactnumber= emphistory.cleaned_data['companycontactnumber'],
#                 withcoeorclearance= emphistory.cleaned_data['withcoeorclearance']
#                 )



#             if education.is_valid():
#                 educationstore = EducationalBackground.objects.create(
#                 informationid=informationid,
#                 highestdegree= education.cleaned_data['highestdegree'],
#                 schoolname=education.cleaned_data['schoolname'],
#                 startingyearattended=education.cleaned_data['startingyearattended'],
#                 endingyearattended=education.cleaned_data['endingyearattended'],
#                 schooltype=education.cleaned_data['schooltype']
#                 )
  

#             if family.is_valid():
#                 familystore = FamilyMemberBackground.objects.create(
#                     informationid= informationid,
#                     membername= family.cleaned_data['membername'],
#                     memberage= family.cleaned_data['memberage'],
#                     memberrelationship= family.cleaned_data['memberrelationship'],
#                     memberoccupation= family.cleaned_data['memberoccupation']
#                 )
                

#             if child.is_valid():
#                 childstore = ChildBackground.objects.create(
#                 childname= child.cleaned_data['childname'],
#                 childage= child.cleaned_data['childage'],
#                 childoccupation= child.cleaned_data['childoccupation'],
#                 informationid= informationid
#                 )
                
                
    
       
  
#     context = {
#     'record': record,
#     'worklocation': worklocation,
#     'position': position,
#     'spouse': spouse,
#     'emphistory': emphistory,
#     'education': education ,
#     'family': family,
#     'child': child 
#     } 
#     return render(request, 'loginapp/create_record.html',context)



def logoutuser(request):
    logout(request)  
