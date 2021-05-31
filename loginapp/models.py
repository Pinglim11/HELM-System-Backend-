# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from onesimus.settings import TIME_ZONE
from django.db import models

class Awards(models.Model):
    amemoreferencenumber = models.OneToOneField('Record', models.DO_NOTHING, db_column='aMemoReferenceNumber', primary_key=True)  # Field name made lowercase.
    awardissuer = models.CharField(db_column='awardIssuer', max_length=20)  # Field name made lowercase.
    awardpurpose = models.CharField(db_column='awardPurpose', max_length=20)  # Field name made lowercase.
    awardtype = models.CharField(db_column='awardType', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'awards'


class Awol(models.Model):
    noofoffense = models.IntegerField(db_column='noOfOffense')  # Field name made lowercase.
    hearingdate = models.DateTimeField(db_column='hearingDate', blank=True, null=True)  # Field name made lowercase.
    wnmemoreferencenumber = models.OneToOneField('Noac', models.DO_NOTHING, db_column='wNMemoReferenceNumber', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'awol'


class ChildBackground(models.Model):
    childname = models.CharField(db_column='childName', max_length=20)  # Field name made lowercase.
    childage = models.IntegerField(db_column='childAge', blank=True, null=True)  # Field name made lowercase.
    childoccupation = models.CharField(db_column='childOccupation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    childid = models.AutoField(db_column='childId', primary_key=True)  # Field name made lowercase.
    informationid = models.ForeignKey('EmployeePersonalInfo', models.DO_NOTHING, db_column='informationId')  # Field name made lowercase.
    def __str__(self):
        return 'id= ' + str(self.childid) + ', ' + self.childname + ' child of ' + self.informationid.employeename
    class Meta:
        managed = False
        db_table = 'child_background'



class Document(models.Model):
    documentid = models.AutoField(db_column='documentId', primary_key=True)  # Field name made lowercase.
    documentname = models.CharField(db_column='documentName', max_length=50)  # Field name made lowercase.
    documentlink = models.CharField(max_length=255)
    dateandtimecreated = models.DateTimeField(db_column='dateAndTimeCreated')  # Field name made lowercase.
    author = models.CharField(max_length=50)
    dateandtimelastedited = models.DateTimeField(db_column='dateAndTimeLastEdited', blank=True, null=True)  # Field name made lowercase.
    recenteditor = models.CharField(db_column='recentEditor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employeeId')  # Field name made lowercase.
    preparedby = models.CharField(db_column='preparedBy', max_length=20)  # Field name made lowercase.
    preparationdate = models.DateTimeField(db_column='preparationDate')  # Field name made lowercase.
    notedby = models.CharField(db_column='notedBy', max_length=20)  # Field name made lowercase.
    noteddate = models.DateTimeField(db_column='notedDate')  # Field name made lowercase.
    approvedby = models.CharField(db_column='approvedBy', max_length=20)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='approvedDate')  # Field name made lowercase.
    receivedby = models.CharField(db_column='receivedBy', max_length=20)  # Field name made lowercase.
    receiveddate = models.DateTimeField(db_column='receivedDate')  # Field name made lowercase.
    memoreferencenumber = models.ForeignKey('Record', models.DO_NOTHING, db_column='memoReferenceNumber', blank=True, null=True)  # Field name made lowercase.
    documenthide = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'document'


class EducationalBackground(models.Model):
    highestdegree = models.CharField(db_column='highestDegree', max_length=20, blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='schoolName', max_length=20)  # Field name made lowercase.
    startingyearattended = models.DateField(db_column='startingYearAttended')  # Field name made lowercase.
    endingyearattended = models.DateField(db_column='endingYearAttended')  # Field name made lowercase.
    schooltype = models.CharField(db_column='schoolType', max_length=15)  # Field name made lowercase.
    informationid = models.ForeignKey('EmployeePersonalInfo', models.DO_NOTHING, db_column='informationId')  # Field name made lowercase.
    degreeid = models.AutoField(db_column='degreeId', primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return 'id= ' + str(self.degreeid) + ', ' + self.informationid.employeename + ' studied at ' + self.schoolname + ' with degree of ' + self.schooltype
    class Meta:
        managed = False
        db_table = 'educational_background'


class EmergencyDetails(models.Model):
    emergencycontactnumber = models.IntegerField(db_column='emergencyContactNumber', primary_key=True)  # Field name made lowercase.
    emergencycontactname = models.CharField(db_column='emergencyContactName', max_length=20)  # Field name made lowercase.
    emergencyrelationship = models.CharField(db_column='emergencyRelationship', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emergencyaddress = models.CharField(db_column='emergencyAddress', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return str(self.emergencycontactnumber)
    class Meta:
        managed = False
        db_table = 'emergency_details'


class Employee(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', primary_key=True)  # Field name made lowercase.
    branch = models.ForeignKey('EmployeeWorkLocation', models.DO_NOTHING, db_column='branch', blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    employmentstatus = models.CharField(db_column='employmentStatus', max_length=15)  # Field name made lowercase.
    salarytype = models.CharField(db_column='salaryType', max_length=10)  # Field name made lowercase.
    salary = models.FloatField()
    jobid = models.ForeignKey('EmployeePosition', models.DO_NOTHING, db_column='jobId', blank=True, null=True)  # Field name made lowercase.
    informationid = models.ForeignKey('EmployeePersonalInfo', models.DO_NOTHING, db_column='informationId')  # Field name made lowercase.
    deletehide = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return 'id =' + str(self.employeeid) + ', ' + self.informationid.employeename
    class Meta:
        managed = False
        db_table = 'employee'


class EmployeePersonalInfo(models.Model):
    employeename = models.CharField(db_column='employeeName', max_length=20)  # Field name made lowercase.
    emergencycontactnumber = models.ForeignKey(EmergencyDetails, models.DO_NOTHING, db_column='emergencyContactNumber')  # Field name made lowercase.
    gender = models.CharField(max_length=10)
    birthdate = models.DateField(db_column='birthDate')  # Field name made lowercase.
    civilstatus = models.CharField(db_column='civilStatus', max_length=10)  # Field name made lowercase.
    citizenship = models.CharField(max_length=20)
    religion = models.CharField(max_length=20, blank=True, null=True)
    bloodtype = models.CharField(db_column='bloodType', max_length=10)  # Field name made lowercase.
    numberofdependent = models.IntegerField(db_column='numberOfDependent')  # Field name made lowercase.
    presentaddress = models.CharField(db_column='presentAddress', max_length=100)  # Field name made lowercase.
    permanentaddress = models.CharField(db_column='permanentAddress', max_length=100)  # Field name made lowercase.
    contactnumber = models.IntegerField(db_column='contactNumber')  # Field name made lowercase.
    spouseid = models.ForeignKey('SpouseBackground', models.DO_NOTHING, db_column='spouseId', blank=True, null=True)  # Field name made lowercase.
    informationid = models.AutoField(db_column='informationId', primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return self.employeename + ' id = ' + str(self.informationid)
    class Meta:
        managed = False
        db_table = 'employee_personal_info'


class EmployeePosition(models.Model):
    position = models.CharField(max_length=20)
    jobid = models.AutoField(db_column='jobId', primary_key=True)  # Field name made lowercase.
    department = models.CharField(max_length=20)
    def __str__(self):
        return self.department + ' , ' + self.position
    class Meta:
        managed = False
        db_table = 'employee_position'


class EmployeePositionHistory(models.Model):
    previousdepartment = models.CharField(db_column='previousDepartment', max_length=20)  # Field name made lowercase.
    previousposition_one = models.CharField(db_column='previousPosition_One', max_length=20)  # Field name made lowercase.
    previousbranch = models.CharField(db_column='previousBranch', max_length=20)  # Field name made lowercase.
    year = models.TextField()  # This field type is a guess.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeId')  # Field name made lowercase.
    pastpositionid = models.AutoField(db_column='pastPositionId', primary_key=True)  # Field name made lowercase.

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
    previouscompanyname = models.CharField(db_column='previousCompanyName', max_length=20)  # Field name made lowercase.
    previousposition = models.CharField(db_column='previousPosition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reasonforleaving = models.CharField(db_column='reasonForLeaving', max_length=20, blank=True, null=True)  # Field name made lowercase.
    companycontactnumber = models.CharField(db_column='companyContactNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    withcoeorclearance = models.CharField(db_column='withCOEorClearance', max_length=10)  # Field name made lowercase.
    employmenthistoryid = models.AutoField(db_column='employmentHistoryId', primary_key=True)  # Field name made lowercase.
    informationid = models.ForeignKey(EmployeePersonalInfo, models.DO_NOTHING, db_column='informationId')  # Field name made lowercase.
    def __str__(self):
        return 'id= ' + str(self.employmenthistoryid) + ', ' + self.informationid.employeename + ' Previously worked at ' + self.previouscompanyname
    class Meta:
        managed = False
        db_table = 'employment_history'


class FamilyMemberBackground(models.Model):
    membername = models.CharField(db_column='memberName', max_length=20)  # Field name made lowercase.
    memberage = models.IntegerField(db_column='memberAge', blank=True, null=True)  # Field name made lowercase.
    memberrelationship = models.CharField(db_column='memberRelationship', max_length=20)  # Field name made lowercase.
    memberoccupation = models.CharField(db_column='memberOccupation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    familyid = models.AutoField(db_column='familyId', primary_key=True)  # Field name made lowercase.
    informationid = models.ForeignKey(EmployeePersonalInfo, models.DO_NOTHING, db_column='informationId')  # Field name made lowercase.
    def __str__(self):
        return 'id= ' + str(self.familyid) + ', ' + self.membername + ' family member of ' + self.informationid.employeename
    class Meta:
        managed = False
        db_table = 'family_member_background'


class MajorOffense(models.Model):
    hearingdate = models.DateTimeField(db_column='hearingDate', blank=True, null=True)  # Field name made lowercase.
    mnmemoreferencenumber = models.OneToOneField('Noac', models.DO_NOTHING, db_column='mNMemoReferenceNumber', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'major_offense'


class Noac(models.Model):
    nmemoreferencenumber = models.OneToOneField('Record', models.DO_NOTHING, db_column='nMemoReferenceNumber', primary_key=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=50, blank=True, null=True)
    noactype = models.CharField(db_column='noacType', max_length=15)  # Field name made lowercase.
    sanction = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'noac'


class Record(models.Model):
    memoreferencenumber = models.IntegerField(db_column='memoReferenceNumber', primary_key=True)  # Field name made lowercase.
    recordname = models.CharField(db_column='recordName', max_length=20)  # Field name made lowercase.
    memodate = models.DateField(db_column='memoDate', blank=True, null=True)  # Field name made lowercase.
    issuingbranch = models.CharField(db_column='issuingBranch', max_length=20)  # Field name made lowercase.
    recorddescription = models.CharField(db_column='recordDescription', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recordtype = models.CharField(db_column='recordType', max_length=15)  # Field name made lowercase.
    issuingdepartment = models.CharField(db_column='issuingDepartment', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'record'


class SpouseBackground(models.Model):
    spousename = models.CharField(db_column='spouseName', max_length=20)  # Field name made lowercase.
    spousecompany = models.CharField(db_column='spouseCompany', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spousecompanyaddress = models.CharField(db_column='spouseCompanyAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numberofchildren = models.IntegerField(db_column='numberOfChildren', blank=True, null=True, default=0)  # Field name made lowercase.
    spouseid = models.AutoField(db_column='spouseId', primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return self.spousename + ', id = ' + str(self.spouseid)
    class Meta:
        managed = False
        db_table = 'spouse_background'


class Timekeeping(models.Model):
    noofoffense = models.IntegerField(db_column='noOfOffense')  # Field name made lowercase.
    tnmemoreferencenumber = models.OneToOneField(Noac, models.DO_NOTHING, db_column='tNMemoReferenceNumber', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timekeeping'
