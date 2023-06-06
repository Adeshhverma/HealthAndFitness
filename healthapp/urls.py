from django.urls import path
from .import views,expert_views,message_views
urlpatterns = [
   
   path ("",views.home,name="home"),
   path ("aboutus/",views.aboutus,name="aboutus"),
   path ("contactus/",views.contactus,name="contactus"),
   path("expert_login/",expert_views.expert_login,name="expert_login"),
   path("patient_login/",views.patient_login,name="patient_login"),
  # path("expert/",views.expert,name="expert"),
   path("expertreg/",expert_views.expertreg,name="expertreg"),
   path("patientreg/",views.patientreg,name="patientreg"),
   path("patient_logout/",views.patient_logout,name="patient_logout"),
   path("expert_logout/",expert_views.expert_logout,name="expert_logout"),
   path("patient_editprofile/",views.patient_editprofile,name="patient_editprofile"),
   path("expert_editprofile/",expert_views.expert_editprofile,name="expert_editprofile"),
   path("trail/",views.trail,name="trail"),
   path("compose_message/",message_views.Compose_Message.as_view(),name="compose_message"),
   path("user_inbox/",message_views.user_Inbox.as_view(),name="user_inbox"),
   path("delete_message/",message_views.Delete_Message.as_view(),name="delete_message"),
   path("show_message/<int:msg_id>",message_views.Show_Message.as_view(),name="show_message"),
   path("add_tips/",expert_views.Tips_Management.as_view(),name="add_tips"),
   path("add_detail/",expert_views.Add_Detail.as_view(),name="add_detail"),
   path("view_expert/",views.View_expert.as_view(),name="view_expert"),
   path("booking_request/<str:expert_id>",views.booking_request.as_view(),name="booking_request"),
   path("final_booking_request/",views.final_booking_request.as_view(),name="final_booking_request"),
   
   # path("patient_view_expert/",views.View_expert.as_view(),name="patient_view_expert")

   
   path("expert_viewbooking/",expert_views.expert_viewbooking.as_view(),name="expert_viewbooking"),
   path("confirm_booking/<int:id>/",expert_views.Confirm_Booking.as_view(),name="confirm_booking"),
   path("cancel_booking/<int:id>/",expert_views.Cancel_Booking.as_view(),name="cancel_booking"),
   path("booking_detail/",views.Booking_Detail.as_view(),name="booking_detail"),


   path("feedback/<str:expert_name>",views.feedbacks.as_view(),name="feedback"),

   path('validate_username/',views.validate_username,name='validate_username'),
   path('validate_expert_username/',expert_views.validate_expert_username,name='validate_expert_username'),
   path("review/",views.Review.as_view(),name="review"),
   path("expert_upload_pic/",expert_views.Expert_Upload_Pic.as_view(),name="expert_upload_pic"),
   path("search/<str:exptype>/",views.SearchResult.as_view(),name="search"),
   path("healthstatus/",views.Healthstatus.as_view(),name="healthstatus")


    
]

