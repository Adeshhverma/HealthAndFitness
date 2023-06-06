
from multiprocessing import context
from django.shortcuts import redirect, render
from django.views import View
from .models import Contact,HealthCompaign, HealthExpert,Patient,Tips,Expert_detail,BookingRequest,Feedback
from django.contrib import messages
from django.http import JsonResponse
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Create your views here.
def home(request):
    # data_dict={
    #      "info":
    #      "Data from view"
    #  }
    campaign=HealthCompaign.objects.all()
    tips_obj=Tips.objects.all()
    context={
        "info":campaign,
        "tip":tips_obj
    }
   
    return render(request,'healthapp/html/home.html',context)
def aboutus(request):
    
    return render (request,'healthapp/html/aboutus.html')
def patient_login(request):
    if request.method=="GET":   
        return render (request,'healthapp/patient/login.html')
    if request.method=="POST":
        username=request.POST["txtusername"]
        userpass=request.POST["txtpass"]
        p=Patient.objects.filter(user_name=username,password=userpass)
        if len(p)>0:
            request.session["user_key"]=username
            request.session["user_type"]="patient"
            user_object=Patient.objects.get(user_name=username)

            context={
                    "userdata":user_object
            }
            return render (request,'healthapp/patient/patient_home.html',context)
        else:
            messages.error(request,"Invalid Credential")
            return redirect("patient_login")


def patientreg(request):
    
    if request.method=="GET":      
        return render (request,'healthapp/patient/patientreg.html')
    
    if request.method=="POST":
        p_username=request.POST["txtusername"]
        p_password=request.POST["txtpass"]
        p_name=request.POST["txtname"]
        p_email=request.POST["txtemail"]
        p_phone=request.POST["txtphone"]
        p_address=request.POST["txtaddress"]
        patient=Patient(user_name=p_username,password=p_password,name=p_name,email=p_email,phone=p_phone,address=p_address) #creating object of Contact class
        patient.save()
        print("Registration Done")
    
        messages.success(request,"ThankYou For Registration")
    return render(request,'healthapp/patient/patientreg.html')
    
def contactus(request):
    if request.method=="GET":
        return render(request,'healthapp/html/contactus.html')
    

    if request.method=="POST":
        print(request.POST) #built in dictionary
        cname=request.POST["txtname"]
        cemail=request.POST["txtemail"]
        cphone=request.POST["txtphone"]
        cquery=request.POST["txtquery"]
        #print(cname,cemail,cphone,cquery)
        contact=Contact(name=cname,email=cemail,phone=cphone,your_query=cquery) #creating object of Contact class
        contact.save()
        print("Contact added")
        messages.success(request,"ThankYou For Contacting Us")
    return render(request,'healthapp/html/conactus.html')

    #########code for patient logout############
def patient_logout(request):
    del request.session["user_key"]
    del request.session["user_type"]
    return redirect ("patient_login")


def patient_editprofile(request):
    if "user_key" in request.session.keys():
        loggedinusername=request.session["user_key"]
    
        if request.method=="GET":
            
            user_object=Patient.objects.get(user_name=loggedinusername)
            context={
                        "userdata":user_object
                    }
            return render (request,'healthapp/patient/patient_editprofile.html',context)
    else:
            messages.error(request,"Please do login First")
            return redirect('home')
    if request.method=="POST":
        uname=request.POST["txtname"]
        emailid=request.POST["txtemail"]
        phonenumber=request.POST["txtphone"]
        addr=request.POST["txtaddress"]
        print(emailid,phonenumber,addr)
        user_object=Patient.objects.get(user_name=loggedinusername)
        user_object.email=emailid
        user_object.phone=phonenumber
        user_object.address=addr
        user_object.name=uname
        user_object.save()
        context={
                    "userdata":user_object
                }
        messages.success(request,"Profile Update Successfully")        


        return render (request,'healthapp/patient/patient_editprofile.html')



def trail(request):
    
    return render (request,'healthapp/patient/trail.html')

class View_expert(View):
    def get(self,request):
        user_object=Expert_detail.objects.all()

        context={
                        "userdata":user_object
                    }
        
            
        if "user_key" in request.session.keys():
              
                
              return render(request,'healthapp/patient/patient_view_expert.html',context)
        else:
                return render(request,'healthapp/html/view_expert.html',context)

    
class booking_request(View):
    def get(self,request,expert_id):
        context={
            "eid":expert_id
        }        
                
        return render(request,'healthapp/patient/booking_request.html',context)


class final_booking_request(View):
        def post(self,request):
            u_name=request.session["user_key"]
            expert_id=request.POST['txtexpertid']
            from_date=request.POST["fromdate"]
            to_date=request.POST["todate"]
            message=request.POST["txtmessage"]
            p=Patient.objects.get(user_name=u_name)
        
            bk=BookingRequest(from_date=from_date,to_date=to_date,user_name=p,expert_user_name=expert_id,user_message_text=message)
            bk.save()
            return render(request,'healthapp/patient/booking_request.html')


class Booking_Detail(View):
    def get(self, request):    
          if "user_key" in request.session.keys():
                u_name=request.session["user_key"]

                booking_obj=BookingRequest.objects.filter(user_name=u_name)
                context={
                    "booking":booking_obj
                    }
                return render(request,'healthapp/patient/booking_detail.html',context)

class feedbacks(View):
   def get(self,request,expert_name):
        context={
            "exp_name":expert_name
        }        
                
        return render(request,'healthapp/patient/feedback.html',context)
class Final_Feedback(View):
    def post(self,request):
        u_name=request.session["user_key"]
        expert_id = request.POST["txtexpert_id"]
        feedback=request.POST["txtfeedback"]
        rating=request.POST["txtrating"]
        p=Patient.objects.get(user_name=u_name)
        f=Feedback(user_name=p,expert_name=expert_id,feedback_text=feedback,rating=rating)
        f.save()
        messages.success(request,"thanks you for feedback") 

        return render(request,'healthapp/patient/Feedback.html')



def validate_username(request):
    username=request.GET["username"]
    data={
        'exists':Patient.objects.filter(user_name__iexact=username).exists()
    }
    return JsonResponse(data)

class Review(View):
    def get(self,request):
        # user_object=Feedback.objects.all()

        # context={
        #                 "userdata":user_object
        #             }
             
                
        return render(request,'healthapp/html/feedback_review.html',context)


class SearchResult(View):
    
    def get(self,request,exptype):
        exp_list=[]
        exptype=HealthExpert.objects.filter(experttype=exptype)
        

        if(len(exptype)>0):

            
            context={
                "expdata":exptype
                
            }
            return render(request,'healthapp/html/search_result.html',context)

        else:
            messages.warning(request,"no data found") 
            return render(request,'healthapp/html/home.html')

class Healthstatus(View):
    def get(self,request):
        
              
                
              return render(request,'healthapp/html/healthstatus.html')

    def post(self,request):
       name=request.POST["txtname"]
       age=request.POST["txtage"]
       gender=request.POST["txtgender"]
       hemo=request.POST["txthemo"]
       weight=request.POST["txtweight"]
       lowerbp=request.POST["txtlowerbp"]
       upperbp=request.POST["txtupperbp"]
       heartbeat=request.POST["txtheartbeat"]
       print(name,age,gender,hemo,weight,lowerbp,upperbp,heartbeat)
       ml_model=joblib.load("ml_model/heathandfitness_modal.joblib")
       print(ml_model)
       predicted_value=ml_model.predict([[int(gender),float(hemo),int(heartbeat),int(upperbp),int(lowerbp)]])
       print(predicted_value)
       status=''
       str=predicted_value
       if str.__contains__("1"):
           status="you are healthy"
       else:
           status="take care of your health"

       context={
                "health":status
                
                }
       return render(request,'healthapp/html/healthstatus.html',context)
       

