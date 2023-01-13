from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from climate_app.models import *
from datetime import datetime
import os
from django.http import HttpResponse, Http404
from climate_app import functions
from climate_app import per_functions
from climate_app import countries_years
from base64 import b64encode
from django.views.decorators.cache import cache_control 
from django.core.files.storage import FileSystemStorage 

import requests
import random
# from asgiref.sync import sync_to_async,async_to_sync
# Create your views here.

from django.contrib import messages
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def index(request):
    reviews=review.objects.all()
    blogs=[i for i in blog.objects.all()]
    experts=[i for i in expert.objects.all()]
    random.shuffle(experts)
    random.shuffle(blogs)
    dashboard=False
    if request.session.has_key('email'):
          dashboard=True
    try:
     nasares=requests.get('https://api.nasa.gov/planetary/apod?api_key=ZQm1OlM8i5SkkXGsbUYhOH2NGhJyAdWjMr9TH6gM').json()  
     response=lambda:requests.get('https://api.unsplash.com/photos/random?query=climate&client_id=8TYss-fyoFCbM5KW5ctaKZViRgptiSMSirRXKYmBNi4').json()
     print(nasares['hdurl'])

     l=[response()['urls']['full'] for x in range(0,2)]
     return render(request,'index.html',{'images':l,'nnpic':nasares['hdurl'],'reviews':reviews,'exps':experts,'bgs':blogs,'header':dashboard,'index':True})
    except:
        return render(request,'index.html',{'reviews':reviews,'exps':experts,'bgs':blogs,'header':dashboard,'index':True})
def sidebar(request):
    all_entities=entitie.objects.all()
    if not request.session.has_key('email'):
         return redirect('index')
    return render(request,'sidebar.html',{'datasets':all_entities})    
def myreview(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    if request.method=='POST':
        user=user_register.objects.get(user_email=request.session['email'])
        rev=review()
        rev.user_name=user.user_email
        rev.heading=request.POST.get('heading')
        rev.description=request.POST.get('description')
        rev.save()
        msg="data added"
        return render(request,'review.html',{'msg':msg})
    else:
        return render(request,'review.html',{})
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def my_profile_details(request):
    if not request.session.has_key('email'):
        return redirect('login')    
    all_entities=entitie.objects.all()      
    user=user_register.objects.get(user_email=request.session['email'])

    return render(request, 'myprofiledetails.html',{'user':user,'datasets':all_entities})
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def edit_profile(request):
    if not request.session.has_key('email'):
        return render(request,'login.html',{'data':'loggedout'})
    all_entities=entitie.objects.all()       
    user=user_register.objects.get(user_email=request.session['email'])
    if request.method=='POST':
         pic=request.FILES['prpics']
         user.profile_pic=pic
         user.fname=request.POST.get('firstname')
         user.lname=request.POST.get('lastname')
         user.dob=request.POST.get('dob')
         user.address=request.POST.get('address')
         user.city=request.POST.get('city')
         user.pincode=request.POST.get('pincode')
         user.save()
         
         return render(request, 'edit_profile.html',{'user':user,'added':'data added','datasets':all_entities})    
             
    
   
    return render(request, 'edit_profile.html',{'user':user,'datasets':all_entities}) 
# def add_profile_pic(request):
#     if not request.session.has_key('email'):
#         return redirect('login') 
#     user=user_register.objects.get(user_email=request.session['email'])

#     if request.method==POST:
#         user.profile_pic=request.POST.get('prpic')
#         user.save()
#         return render(request, 'edit_profile.html',{'user':user,'added':'data added','datasets':all_entities})    

def dashboard_welcome(request):
    all_entities=entitie.objects.all()     
    return render(request,'dash-board.html',{'datasets':all_entities})

def logout(request):
    if not request.session.has_key('email'):
        return redirect('/login')    
    del request.session['email']
    return redirect('/login')     

def login(request):
   if request.method=='POST': 
    get_email=request.POST.get('login_name')
    get_password=request.POST.get('login_pass')
    if_user=user_register.objects.filter(user_email=get_email,password=get_password)
    u=len(if_user)
    if u>0:
        request.session['email']=get_email
        return redirect('index')
    else:
        return render(request,'login.html',{'e':1})   
   return render(request,'login.html')   


def head_foot(request):
      return render(request,'head_foot.html')
       
def register(request):
 if request.POST.get('user_email') not  in list(user_register.objects.filter(user_email=request.POST.get('user_email'))):
    if request.method=='POST':
       user=user_register()
       pw=request.POST.get('pas')
       cp=request.POST.get('con_pass')
       if pw == cp:
        user.fname=request.POST.get('fname')
        user.lname=request.POST.get('lname')
        user.user_email=request.POST.get('user_email')
        user.password=request.POST.get('pas')
        #user.confirm_password=request.POST.get('con_pass')
        user.save()
        return render(request,'register.html',{'m1':1})
       else:
        return render(request,'register.html',{'m1':2})
    else:
       return render(request, 'register.html')
 else:
    return render(request,'register.html',{'m1':3})      
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def changepass(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    all_entities=entitie.objects.all()       
    if request.method=='POST':
        user=user_register.objects.get(user_email=request.session['email'])
        old_password=request.POST.get('old_pass')
        new_password=request.POST.get('new_pass')
        confirm_password=request.POST.get('confirm_pass')
        print(user.password)
        if user.password == old_password: 
           if new_password==confirm_password:
              user.password=new_password
              user.save()
              return render(request,'change_password.html',{'created':1,'datasets':all_entities})
           else:
              return render(request,'change_password.html',{'created':2,'datasets':all_entities})
        else:
             return render(request,'change_password.html',{'created':3,'datasets':all_entities})
    else:
        return render(request,'change_password.html',{'datasets':all_entities})
             
def forgetpass(request):
    if request.method=='POST':
        em=request.POST.get('email')
        user=user_register.objects.get(user_email=em)
        if user.user_email==em:
            pw=user.password
            sub='your new password'
            mess='your password is '+ pw
            emailfr=settings.EMAIL_HOST_USER
            recipientls=[em,]
            send_mail(subject=sub,message=mess,from_email=emailfr,recipient_list=recipientls,auth_password=settings.EAMIL_HOST_PASSWORD)
            
            return render(request,'forget_password.html',{'res':'your password has been sent to your respective email account'})
        else:
            return render(request,'forget_password.html',{'res':'Invalid email'})
    else:
        return render(request,'forget_password.html')    



def faqs(request):
    res=faq.objects.all()
    
    return render(request,'faqs.html',{'data':res})  
def allblogs(request):
    res=blog.objects.all()
    return render(request,'blogs.html',{'data':res})
    
def h_support(request):
    if not request.session.has_key('email'):
        return redirect('login')
    user=user_register.objects.get(user_email=request.session['email'])
    user_help=help_support()
    if request.method=='POST':
         user_help.user_name=user.fname + user.lname
         user_help.help_heading=request.POST.get('heading')
         user_help.help_description=request.POST.get('description')
         user_help.save()
         return render(request,'help.html',{'msg':'query sent'})
    else:
         return render(request,'help.html',{})


def contactus(request):
    con=contact()
    if request.method=='POST':
     con.name=request.POST.get('name')
     con.email=request.POST.get('email')
     con.subject=request.POST.get('subject')
     con.message=request.POST.get('message')
     con.save()
     return render(request,'contactus.html',{'flag':1})
    else:
      return render(request,'contactus.html',{})
   
def blogdetail(request,id):
    res=blog.objects.get(id=id)

    return render(request,'blogdetails.html',{'data':res})

def oz_perdiction(request):
    return render(request,'ozone_perdiction.html')
def showcause(request):
    causes_cat=causes_category.objects.all()
    for causes in causes_cat:
         if causes.category_name=='green house gases':
                   gases=cause.objects.filter(cat=causes.id)
         if causes.category_name=='human roles':
                   hroles=cause.objects.filter(cat=causes.id)
         if causes.category_name=='global warming':
                   gw=cause.objects.filter(cat=causes.id)
                                 
    gases=[i for i in gases if i.title != 'water vapour']
    w=[i for i in gases if i.title =='water vapours'] 
    print(hroles)
    print(gw)
    return render(request,'causes.html',{'gas':gases,'w':w[0],'hroles':hroles,'gw':gw,'reviews':review.objects.all()})
def showeffects(request):
        effects=effect.objects.all()
        disasters=disaster.objects.all()
        return render(request,'effects.html',{'effect':effects,'disaster':disasters,'reviews':review.objects.all()})
def showeactions(request):
        actions=action.objects.all() 
        return render(request,'actions.html',{'action':actions,'reviews':review.objects.all()})
def showevidence(request):
        evidences=evidence.objects.all()
        return render(request,'evidence.html',{'evidence':evidences,'reviews':review.objects.all()})        
def showngos(request):
        ngos=ngo.objects.all()
        return render(request,'ngos.html',{'ngo':ngos})
   
def ngodescription(request,id):
    res=ngo.objects.get(id=id)
    return render(request,'ngodescription.html',{'data':res})

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, f'datasets/{path}')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404  
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def showdataset(request,id):
    if not request.session.has_key('email'):
        return redirect('index')
    ds=dataset.objects.get(entity_id=id)
    ds_columns=ds.columns_names.split(',')
    col_des=ds.columns_description.split(',')
    ds_col_des=zip(ds_columns,col_des)
    all_entities=entitie.objects.all()  
    return render(request,'dataset.html',{'data':ds,'datasets':all_entities,'ds_col_des':ds_col_des})    

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def showvisuals(request,id):
    if not request.session.has_key('email'):
        return redirect('index')
    ds=visuals.objects.filter(entity_id=id)
    all_entities=entitie.objects.all()  
    return render(request,'visualization.html',{'data':ds,'datasets':all_entities})  
@cache_control(no_cache=True, must_revalidate=True,no_store=True) 
def showperdictions(request,id):
    if not request.session.has_key('email'):
        return redirect('index')
    ds=perdiction.objects.filter(entity_id=id)
    all_entities=entitie.objects.all()  
    return render(request,'perdiction.html',{'data':ds,'datasets':all_entities})   
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def all_visualization(request,l):
    # try:
       all_entities=entitie.objects.all()
       print(l)         
       if l=='top_consumption_countries':
         
           if request.method == 'POST':
                 graphic=functions.top_ozone(request)

                 return render(request,'vizs/top_consumption_countries.html',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'years':countries_years.year_dic['ozoneyears']})
           if request.method=='GET':
                 return render(request,'vizs/top_consumption_countries.html',{'datasets':all_entities,'years':countries_years.year_dic['ozoneyears']})
           else:
                raise Http404
     
                   
       elif l=='ozone_cmp_countries_year_range':
            if request.method == 'POST':
                 graphic=functions.ozone_comparisons(request)
                 return render(request,'vizs/ozone_cmp_countries_year_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'countries':countries_years.countries_dic['ozonecountries'],'years':countries_years.year_dic['ozoneyears']})    
            if request.method =='GET':
                 return render(request,'vizs/ozone_cmp_countries_year_range.html',{'datasets':all_entities,'countries':countries_years.countries_dic['ozonecountries'],'years':countries_years.year_dic['ozoneyears']})    
       elif l== 'least_consumption_country':
            if request.method=='POST':
                graphic=functions.least_ozone(request)
                
                return render(request,'vizs/least_consumption_country.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['ozoneyears']})    
            if request.method =='GET':
                 return render(request,'vizs/least_consumption_country.html',{'datasets':all_entities,'years':countries_years.year_dic['ozoneyears']})    
                     
       elif l== 'ozone_cmp_year':
            if request.method=='POST':
                graphic=functions.ozone_yearly(request)
                return render(request,'vizs/ozone_cmp_year.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['ozoneyears']})    
            if request.method =='GET':
                 return render(request,'vizs/ozone_cmp_year.html',{'datasets':all_entities,'years':countries_years.year_dic['ozoneyears']})         
       elif l== 'land_temp_cmp_year_range':
            if request.method=='POST':
                graphic=functions.land_temp_yearly(request)
                if graphic==None:
                   return render(request,'vizs/land_temp_cmp_year_range.html',{'datasets':all_entities,'ns':1,'years':countries_years.year_dic['land_temperature_years']})    
                else:
                   return render(request,'vizs/land_temp_cmp_year_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['land_temperature_years']})    
            if request.method =='GET':
                 return render(request,'vizs/land_temp_cmp_year_range.html',{'datasets':all_entities,'years':countries_years.year_dic['land_temperature_years']})       
       
       elif l== 'air_deaths_diff_gases_allyears':
            if request.method=='GET':
                graphic=functions.all_gases_cmp(request)
                return render(request,'vizs/air_deaths_diff_gases_allyears.html',{'datasets':all_entities,'graphic':graphic.decode('utf8')})    
           
       elif l== 'air_deaths_country_one_year':
            if request.method=='POST':
                graphic=functions.country_year_deaths(request)
                return render(request,'vizs/air_deaths_country_one_year.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['air_pollution_years'],'countries':countries_years.countries_dic['air_pollution_countries']})    
            if request.method=='GET':
                return render(request,'vizs/air_deaths_country_one_year.html',{'datasets':all_entities,'years':countries_years.year_dic['air_pollution_years'],'countries':countries_years.countries_dic['air_pollution_countries']})    
           
       elif l== 'air_max_min_deaths_top_country_oneyear':
            if request.method=='POST':
                graphic=functions.air_max_min_death_top_country(request)
                return render(request,'vizs/air_max_min_deaths_top_country_oneyear.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['air_pollution_years']})    
            if request.method=='GET':
                return render(request,'vizs/air_max_min_deaths_top_country_oneyear.html',{'datasets':all_entities,'years':countries_years.year_dic['air_pollution_years']})    
       elif l== 'air_deaths_cmp_differentcause_country_year_range':
            if request.method=='POST':
                graphic=functions.deaths_onecountry_year_cause(request)
                return render(request,'vizs/air_deaths_cmp_differentcause_country_year_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['air_pollution_years'],'countries':countries_years.countries_dic['air_pollution_countries']})    
            if request.method=='GET':
                return render(request,'vizs/air_deaths_cmp_differentcause_country_year_range.html',{'datasets':all_entities,'years':countries_years.year_dic['air_pollution_years'],'countries':countries_years.countries_dic['air_pollution_countries']})    
       elif l== 'air_deaths_countries_deaths_cmp_year_range':
            if request.method=='POST':
                graphic=functions.deaths_countries_year_cause(request)
                return render(request,'vizs/air_deaths_countries_deaths_cmp_year_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'years':countries_years.year_dic['air_pollution_years'],'countries':countries_years.countries_dic['air_pollution_countries']})    
            if request.method=='GET':
                return render(request,'vizs/air_deaths_countries_deaths_cmp_year_range.html',{'datasets':all_entities,'years':countries_years.year_dic['air_pollution_years'],'countries':countries_years.countries_dic['air_pollution_countries']})          
       elif l== 'air_max_deaths_cause_or_country':
            if request.method=='GET':
                graphic=functions.air_max_deaths_cause_or_cn(request)
                return render(request,'vizs/air_max_deaths_cause_or_country.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'countries':countries_years.countries_dic['air_pollution_countries']})    
            if request.method=='POST':
                graphic=functions.air_max_deaths_cause_or_cn(request)
                return render(request,'vizs/air_max_deaths_cause_or_country.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'countries':countries_years.countries_dic['air_pollution_countries']})                   
       elif l== 'water_deaths_country_allyears_range':
            if request.method=='GET':
                graphic=functions.water_deaths_all_years_range_country(request)
                return render(request,'vizs/water_deaths_country_allyears_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'countries':countries_years.countries_dic['unsafe_water'],'years':countries_years.year_dic['unsafe_water']})  
            if request.method=='POST':
                graphic=functions.water_deaths_all_years_range_country(request)
                return render(request,'vizs/water_deaths_country_allyears_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'countries':countries_years.countries_dic['unsafe_water'],'years':countries_years.year_dic['unsafe_water']})                   
       
       elif l== 'water_deaths_cmp_countries_year_range':
            if request.method=='GET':
                return render(request,'vizs/water_deaths_cmp_countries_year_range.html',{'datasets':all_entities,'countries':countries_years.countries_dic['unsafe_water'],'years':countries_years.year_dic['unsafe_water']})  
            if request.method=='POST':
                graphic=functions.water_deaths_cmp_countries_range(request)
                return render(request,'vizs/water_deaths_cmp_countries_year_range.html',{'datasets':all_entities,'graphic':graphic.decode('utf8'),'countries':countries_years.countries_dic['unsafe_water'],'years':countries_years.year_dic['unsafe_water']})                   
       elif l=='co2_analysis_range':
            if request.method=='GET':
                functions.co2_graph(request)
                return render(request,'vizs/co2_analysis.html',{'datasets':all_entities})  
            
       elif l=='methane_analysis_range':
            if request.method=='GET':
                functions.methane_graph(request)
                return render(request,'vizs/methane_analysis.html',{'datasets':all_entities})  
       elif l=='no2_analysis_range':
            if request.method=='GET':
                functions.no2_graph(request)
                return render(request,'vizs/no2_analysis.html',{'datasets':all_entities})       
                
       else:
           return HttpResponse('under construction')
              
    # except :
    #     return redirect('login')            
def all_perdictions(request,l):
    
       all_entities=entitie.objects.all()
       print(l)         
       if l=='oz_cn_per':
           if request.method == 'POST':
                  graphic=per_functions.ozone_per(request)
                  return render(request,'pers/ozone_per',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'countries':countries_years.countries_dic['ozonecountries']})
           if request.method=='GET':
                 return render(request,'pers/ozone_per',{'datasets':all_entities,'countries':countries_years.countries_dic['ozonecountries']})
           
       elif l=='air_pol_per':
           if request.method == 'POST':
                  graphic=per_functions.air_pol_per(request)
                  return render(request,'pers/air_pol_per',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'countries':countries_years.countries_dic['air_pollution_countries']})
           if request.method=='GET':
              
                 return render(request,'pers/air_pol_per',{'datasets':all_entities,'countries':countries_years.countries_dic['air_pollution_countries']})
           
       elif l=='nt_em_per':
           if request.method == 'POST':
                  graphic=per_functions.nt_em_per(request)
                  return render(request,'pers/nt_em_per',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'countries':countries_years.countries_dic['nitrous_dioxide']})
           if request.method=='GET':
              
                 return render(request,'pers/nt_em_per',{'datasets':all_entities,'countries':countries_years.countries_dic['nitrous_dioxide']})
           
            
       elif l=='mth_em_per':
           if request.method == 'POST':
                  graphic=per_functions.mth_em_per(request)
                  return render(request,'pers/mth_em_per',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'countries':countries_years.countries_dic['methane']})
           if request.method=='GET':
              
                 return render(request,'pers/mth_em_per',{'datasets':all_entities,'countries':countries_years.countries_dic['methane']})

       elif l=='co2_em_per':
           if request.method == 'POST':
                  graphic=per_functions.co2_em_per(request)
                  return render(request,'pers/co2_em_per',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'countries':countries_years.countries_dic['co2_countries']})
           if request.method=='GET':
              
                 return render(request,'pers/co2_em_per',{'datasets':all_entities,'countries':countries_years.countries_dic['co2_countries']})
       elif l=='gb_eth_per':
           if request.method == 'POST':
                  graphic=per_functions.gb_eth_per(request)
                  return render(request,'pers/gb_eth_per',{'datasets':all_entities,'graphic': graphic.decode('utf8')})
           if request.method=='GET':
              
                 return render(request,'pers/gb_eth_per',{'datasets':all_entities})     
       elif l=='un_wt_per':
           if request.method == 'POST':
                  graphic=per_functions.un_wt_per(request)
                  return render(request,'pers/un_wt_per',{'datasets':all_entities,'graphic': graphic.decode('utf8'),'countries':countries_years.countries_dic['unsafe_water']})
           if request.method=='GET':
              
                 return render(request,'pers/un_wt_per',{'datasets':all_entities,'countries':countries_years.countries_dic['unsafe_water']})                           
           else:
                raise Http404  
    # except:
    #     return redirect('login')                      

             
