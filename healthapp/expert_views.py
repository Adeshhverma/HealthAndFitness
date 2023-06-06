from distutils.command import upload
from tkinter import E
from django.shortcuts import render,HttpResponse,redirect
from.models import  HealthExpert,Tips,Expert_detail,BookingRequest
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
# def demo(request):
#     print("hello")
#     return HttpResponse(request,"<h1>hello<h1>")
def expertreg(request):
    
    if request.method=="GET": 
            
        return render (request,'healthapp/expert/expertreg.html')
    
    if request.method=="POST":
            e_username=request.POST["txtusername"]
            e_password=request.POST["txtpass"]
            e_name=request.POST["txtname"]
            e_email=request.POST["txtemail"]
            e_phone=request.POST["txtphone"]
    
            e_city=request.POST["txtcity"]
            e_address=request.POST["txtaddress"]
            e_gender=request.POST["txtgender"]
            e_experttype=request.POST["txtexpert"]
            healthExpert=HealthExpert(user_name=e_username,password=e_password,name=e_name,email=e_email,phone=e_phone,city=e_city,address=e_address,gender=e_gender,experttype=e_experttype) #creating object of Contact class
            healthExpert.save()
            print("Registration Done")
        
            messages.success(request,"ThankYou For Registration")
            return render(request,'healthapp/expert/expertreg.html')
    
def expert_login(request):
    
    if request.method=="GET":   
        return render (request,'healthapp/expert/expert.html')
          

    if request.method=="POST":
        username=request.POST["txtusername"]
        userpass=request.POST["txtpass"]
        p=HealthExpert.objects.filter(user_name=username,password=userpass)
        if len(p)>0:
            request.session["user_key"]=username
            request.session["user_type"]="HealthExpert"
            user_object=HealthExpert.objects.get(user_name=username)

            print(request.session["user_type"])
            context={
                    "userdata":user_object
            }
            return render (request,'healthapp/expert/expert_home.html',context)
            
        else:
            messages.error(request,"Invalid Credential")
            return redirect('expert_login')

def expert_editprofile(request):
    if "user_key" in request.session.keys():
        loggedinusername=request.session["user_key"]
    
        if request.method=="GET":
            
            user_object=HealthExpert.objects.get(user_name=loggedinusername)
            context={
                        "userdata":user_object
                    }
            return render (request,'healthapp/expert/expert_editprofile.html',context)
    else:
            messages.error(request,"Please do login First")
            return redirect('home')
    if request.method=="POST":
        uname=request.POST["txtname"]
        emailid=request.POST["txtemail"]
        phonenumber=request.POST["txtphone"]
        addr=request.POST["txtaddress"]
        print(emailid,phonenumber,addr)
        user_object=HealthExpert.objects.get(user_name=loggedinusername)
        user_object.email=emailid
        user_object.phone=phonenumber
        user_object.address=addr
        user_object.name=uname
        user_object.save()
        context={
                    "userdata":user_object
                }
        messages.success(request,"Profile Update Successfully")        


        return render (request,'healthapp/expert/expert_editprofile.html')


def expert_logout(request):
    del request.session["user_key"]
    del request.session["user_type"]
    return redirect ("expert_login")

class Tips_Management(View):
    def get(self,request):
        if "user_key" in request.session.keys():
            user_role=request.session['user_type']
            # print(user_role)
            
            if user_role=="HealthExpert":
                return render(request,'healthapp/expert/add_tips.html')
        else:
            messages.error(request,"Please do login First")
            return redirect('home')
    def post(self,request):
        u_name=request.session["user_key"]
        print(u_name)
        tips_content=request.POST['txtcontent']
        expert=HealthExpert.objects.get(user_name=u_name)
        print(expert.user_name)
        t=Tips(Username=expert,Tips_contents=tips_content)
        print(t)
        t.save()
        messages.success(request,"Tips submitted Successfully")
        return render (request,'healthapp/expert/add_tips.html')

class Add_Detail(View):
    def get(self,request):
        if "user_key" in request.session.keys():
            user_name=request.session['user_key']
            # print(user_role)
            user_object=HealthExpert.objects.get(user_name=user_name)
            context={
                        "userdata":user_object
                        }
            
            return render(request,'healthapp/expert/add_detail.html',context)
        else:
                messages.error(request,"Please do login First")
                return redirect('home')

    def post(self,request):
        user_name=request.session["user_key"]
        experience=request.POST['txtexperience']
        skill=request.POST['txtskill']
        about=request.POST['txtabout']
        highest_qualification=request.POST['txtqualification']
        hwexpert=HealthExpert.objects.get(user_name=user_name)
        
        a=Expert_detail(user_name=hwexpert,experience=experience,skills=skill,about=about,highest_qualification=highest_qualification)
      
        a.save()
        messages.error(request,"Detail Added Successfully")
        return redirect('add_detail')


class expert_viewbooking(View):
     def get(self, request):
          if "user_key" in request.session.keys():

               user_name=request.session["user_key"]
               booking=BookingRequest.objects.filter(expert_user_name=user_name)
               # print(booking)
               context={
                    "expert_user":booking  
               }
               
               return render(request,'healthapp/expert/expert_viewbooking.html',context)    
         
class Confirm_Booking(View):
     def get (self,request,id):
          if "user_key" in request.session.keys():

               user_name=request.session["user_key"]
               booking=BookingRequest.objects.filter(expert_user_name=user_name)
               # print(booking)
               context={
                    "expert_user":booking  
               }
               booking_request_obj=BookingRequest.objects.get(id=id)
               booking_request_obj.status="confirm"
               booking_request_obj.response_text="Booking has been confirmed"
               booking_request_obj.save()
               messages.success(request,"Booking has been confirmed")

               return render(request,'healthapp/expert/expert_viewbooking.html',context)     

class Cancel_Booking(View):
     def get (self,request,id):
          if "user_key" in request.session.keys():

               user_name=request.session["user_key"]
               booking=BookingRequest.objects.filter(expert_user_name=user_name)
               # print(booking)
               context={
                    "expert_user":booking  
               }
               booking_request_obj=BookingRequest.objects.get(id=id)
               booking_request_obj.status="cancel"
               booking_request_obj.response_text="Booking has been cancelled"
               booking_request_obj.save()
               messages.success(request,"Booking has been cancelled")

               return render(request,'healthapp/expert/expert_viewbooking.html',context)


def validate_expert_username(request):
    username=request.GET["username"]
    data={
        'exists':HealthExpert.objects.filter(user_name__iexact=username).exists()
    }
    return JsonResponse(data)


class Expert_Upload_Pic(View):
    def post(self,request):
        loggedinusername=request.session["user_key"]
        expert_pic=request.FILES['file_upload']
        print("fileupload",expert_pic)
        fs=FileSystemStorage()
        file_obj=fs.save(expert_pic.name,expert_pic)
        print("name",expert_pic.name)
        print("fileobj",file_obj)
        print("base",fs.base_url)
        uploaded_file_url=fs.url(file_obj)
        print("file urls is",uploaded_file_url)
        expert_obj=HealthExpert.objects.get(user_name=loggedinusername)
        expert_obj.pic_name=expert_pic.name
        expert_obj.save()
        context={
            "userdata":expert_obj,
            "file_url":uploaded_file_url
        }
        return render(request,'healthapp/expert/expert_home.html',context)
        


        


        