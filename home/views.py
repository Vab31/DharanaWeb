import email
from io import StringIO
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,reverse
from home.models import interactionrating, review
from home.models import rating,qualityrating
from home.models import languagerating
from home.models import Info
from home.models import pageinfo
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

token=0;
def searchMatch(query, item):
    if query in item.title.lower() or query in item.content1.lower()  or query in item.content2.lower():
        return True
    else:
        return False

def search(request):
    allProds = []
    
    query=request.GET.get('search');
    print(query);
    list= pageinfo.objects.all( )
    prod=[item for item in list if searchMatch(query, item)]
    print(len(prod))
    
    if len(prod)!= 0:
        params = {'prod': prod, "msg":""}
    #         allProds.append([prod])
    # params = {'allProds': allProds, "msg":""}
    if  len(query)<4 or len(prod)==0 :
        params={'msg':"Please make sure to enter relevant search query"}

    return render(request, 'search.html', params)



def index(request):
   list= reversed (pageinfo.objects.all( )[:5]);
#    email=request.email;
#    print(email);

   return render(request,'index.html',{'list':list})


def page(request,title_name):
    global token
    
    token=title_name;
    
    

    information=pageinfo.objects.filter(title = title_name)[0];

    if request.method=='POST':
        comment=request.POST.get('comment');
        username=request.user
        print(username);
        type=title_name;
        print(comment);
        if comment != None:
         collect=review(comment=comment, type=type, username=username);
         collect.save();
    val=reversed( review.objects.filter(type=title_name));

   
  
    intial_value,intial_value_for_languge,intial_value_for_interaction,intial_value_of_quality=0,0,0,0;
    user_rating,user_rating_for_interaction,user_rating_for_language,user_rating_for_quality=0,0,0,0;
    username=request.user;
   
    
    
    # print(username)

    if request.user.is_authenticated:
        
        user_rating=rating.objects.filter(type=title_name).filter(email=email).values('rate');
        user_rating_for_interaction=interactionrating.objects.filter(type=title_name).filter(email=email).values('rate');
        user_rating_for_quality=qualityrating.objects.filter(type=title_name).filter(email=email).values('rate');
        user_rating_for_language= languagerating.objects.filter(type=title_name).filter(email=email).values('rate');
        
        
    
      

   
    
    #   for depthofthecourse
    if request.method=='POST':
        value=request.POST.get('btnradio');
        username=request.user;
        email=username.email;
        print(value, username,)
        
        
        type=title_name;
        if user_rating.count()== 0:
          if value != None:
            collect=rating(rate=value,type=type ,email=email);
            collect.save();
        elif user_rating.count()==1:
            if value != None:
             rating.objects.filter(email=email).update(rate=value);
        else:
            print('noting happen')

    total_rating= rating.objects.filter(type=title_name)
    for rating_value in total_rating:
        intial_value=intial_value+rating_value.rate;

    if total_rating.count() != 0 :
     intial_value=intial_value/(total_rating.count())

    # rating_value=intial_value/(total_rating.count());


#for languageclarity
     

     if request.method=='POST':
        value=request.POST.get('btnradioforlanguge');
        username=request.user;
        email=username.email;
        print(value, username,)
        
     
        type=title_name;

        
        if user_rating_for_language.count()== 0:
          if value != None:
            collect=languagerating(rate=value,type=type ,email=email);
            collect.save();
        elif user_rating_for_language.count()==1:
            if value != None:
             languagerating.objects.filter(email=email).update(rate=value);
        else:
            print('noting happen')

    total_rating= languagerating.objects.filter(type=title_name)
    for rating_value in total_rating:
        
       intial_value_for_languge=intial_value_for_languge +rating_value.rate;

    if total_rating.count() != 0 :
     intial_value_for_languge=intial_value_for_languge/(total_rating.count())  

# =========================== interaction_rating==============================


     

     if request.method=='POST':
        value=request.POST.get('btnradioforinteraction');
        username=request.user;
        email=username.email;
        print(value, username,)
        
     
        

       
        type=title_name;
        if user_rating_for_interaction.count()== 0:
          if value != None:
            collect=interactionrating(rate=value,type=type ,email=email);
            collect.save();
        elif user_rating_for_interaction.count()==1:
            if value != None:
             interactionrating.objects.filter(username=username).update(rate=value);
        else:
            print('noting happen')

    total_rating= interactionrating.objects.filter(type=title_name)
    for rating_value in total_rating:
        
       intial_value_for_interaction=intial_value_for_interaction +rating_value.rate;

    if total_rating.count() != 0 :
     intial_value_for_interaction=intial_value_for_interaction/(total_rating.count()) 

# ===============================Quality of course================================== 
    
    if request.method=='POST':
        value=request.POST.get('studymaterial');
        username=request.user;
        email=username.email;
        print(value, username,)
        
     
        type=title_name;
        if user_rating_for_quality.count()== 0:
          if value != None:
            collect=qualityrating(rate=value,type=type ,email=email);
            collect.save();
        elif user_rating_for_quality.count()==1:
            if value != None:
             qualityrating.objects.filter(email=email).update(rate=value);
        else:
            print('noting happen')
          
    total_rating= qualityrating.objects.filter(type=title_name)
    for rating_value in total_rating:
        
       intial_value_of_quality=intial_value_of_quality +rating_value.rate;

    if total_rating.count() != 0 :
     intial_value_of_quality=intial_value_of_quality/(total_rating.count()) 

    if request.user.is_authenticated and user_rating.count()!=0:
        user_rating=user_rating[0]['rate'];
    else:
        user_rating=0;
    
    if request.user.is_authenticated and user_rating_for_quality.count()!=0:
        user_rating_for_quality=user_rating_for_quality[0]['rate'];
    else:
        user_rating_for_quality=0;
    
    if request.user.is_authenticated and user_rating_for_interaction.count()!=0:
        user_rating_for_interaction=user_rating_for_interaction[0]['rate'];
    else:
        user_rating_for_interaction=0;
    
    if request.user.is_authenticated and user_rating_for_language.count()!=0:
        user_rating_for_language=user_rating_for_language[0]['rate'];
    else:
        user_rating_for_language=0;
    



    return render(request,'reviewbody.html' ,{'val':val,'intial_value':intial_value, 'information':information,'token':token,
    'intial_value_for_languge':intial_value_for_languge,'intial_value_for_interaction':intial_value_for_interaction,
    'intial_value_of_quality':intial_value_of_quality,'user_rating':user_rating,'user_rating_for_interaction':user_rating_for_interaction,
    'user_rating_for_language':user_rating_for_language,'user_rating_for_quality':user_rating_for_quality})




# ===================sign up=================

def signup(request):
    if request.method=='POST':
        username= request.POST.get('uname');
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(username, email, password ,fname, lname)

        # create user================
        if(password==cpassword):
           myuser=User.objects.create_user(username,email,password);
           myuser.first_name=fname;
           myuser.last_name=lname;
           
           myuser.save()
           messages.success(request,'your account has been successfully created')
           if token == 0:
              messages.success(request,'your account has been successfully created');
              return redirect('home');
           else:
              messages.success(request,'your account has been successfully created');
              return HttpResponseRedirect(reverse('page', args=(token,)),)
        else:
           
            if token == 0:
               messages.error(request,'Password And Confirm Password are not same ')
               return redirect('home');
            else:
               messages.error(request,'Password And Confirm Password are not same ')
               return HttpResponseRedirect(reverse('page', args=(token,)),)
    return redirect('home')

# ===================Login==================

def handellogin(request):
    if request.method=='POST':
        user=request.POST.get('user');
        password=request.POST.get('passwd')
        user=authenticate(username=user, password=password);
        print(user,password)
        if user is not None:
            login(request, user)
            print('success')
            confirm=True;
            # url = reverse('page', kwargs={'token':token})
            # return HttpResponseRedirect(url)
            # return redirect('page')
            
            # ...
            messages.success(request, 'successfully loged in.')
            return HttpResponseRedirect(reverse('page', args=(token,)),{'confirm':confirm})

        else:
            print('incorrect');
            
            print (token)
            if token == 0:
              messages.warning(request, 'Log in failed. Incorrect Details')
              return redirect('home');
            else:
              messages.warning(request, 'Log in failed. Incorrect Details')
              return HttpResponseRedirect(reverse('page', args=(token,)),)

    return redirect('home')



def handellogout(request):
     logout(request);
     print('succes fully logout')

     if token != None:
       return HttpResponseRedirect(reverse('page', args=(token,)))
     else:
       return redirect('home') 
    #  url = reverse('page', arg=[786])
    #  return HttpResponseRedirect(url)


def  contact(request):
    success=False;

    if request.method=='POST':
       email=request.POST.get('email');
       comment=request.POST.get('comment');
       
       datasave=Info(email=email,comment=comment);
       datasave.save();
       success=True;
    return render(request,'contact.html',{'success':success,} )


def about(request):
    title='About us'
    return render(request, 'about.html', {'title':title,} )
    
