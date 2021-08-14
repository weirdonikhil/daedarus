from message.getMessage import getmessages
from BlinkskyAPI.sendReward import SendReward
from users.Rewards import  GetRewardDetails
from projects.rate_task import rateProject
from message.sendMessage import sendmessage
from projects.submitIdea import submit_idea
from projects.submitTask import submit_task
from users.GetEmployeeFromCompany import CompanyEmployees
from projects.idea_submission_details import business_idea
from projects.task_submission_details import submission_details
from projects.add_task import Create_task
from projects.projectDetails import project_details
from flask import Flask, render_template, request, redirect, session
from Authorization.registeration import register_user
from Authorization.login import employee_login
from Authorization.resetPassword import reset_password
from FirebaseCredentials.Firebase import auth,db
from projects.addProject import CreateProject

app = Flask(__name__)

app.secret_key="thisisblinkathonhackathon"


@app.route("/")
def Landing():
    return render_template("landing.html")

@app.route("/dashboard")
def index():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_status=db.child("Users").child(employee_id).child("profile/status").get().val()
              user_id=employee_id
        if (user_status=="admin"):
            if db.child("Users").child(user_id).child("messages").get().val() is not None:
              msgss=getmessages(user_id)
              return render_template("index.html", name = user_name,msgss=msgss,msg=True)
            else:
              return render_template("index.html", name = user_name)  
        else :
         return render_template("index_member.html", name=user_name)
    except KeyError:
        return redirect("/login")

@app.route("/registeration",methods=["GET","POST"])
def registeration():
    if request.method=="POST":
            email=request.form["email"]
            password=request.form["password"]
            employeeCode=request.form["employee_code"]
            mobile=request.form["mobile"]
            employee_company=request.form["employee_company"]
            employee_name=request.form["employee_name"]
            admin=request.form["admin"]
            print(admin)
            register_user(email,password,employeeCode,mobile,employee_company,employee_name,admin)
            return redirect("/dashboard")
    return render_template("Registeration.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        try:
            email=request.form["email"]
            password=request.form["password"]
            employee_login(email,password)
            user=auth.sign_in_with_email_and_password(email,password)
            user = auth.refresh(user['refreshToken'])
            user_id = user['idToken']
            session['usr'] = user_id
            all_users = db.child("Users").get()
            for user in all_users.each():
             employee_id=user.key()
             path="Users/"+employee_id+"/profile/email"
             user_email=db.child(path).get().val()
             if (user_email==email) :
              db.child("Users").child(employee_id).child("session").update({"session_id":session['usr']})
            return redirect("/dashboard")
        except:
            err_msg="Wrong Credentials!"
            return render_template("Login.html",sweetalert=True,err_msg=err_msg)
    return render_template("Login.html")

@app.route("/forgot-password",methods=["GET","POST"])
def forgot_password():
    if request.method=="POST":
        try:
            email=request.form["email"]
            reset_password(email)
        except:
            err_msg="Email was not found linked with any user"
            return render_template("forgot-password.html", sweetalert=True, err_msg=err_msg)
    return render_template("forgot-password.html")

@app.route("/add-project",methods=["GET","POST"])
def add_project():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_company=db.child("Users").child(employee_id).child("profile/company").get().val()
              user_id=employee_id
        employees=CompanyEmployees(user_company)
        if request.method=="POST":
            project_name=request.form["project_name"]
            project_id=request.form["project_id"]
            project_members=request.form["members"]
            project_description=request.form["project_description"]
            CreateProject(project_name,project_id,project_members,project_description,user_id)
        return render_template("add_project.html", name = user_name,employees=employees)
    except KeyError:
        return redirect("/login")


@app.route("/add-task",methods=["GET","POST"])
def add_task():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if request.method=="POST":
            task_name=request.form["task_name"]
            task_id=request.form["task_id"]
            task_project_id=request.form["task_project_id"]
            task_description=request.form["task_description"]
            Create_task(task_name,task_id,task_project_id,task_description,user_id)
        return render_template("add_task.html", name = user_name)
    except KeyError:
        return redirect("/login")

@app.route("/projects")
def projects():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id 
        if db.child("Users/"+user_id+"/Projects").get().val() is not None:
         projects_info=project_details(user_id)
         return render_template("projects.html",name=user_name,projects=projects_info)
        else:
         return render_template("projects.html",name=user_name,message="No Running Projects were found")
    except KeyError:
        return redirect("/login")

@app.route("/check-idea")
def check_idea():
    return render_template("check_idea.html")

@app.route("/idea_submissions")
def idea_submissions():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if db.child("Users/"+user_id+"/ideaSubmission").get().val() is not None:
         idea_details=business_idea(user_id)
         return render_template("idea_submissions.html",name=user_name,ideas=idea_details)
        else:
          return render_template("idea_submissions.html",name=user_name,message="No Business Ideas Found")
    except KeyError:
        return redirect("/login")

@app.route("/submissions")
def submissions():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if db.child("Users/"+user_id+"/task_submissions").get().val() is not None:
         task_details=submission_details(user_id)
         return render_template("submissions.html",name=user_name,tasks=task_details)
        else:
         return render_template("submissions.html",message="No Submissions Found")
    except KeyError:
        return redirect("/login")


@app.route("/reward-history")
def reward_history():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if db.child("Users/"+user_id+"/rewards").get().val() is not None:
         reward=GetRewardDetails(user_id)
         return render_template("history.html",name=user_name,rewards=reward)
        else:
         return render_template("history.html",name=user_name,message="No Gift Cards has been issued")
    except KeyError:
        return redirect("/login")


@app.route("/rate-submissions",methods=["GET","POST"])
def rate_submissions():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if request.method=="POST":
            rating=request.form["rating"]
            emp_id=request.form["employee_id"]
            task_id=request.form["task_id"]
            rateProject(rating,emp_id,task_id,user_id)
            return redirect("/submissions")
        return render_template("rate_project.html",name=user_name)
    except KeyError:
        return redirect("/login")


@app.route("/give-reward",methods=["GET","POST"])
def give_reward():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        adminPhone=db.child("Users").child(user_id).child("profile/mobile").get().val()
        company=db.child("Users").child(user_id).child("profile/company").get().val()
        if request.method=="POST":
            emp_id=request.form["employee_id"]
            emp_phone=db.child("Users").child(emp_id).child("profile/mobile").get().val()
            emp_name=db.child("Users").child(emp_id).child("profile/name").get().val()
            gift_card_value=request.form["reward_value"]
            link=SendReward(company,adminPhone,emp_phone,gift_card_value,emp_id,emp_name,user_id)
            return render_template("reward_submissions.html",name=user_name,sweetalert=True,link=link)
        return render_template("reward_submissions.html",name=user_name)
    except KeyError:
        return redirect("/login")
    
#admin_pages

############################################

# members_pages

@app.route("/dashboard-member")
def member_dashboard():
    return render_template("index_member.html")

@app.route("/member-projects")
def memberProjects():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id 
        if db.child("Users/"+user_id+"/Projects").get().val() is not None:
         projects_info=project_details(user_id)
         return render_template("member_projects.html",name=user_name,projects=projects_info)
        else:
          return render_template("member_projects.html",name=user_name,message="No Running Projects were found")
    except KeyError:
        return redirect("/login")

@app.route("/tasks",methods=["GET","POST"])
def tasks():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if  db.child("Users").child(user_id).child("task_submissions").get().val() is None:
         if request.method=="POST":
           task_name=request.form["task_name"]
           task_id=request.form["task_id"]
           project_name=request.form["project_name"]
           project_id=request.form["project_id"]
           submit_task(project_name,project_id,task_name,task_id,user_id)
           return redirect("/exercise-portal")
         return render_template("member_tasks.html",name=user_name,message="No Submissions found till now")
        else:
         task_details=submission_details(user_id)
         if request.method=="POST":
           task_name=request.form["task_name"]
           task_id=request.form["task_id"]
           project_name=request.form["project_name"]
           project_id=request.form["project_id"]
           submit_task(project_name,project_id,task_name,task_id,user_id)
           return redirect("/exercise-portal")
         return render_template("member_tasks.html", name=user_name,tasks=task_details)
    except KeyError:
        return redirect("/login")

@app.route("/idea",methods=["GET","POST"])
def idea():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if request.method=="POST":
            idea_tagline=request.form["idea_tagline"]
            description=request.form["description"]
            business_model=request.form["business_model"]
            business_model_link=request.form["business_model_link"]
            submit_idea(user_id,idea_tagline,business_model_link,business_model,description)
        return render_template("member_submit_idea.html",name=user_name)
    except KeyError:
        return redirect("/login")


@app.route("/send-message",methods=["GET","POST"])
def send_message():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if request.method=="POST":
            admin_email=request.form["admin_email"]
            gift_card_value=request.form["gift_card_value"]
            description=request.form["msg_description"]
            sendmessage(description,gift_card_value,admin_email,user_id)
            return render_template("send_message.html",name=user_name,sweetalert=True)
        return render_template("send_message.html",name=user_name)
    except KeyError:
        return redirect("/login")

@app.route("/member-reward-history")
def member_reward_history():
    try:
        session['usr']
        all_users = db.child("Users").get()
        for user in all_users.each():
            employee_id=user.key()
            path="Users/"+employee_id+"/session/session_id"
            customer_session=db.child(path).get().val()
            if (customer_session==session['usr']) :
              user_name=db.child("Users").child(employee_id).child("profile/name").get().val()
              user_id=employee_id
        if db.child("Users/"+user_id+"/Projects").get().val() is not None:
         reward=GetRewardDetails(user_id)
         return render_template("member_reward_history.html",name=user_name,rewards=reward)
        else:
         return render_template("member_reward_history.html",name=user_name,message="No Rewards Issued till Now")
    except KeyError:
        return redirect("/login")

#######################
@app.route("/exercise-portal")
def exercise():
    return render_template("yoga_OpenCV.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")






















