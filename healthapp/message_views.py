from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import redirect, render
from.models import User_Message
from django.views import View
from django.contrib import messages

class Compose_Message(View):
    def get(self,request):
        if "user_key" in request.session.keys():
            user_role=request.session['user_type']
            print(user_role)
            if user_role=="patient":
                return render(request,'healthapp/patient/compose_message.html')
            if user_role=="HealthExpert":
                return render(request,'healthapp/expert/compose_message.html')
        else:
            messages.error(request,"Please do login First")
            return redirect('home')
    def post(self,request):
        user_role=request.session["user_type"]
        receiver_id=request.POST['txtreceiver']
        sender_id=request.session['user_key']
        subject=request.POST['txtsubject']
        messege_content=request.POST['txtcontent']
        user_msg=User_Message(receiver_id=receiver_id,sender_id=sender_id,subject=subject,content=messege_content,)
        user_msg.save()
        if user_role=="patient":
            return render(request,'healthapp/patient/compose_message.html')
        if user_role=="HealthExpert":
            return render(request,'healthapp/expert/compose_message.html')

class user_Inbox(View):
   
    def get(self,request):
        if "user_key" in request.session.keys():
            user_id=request.session['user_key']
            user_role=request.session['user_type']
            message_objects=User_Message.objects.filter(receiver_id=user_id)#returns multiple object
            print(message_objects)
            context={
                "msg":message_objects
            }
            if user_role=="patient":
                return render(request,'healthapp/patient/patient_inbox.html',context)
            if user_role=="HealthExpert":
                return render(request,'healthapp/expert/expert_inbox.html',context)
        else:
            messages.error(request,"Please do login First")
            return redirect('home')            
class Delete_Message(View):
    def post(self,request):
        user_id=request.session["user_key"]
        user_role=request.session["user_type"]
        message_objects_list = request.POST.getlist("chk")
        #print(message_objects_list)
        for msg_id in message_objects_list:
            #print(msg_id)
            msg_object=User_Message.objects.get(id=msg_id)
            msg_object.delete()
        message_objects=User_Message.objects.filter(receiver_id=user_id)
        context={
            "msg":message_objects
        }
        if user_role=="patient":
                return render(request,'healthapp/patient/patient_inbox.html',context)
        if user_role=="HealthExpert":
                return render(request,'healthapp/expert/expert_inbox.html',context)


class Show_Message(View):
    def get(self,request,msg_id):
        user_id=request.session["user_key"]
        user_role=request.session["user_type"]
        message_object=User_Message.objects.get(id=msg_id)
        print(message_object)
        context={
            "msg":message_object        }
        if user_role=="patient":
                return render(request,'healthapp/patient/patient_show_message.html',context)
        if user_role=="HealthExpert":
                return render(request,'healthapp/expert/expert_show_message.html',context)