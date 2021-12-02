from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Patient
from django.shortcuts import redirect
from .form import ArchiveForm


def return_session_id(request):
    try:
        id = request.session["user_id"]
        return id
    except:
        return False


def index(request):
    id = return_session_id(request)
    if id:
        return redirect('register/')
    
    template = loader.get_template('registr/index.html')
    if request.method == 'POST':

        uname = request.POST.get('uname')
        psw = request.POST.get('psw')

        try:
            user = User.objects.get(login=uname)
        except:
            context = {'is_not_exist': True}
            return HttpResponse(template.render(context, request))

        if psw == user.password:
            request.session['user_id'] = user.pk
            return redirect('register/')

        if psw != user.password:
            context = {'password_incorrect' : True}
            return HttpResponse(template.render(context, request))

    context = {'is_not_exist': False, 'password_incorrect' : False}
    return HttpResponse(template.render(context, request))

def choose(request):
    id = return_session_id(request)
    if not id:
        return redirect('/')
    
    user = User.objects.get(pk=id)
    template = loader.get_template('registr/choose.html')
    context = {'user': user}
    return HttpResponse(template.render(context, request))

def register_list(request, patient_type):
    id = return_session_id(request)
    if not id:
        return redirect('/')

    user = User.objects.get(pk=id)
    patients = Patient.objects.filter(type_register=str(patient_type))

    template = loader.get_template('registr/table.html')
    context = {'user': user, 'patients' : patients}

    return HttpResponse(template.render(context, request))

def adding(request, patient_type):
    id = return_session_id(request)
    if not id:
        return redirect('/')

    user = User.objects.get(pk=id)
    if user.access != '3':
        register_list(request, patient_type)

    if request.POST:
        diagnosis = request.POST.get('diagnosis')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        father_name = request.POST.get('father_name')
        date_birthday = request.POST.get('date_birthday')
        address = request.POST.get('address')
        dosage = request.POST.get('dosage')
        therapy = request.POST.get('therapy')
        monthly_need = request.POST.get('monthly_need')
        annual_need = request.POST.get('annual_need')
        last_editor = user
        type_register = patient_type
        form = ArchiveForm(request.POST, request.FILES)

        new_patient = Patient()
    
        new_patient.last_name = last_name
        new_patient.first_name = first_name
        new_patient.father_name = father_name
        new_patient.date_birthday = date_birthday
        new_patient.address = address
        new_patient.dosage = dosage
        new_patient.diagnosis = diagnosis
        new_patient.therapy = therapy
        new_patient.monthly_need = monthly_need
        new_patient.annual_need = annual_need
        new_patient.last_editor = last_editor
        new_patient.type_register = type_register
    
        if form.is_valid():
            form.save()
        
        new_patient.save()

        return register_list(request, patient_type)
    else:
        form = ArchiveForm()

    template = loader.get_template('register/adding.html')
    context = {'user': user, 'form': form}
    return HttpResponse(template.render(context, request))
        
def logout(request):
    id = return_session_id(request)
    if not id:
        return redirect('/')

    del request.session['user_id']
    return redirect('/')

def details(request, patient_type, patient_pk):
    id = return_session_id(request)
    if not id:
        return redirect('/')
    
    user = User.objects.get(pk=id)
    patient = Patient.objects.get(pk=patient_pk)
    
    if request.POST and user.access == '1':
        sname = request.POST.get("sname")
        fname = request.POST.get("fname")
        fathername = request.POST.get("fathername")
        dbirth = request.POST.get("dbirth")
        address = request.POST.get("address")
        dosage = request.POST.get("dosage")
        diagnosis = request.POST.get("diagnosis")
        therapy = request.POST.get("therapy")
        monthly_need = request.POST.get("monthly_need")
        annual_need = request.POST.get("annual_need")
        register = request.POST.get("register")
        
        patient.last_name = sname
        patient.first_name = fname
        patient.father_name = fathername
        patient.date_birthday = dbirth
        patient.address = address
        patient.diagnosis = diagnosis
        patient.therapy = therapy
        patient.monthly_need = monthly_need
        patient.annual_need = annual_need
        patient.type_register = register
        form = ArchiveForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        patient.save()
        return redirect(f"/register/{patient.type_register}/")
    else:
        form = ArchiveForm()
    
    template = loader.get_template('registr/patient.html')
    context = {'user': user, 'patient': patient, 'form': form}
    return HttpResponse(template.render(context, request))
    