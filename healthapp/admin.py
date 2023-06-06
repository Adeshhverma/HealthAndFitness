from django.contrib import admin
from .models import  Contact, Expert_detail, Feedback,HealthCompaign,HealthExpert,Patient, Tips, User_Message,BookingRequest

class HealthExpertAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','city','address')
    list_filter=['name','city']
    search_fields=('city','experttype')

class PatientAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','address')
    list_filter=['name','address']
    search_fields=('address',)
class userMessageAdmin(admin.ModelAdmin):
    list_display=('receiver_id','sender_id','subject','date')
    list_filter=['date']
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','date')
    list_filter=['date']

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('user_name','expert_name','rating','date')
    list_filter=['expert_name','rating']

class HealthCompaignAdmin(admin.ModelAdmin):
    list_display=('campaign_id','organizer_name','date',)
    list_filter=['organizer_name','date']
class TipsAdmin(admin.ModelAdmin):
    list_display=('Username','date',)
    list_filter=['Username','date']
class Expert_detailAdmin(admin.ModelAdmin):
    list_display=('user_name','experience','skills','highest_qualification')
    list_filter=['experience','skills','highest_qualification']
    search_fields=('experience','highest_qualification')

class BookingRequestAdmin(admin.ModelAdmin):
    list_display=('from_date','to_date','user_name','expert_user_name','request_date')
    list_filter=['request_date']
    search_fields=('request_date','expert_user_name')
   
admin.site.register(Contact,ContactAdmin)
admin.site.register(HealthCompaign,HealthCompaignAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(HealthExpert,HealthExpertAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(User_Message,userMessageAdmin)
admin.site.register(Tips,TipsAdmin)
admin.site.register(Expert_detail,Expert_detailAdmin)
admin.site.register(BookingRequest,BookingRequestAdmin)

admin.site.site_header= "Health & Fitness Admintration"
admin.site.site_title= "Health & Fitness Admin DashBoard"
admin.site.index_title="Welcome To Health & Fitness Portal" 

# Register your models here.
