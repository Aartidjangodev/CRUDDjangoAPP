from django.shortcuts import render,redirect
from .models import Student,Country

# Create your views here.
def loadForm(request):
    vcntry=Country.objects.all() # fetch all the countries
    return render(request,'student_form.html',{'cntry':vcntry})# dictionary
def insertRecord(request):
    if request.method=='POST':
        vname=request.POST.get('sname') # it get value  from textbox
        vgender=request.POST.get('gender') #fetch gender
        vhobbies = request.POST.getlist('chk[]') # get the list of the checkbox
        vcountry=request.POST.get('country') # get the country from select tag
        obj=Student() # create of student class
        obj.name=vname # save the value of textbox in student table name field
        obj.gender=vgender #save the gender value
        obj.hobbies = vhobbies # save the hobbies
        obj.countryid=vcountry
        obj.save()
        return redirect('/') # send the page to the show page not studentForm
    else:
        return render(request,'student_form.html')
def showRecords(request):
        #obj=Student.objects.all() # to fetch all the records from Student table
        obj=Student.objects.raw(
            'SELECT * FROM mysqlcrudapp_student LEFT JOIN mysqlcrudapp_country ON mysqlcrudapp_student.countryid=mysqlcrudapp_country.id')

        return render(request,'show_students.html',{'data':obj})
def deleteRecord(request,sid):
    std=Student.objects.get(id=sid) #get the id of the student
    std.delete()
    return redirect('/')  #show page view
def getRecordbyID(request,sid):
    vcntry=Country.objects.all()
    std=Student.objects.get(id=sid)# get the records by id
    return render(request,'editStudent.html',{'data':std,'cntry':vcntry})
def updateRecord(request,sid):
    std=Student.objects.get(id=sid)

    vname=request.POST.get('sname')#fetch the value from textbox
    vgender=request.POST.get('gender')
    vhobbies = request.POST.getlist('chk[]') # get the list of the checkbox
    vcountry=request.POST.get('country')
    std.name=vname # save value i the model field
    std.gender=vgender
    std.hobbies=vhobbies
    std.countryid=vcountry
    std.save()
    return redirect('/')

# SELECT * FROM mysqlcrudapp_student LEFT JOIN mysqlcrudapp_country ON mysqlcrudapp_student.countryid=mysqlcrudapp_country.id;