from django.shortcuts import render
from django.core.mail import send_mail

from .models import PortAllocation

def index(request):
    #error messages to pass to view
    error_message_list = []

    context = {}

    if request.method=="POST":
        #get port form data
        data = request.POST.copy()
        ports = [int(data.get('input_port_one')),int(data.get('input_port_two'))]
        student_no = data.get('input_student_no')

        #validate port form data
        form_data_valid = True
        for port in ports:
            if port >= 61000 and port <= 61999:
                print(str(port) + " in port range")
            else:
                form_data_valid = False
                error_message_list.append("Port '" + str(port) + "' invalid: Must be between 61000-61999")

        if student_no.startswith('s') and len(student_no) == 8:
            try:
                student_no[-7:]
            except ValueError:
                form_data_valid = False
                error_message_list.append("Student number '" + student_no + "' invalid, must end in 7 digits")
        else:
            form_data_valid = False
            error_message_list.append("Student number '" + student_no + "' invalid, must begin with 's' and end in 7 digits")
        print("Data valid? " + str(form_data_valid))
        for error in error_message_list:
            print(error)
        
        #check ports available (in model)
        for port in ports:
            if PortAllocation.objects.filter(port_number=port).exists():
                print("Port number "+str(port)+" is taken!")
                form_data_valid = False
        
        #if form_data_valid remains true, add ports to db and send email for further processing
        if form_data_valid == True:
            PortAllocation.objects.create(port_number=ports[0],student=student_no)
            PortAllocation.objects.create(port_number=ports[1],student=student_no)
            send_mail(
                'Network Programming - Allocated Port Numbers',
                'Student Number: '+student_no+', Port 1: '+str(ports[0])+', Port 2: '+str(ports[1]),
                'portallocator@gmail.com',
                ['s3431583@student.rmit.edu.au'],
                fail_silently=False,
            )
            print("email sent!")

        #prepare context for render
        context = {
            'error_message_list': error_message_list,
            'form_data_valid': form_data_valid,
        }

    return render(request, 'portmanager/index.html', context)