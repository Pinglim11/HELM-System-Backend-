
#from onesimus.settings import TIME_ZONE
from django.db import models

class Awards(models.Model):
    amemoreferencenumber = models.OneToOneField('Record', models.DO_NOTHING, db_column='aMemoReferenceNumber', primary_key=True)  
    awardissuer = models.CharField(db_column='awardIssuer', max_length=100)  
    awardpurpose = models.CharField(db_column='awardPurpose', max_length=100)  
    awardtype = models.CharField(db_column='awardType', max_length=20)  

    class Meta:
        managed = False
        db_table = 'awards'


class Awol(models.Model):
    noofoffense = models.IntegerField(db_column='noOfOffense')  
    hearingdate = models.DateTimeField(db_column='hearingDate', blank=True, null=True)  
    wnmemoreferencenumber = models.OneToOneField('Noac', models.DO_NOTHING, db_column='wNMemoReferenceNumber', primary_key=True)  

    class Meta:
        managed = False
        db_table = 'awol'


class ChildBackground(models.Model):
    childname = models.CharField(db_column='childName', max_length=100)  
    childage = models.IntegerField(db_column='childAge', blank=True, null=True)  
    childoccupation = models.CharField(db_column='childOccupation', max_length=20, blank=True, null=True)  
    childid = models.AutoField(db_column='childId', primary_key=True)  
    informationid = models.ForeignKey('EmployeePersonalInfo', models.DO_NOTHING, db_column='informationId')  
    def __str__(self):
        return 'id= ' + str(self.childid) + ', ' + self.childname + ' child of ' + self.informationid.employeename
    class Meta:
        managed = False
        db_table = 'child_background'


class Document(models.Model):
    documentid = models.AutoField(db_column='documentId', primary_key=True)  
    documentname = models.CharField(db_column='documentName', max_length=100)  
    documentlink = models.CharField(max_length=255)
    dateandtimecreated = models.DateTimeField(db_column='dateAndTimeCreated')  
    author = models.CharField(max_length=50)
    dateandtimelastedited = models.DateTimeField(db_column='dateAndTimeLastEdited', blank=True, null=True)  
    recenteditor = models.CharField(db_column='recentEditor', max_length=50, blank=True, null=True)  
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employeeId')  
    preparedby = models.CharField(db_column='preparedBy', max_length=100)  
    preparationdate = models.DateTimeField(db_column='preparationDate')  
    notedby = models.CharField(db_column='notedBy', max_length=100)  
    noteddate = models.DateTimeField(db_column='notedDate')  
    approvedby = models.CharField(db_column='approvedBy', max_length=100)  
    approveddate = models.DateTimeField(db_column='approvedDate')  
    receivedby = models.CharField(db_column='receivedBy', max_length=100)  
    receiveddate = models.DateTimeField(db_column='receivedDate')  
    memoreferencenumber = models.ForeignKey('Record', models.DO_NOTHING, db_column='memoReferenceNumber', blank=True, null=True)  
    documenthide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document'


class EducationalBackground(models.Model):
    highestdegree = models.CharField(db_column='highestDegree', max_length=20, blank=True, null=True)  
    schoolname = models.CharField(db_column='schoolName', max_length=100)  
    startingyearattended = models.DateField(db_column='startingYearAttended')  
    endingyearattended = models.DateField(db_column='endingYearAttended')  
    schooltype = models.CharField(db_column='schoolType', max_length=15)  
    informationid = models.ForeignKey('EmployeePersonalInfo', models.DO_NOTHING, db_column='informationId')  
    degreeid = models.AutoField(db_column='degreeId', primary_key=True)  
    def __str__(self):
        return 'id= ' + str(self.degreeid) + ', ' + self.informationid.employeename + ' studied at ' + self.schoolname + ' with degree of ' + self.schooltype
    class Meta:
        managed = False
        db_table = 'educational_background'


class EmergencyDetails(models.Model):
    emergencycontactnumber = models.CharField(db_column='emergencyContactNumber', primary_key=True, max_length=20)  
    emergencycontactname = models.CharField(db_column='emergencyContactName', max_length=100)  
    emergencyrelationship = models.CharField(db_column='emergencyRelationship', max_length=20, blank=True, null=True)  
    emergencyaddress = models.CharField(db_column='emergencyAddress', max_length=255)  
    def __str__(self):
        return str(self.emergencycontactnumber)
    class Meta:
        managed = False
        db_table = 'emergency_details'


class Employee(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', primary_key=True)  
    branch = models.ForeignKey('EmployeeWorkLocation', models.DO_NOTHING, db_column='branch', blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate')  
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  
    employmentstatus = models.CharField(db_column='employmentStatus', max_length=15)  
    salarytype = models.CharField(db_column='salaryType', max_length=10)  
    salary = models.FloatField()
    jobid = models.ForeignKey('EmployeePosition', models.DO_NOTHING, db_column='jobId', blank=True, null=True)  
    informationid = models.ForeignKey('EmployeePersonalInfo', models.DO_NOTHING, db_column='informationId')  
    deletehide = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return 'id =' + str(self.employeeid) + ', ' + self.informationid.employeename
    class Meta:
        managed = False
        db_table = 'employee'


class EmployeePersonalInfo(models.Model):
    employeename = models.CharField(db_column='employeeName', max_length=100)  
    emergencycontactnumber = models.ForeignKey(EmergencyDetails, models.DO_NOTHING, db_column='emergencyContactNumber')  
    gender = models.CharField(max_length=10)
    birthdate = models.DateField(db_column='birthDate')  
    civilstatus = models.CharField(db_column='civilStatus', max_length=10)  
    citizenship = models.CharField(max_length=20)
    religion = models.CharField(max_length=20, blank=True, null=True)
    bloodtype = models.CharField(db_column='bloodType', max_length=10)  
    numberofdependent = models.IntegerField(db_column='numberOfDependent')  
    presentaddress = models.CharField(db_column='presentAddress', max_length=255)  
    permanentaddress = models.CharField(db_column='permanentAddress', max_length=255)  
    contactnumber = models.CharField(db_column='contactNumber', max_length=20)  
    spouseid = models.ForeignKey('SpouseBackground', models.DO_NOTHING, db_column='spouseId', blank=True, null=True)  
    informationid = models.AutoField(db_column='informationId', primary_key=True)  
    def __str__(self):
        return self.employeename + ' id = ' + str(self.informationid)
    class Meta:
        managed = False
        db_table = 'employee_personal_info'


class EmployeePosition(models.Model):
    position = models.CharField(max_length=20)
    jobid = models.AutoField(db_column='jobId', primary_key=True)  
    department = models.CharField(max_length=20)
    def __str__(self):
        return self.department + ' , ' + self.position
    class Meta:
        managed = False
        db_table = 'employee_position'


class EmployeePositionHistory(models.Model):
    previousdepartment = models.CharField(db_column='previousDepartment', max_length=20)  
    previousposition_one = models.CharField(db_column='previousPosition_One', max_length=20)  
    previousbranch = models.CharField(db_column='previousBranch', max_length=20)  
    year = models.TextField()  # This field type is a guess.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeId')  
    pastpositionid = models.AutoField(db_column='pastPositionId', primary_key=True)  

    class Meta:
        managed = False
        db_table = 'employee_position_history'


class EmployeeWorkLocation(models.Model):
    branch = models.CharField(primary_key=True, max_length=20)
    region = models.CharField(max_length=20)
    def __str__(self):
        return self.region + ' , ' + self.branch
    class Meta:
        managed = False
        db_table = 'employee_work_location'


class EmploymentHistory(models.Model):
    previouscompanyname = models.CharField(db_column='previousCompanyName', max_length=100)  
    previousposition = models.CharField(db_column='previousPosition', max_length=20, blank=True, null=True)  
    reasonforleaving = models.CharField(db_column='reasonForLeaving', max_length=255, blank=True, null=True)  
    companycontactnumber = models.CharField(db_column='companyContactNumber', max_length=20, blank=True, null=True)  
    withcoeorclearance = models.CharField(db_column='withCOEorClearance', max_length=10)  
    employmenthistoryid = models.AutoField(db_column='employmentHistoryId', primary_key=True)  
    informationid = models.ForeignKey(EmployeePersonalInfo, models.DO_NOTHING, db_column='informationId')  
    def __str__(self):
        return 'id= ' + str(self.employmenthistoryid) + ', ' + self.informationid.employeename + ' Previously worked at ' + self.previouscompanyname
    class Meta:
        managed = False
        db_table = 'employment_history'


class FamilyMemberBackground(models.Model):
    membername = models.CharField(db_column='memberName', max_length=100)  
    memberage = models.IntegerField(db_column='memberAge', blank=True, null=True)  
    memberrelationship = models.CharField(db_column='memberRelationship', max_length=20)  
    memberoccupation = models.CharField(db_column='memberOccupation', max_length=20, blank=True, null=True)  
    familyid = models.AutoField(db_column='familyId', primary_key=True)  
    informationid = models.ForeignKey(EmployeePersonalInfo, models.DO_NOTHING, db_column='informationId')  
    def __str__(self):
        return 'id= ' + str(self.familyid) + ', ' + self.membername + ' family member of ' + self.informationid.employeename
    class Meta:
        managed = False
        db_table = 'family_member_background'


class MajorOffense(models.Model):
    hearingdate = models.DateTimeField(db_column='hearingDate', blank=True, null=True)  
    mnmemoreferencenumber = models.OneToOneField('Noac', models.DO_NOTHING, db_column='mNMemoReferenceNumber', primary_key=True)  

    class Meta:
        managed = False
        db_table = 'major_offense'


class Noac(models.Model):
    nmemoreferencenumber = models.OneToOneField('Record', models.DO_NOTHING, db_column='nMemoReferenceNumber', primary_key=True)  
    remarks = models.TextField(blank=True, null=True)
    noactype = models.CharField(db_column='noacType', max_length=15)  
    sanction = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'noac'



class Record(models.Model):
    memoreferencenumber = models.IntegerField(db_column='memoReferenceNumber', primary_key=True)  
    recordname = models.CharField(db_column='recordName', max_length=100)  
    memodate = models.DateField(db_column='memoDate', blank=True, null=True)  
    issuingbranch = models.CharField(db_column='issuingBranch', max_length=20)  
    recorddescription = models.TextField(db_column='recordDescription', blank=True, null=True)  
    recordtype = models.CharField(db_column='recordType', max_length=15)  
    issuingdepartment = models.CharField(db_column='issuingDepartment', max_length=20)  

    class Meta:
        managed = False
        db_table = 'record'


class SpouseBackground(models.Model):
    spousename = models.CharField(db_column='spouseName', max_length=100)  
    spousecompany = models.CharField(db_column='spouseCompany', max_length=20, blank=True, null=True)  
    spousecompanyaddress = models.CharField(db_column='spouseCompanyAddress', max_length=255, blank=True, null=True)  
    numberofchildren = models.IntegerField(db_column='numberOfChildren', blank=True, null=True)  
    spouseid = models.AutoField(db_column='spouseId', primary_key=True)  
    def __str__(self):
        return self.spousename + ', id = ' + str(self.spouseid)
    class Meta:
        managed = False
        db_table = 'spouse_background'


class Timekeeping(models.Model):
    noofoffense = models.IntegerField(db_column='noOfOffense')  
    tnmemoreferencenumber = models.OneToOneField(Noac, models.DO_NOTHING, db_column='tNMemoReferenceNumber', primary_key=True)  

    class Meta:
        managed = False
        db_table = 'timekeeping'