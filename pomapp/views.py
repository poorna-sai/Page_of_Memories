from django.shortcuts import render , redirect ,get_object_or_404
from .models import *

from django.core.paginator import Paginator , EmptyPage  
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .forms import postform

# userr forget password

# Create your views here.

#Register User
def Register(request):
	if request.method=='POST':
		profilepic = request.FILES.get('profilepic')
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 =request.POST['password2']
		if password1==password2:
			if User.objects.filter(username = username).exists():
				messages.info(request , "Username already taken")
				return redirect('Register')
			elif User.objects.filter(email = email).exists():
				messages.info(request,"email already exist")
				return redirect('Register')
			else:
				user = User.objects.create_user(username = username , email=email , password=password1 )
				usermodel = UserModel(profilepic = profilepic , username =username , email=email)
				usermodel.save()
				user.save()
				return redirect('Addpost')
	return render(request , 'index.html')

#login view.....
def Login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password1']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request , user)
			return redirect('viewpost')
		else:
			messages.success(request, ('invalid credentials problem in login'))
			return redirect('login')
	return render(request,'login.html')

# Logout view... 
def logout(request):
	auth.logout(request)
	return redirect('login')
def home(request):
	form = postform
	
	return render(request , 'post.html')


# ADD POST VIEW TO ADD POST USING POST METHOD 
def Addpost(request):
	if request.user.is_authenticated:

		if request.method == 'POST':
			if "Submit" in request.POST:

				username = request.POST.get('username')
				description = request.POST.get('description')
				data = Posts(username = username , description= description)
				data.save()
				return redirect('home')
			else:
				username = request.POST.get('username')
				description = request.POST.get('description')
				data = PrivateDairy(username = username , description= description)
				data.save()
				return redirect('home')
		else:
			return redirect('home')
	else:
		return redirect("login")

# VIEW TO VIEW ALL POSTS GET METHOD USED HERE .......
def viewpost(request):
	if request.user.is_authenticated:
		vobj = Posts.objects.all()
		p = Paginator(vobj , 2 )
		page_num = request.GET.get('page' ,1)
		page = p.page(page_num)
		try:
			page = p.page(page_num)
		except EmptyPage:
			page = p.page(1)
		data ={
			'databasekey' : page
		}
		return render(request , 'viewpost.html' , data)
	else:
		return redirect("login")

 
 #VIEW FOR UPDATE THE POST BY USING PUT OR UPDDATE METHOD .......
def updatepost(request , id):
	if request.user.is_authenticated:

		if request.method == 'POST':
			username = request.POST.get('username')
			description = request.POST.get('description')
			data = Posts(id = id ,username = username , description= description)
			data.save()
			return redirect('viewpost')
		
		uobj = Posts.objects.get(id = id)
		context = {
		 'databasekey':uobj
		}
		return render(request , 'updatepost.html' , context)
	else:
		return redirect("login")


# VIEW FOR DISPLAY USER PROFILE USING GET METHOD ......
def profile(request):
	if request.user.is_authenticated:
		user = request.user.email
		stdobj = UserModel.objects.filter(email = user)
		data={
			'data':stdobj,
		}
		return render(request , 'profile.html' , data)
	else:
		return redirect('login')
	return render(request , 'profile.html')

#VIEW FOR EDIT THE EXESTING POST POSTED BY THE SAME USER .....
def editpost(request):
	if request.user.is_authenticated:
		user = request.user.username
		
		vobj = Posts.objects.filter(username = user)
		data ={
			'data' : vobj
		}
		
	return render(request , 'editpost.html' ,data)

#VIEW FOR DELETE THE EXISTING POST POSTED BY THE SAME USER ... USING DELETE METHOD . . .
def Deletepost(request , id):
	if request.user.is_authenticated:
		dele = Posts.objects.filter(id = id)
		dele.delete()
		return redirect('viewpost')


#ABOUT US PAGE DISPLAY THE DEVELOPER DETAILS ... .. 
def Aboutus(request):
	return render(request , 'aboutus.html')

# VIEW FOR CHANGE THE PASSWORD FOR THE EXISTING USER BY USING TOKEN AUTHENTICATION ... 
def ChangePassword(request , token):
    context = {}
 
    try:
        profile_obj = UserModel.objects.filter(forget_password_token = token).first()
        user_name = profile_obj.username
        print(f"forgotten username ==={user_name}")
        #context = {'user_name' : profile_obj.username}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            
            
            if user_name is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(username = user_name)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)

# VIEW FOR GENERATE AND RESET PASSWORD ....
import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= UserModel.objects.get(username = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')


# VIEW AND LIBRARIES FOR SENDING REST PASSWORD ....
from email.message import EmailMessage
import ssl
import smtplib


def send_forget_password_mail(email , token):
	lemail = ""
	lemail = email
	token = token
	email_sender = 'poorna143pilla@gmail.com'
	email_password = 'miuxfsxjfbxrwlak'


	email_reciver = lemail


	subject = "Reset Password Page of memories"
	body = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
	
	em = EmailMessage()
	em['From'] = email_sender
	em['To'] = email_reciver
	em['subject'] = subject
	em.set_content(body)


	context = ssl.create_default_context()

	with smtplib.SMTP_SSL('smtp.gmail.com' , 465 , context = context) as smtp:
	    smtp.login(email_sender , email_password)
	    smtp.sendmail(email_sender , email_reciver , em.as_string())






# pdf printing view .. 

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_pdf_view(request):
	if request.user.is_authenticated:

	    template_path = 'printpdf.html'
	    data=Posts.objects.all()
	    context = {'data': data}
	    # Create a Django response object, and specify content_type as pdf
	    response = HttpResponse(content_type='application/pdf')
	    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	    response['Content-Disposition'] = 'filename="report.pdf"'
	    # find the template and render it.
	    template = get_template(template_path)
	    html = template.render(context)

	    # create a pdf
	    pisa_status = pisa.CreatePDF(
	       html, dest=response)
	    # if error then show some funny view
	    if pisa_status.err:
	       return HttpResponse('We had some errors <pre>' + html + '</pre>')
	    return response
	else:
		return redirect("login")



def View_Persnol_Dairy(request):
	if request.user.is_authenticated:
		username = request.user.username
		vobj = PrivateDairy.objects.filter(username = username)
		p = Paginator(vobj , 2 )
		page_num = request.GET.get('page' ,1)
		page = p.page(page_num)
		try:
			page = p.page(page_num)
		except EmptyPage:
			page = p.page(1)
		data ={
			'databasekey' : page
		}
		return render(request , 'dairy.html' , data)
	else:
		return redirect("login")
