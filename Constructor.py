#Name: Ariel
#Date: 22/10
#Comments: all class created

####################
#Importing modules
####################



####################
# Consructors
####################

import email


class Candidate:
    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email


class Interviewer:
    def __init__(self,employee_ID,firstName,last_name,email,phoneNum, planned_interview,availabilities,created_job_Postings):
        self.employee_ID = employee_ID
        self.firstName = firstName
        self.last_name = last_name
        self.email = email
        self.phoneNum = phoneNum
        self.planned_interview = planned_interview
        self.availabilities = availabilities
        self.created_job_Postings = created_job_Postings

class Job_Posting:
    def __init__(self, post_ID, title, description, num_of_jobOffers, interviewer, application_Forms):
        self.post_ID = post_ID
        self.title = title
        self.description = description
        self.num_of_jobOffers = num_of_jobOffers
        self.interviewer = interviewer
        self.application_Forms = application_Forms

class application_Forms:
    def __init__(self, app_ID, candidate, jobPosting, CV):
        self.app_ID = app_ID
        self.candidate = candidate
        self.jobPosting = jobPosting
        self.CV = CV

class Candidate:
    def __init__(self,candidate_ID,firstName,lastName,dateOfBirth, email, phoneNum, applicationForm, tentative_appointment, interview, is_archived):
        self.candidate_ID = candidate_ID
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phoneNum = phoneNum
        self.applicationForm = applicationForm
        self.tentative_appointment = tentative_appointment
        self.interview = interview
        self.is_archived = is_archived

class Trainee(Candidate):
    def __init__(self,trainee_ID,start_date):
        self.trainee_ID = trainee_ID
        self.start_date = start_date

class Interview:
    def __init__(self,Interview_ID,candidate,interviewer,timeslot,interview_Results):
        self.Interview_ID = Interview_ID
        self.candidate = candidate
        self.interviewer = interviewer
        self.timeslot = timeslot
        self.interview_Results = interview_Results

class TimeSlot:
    def __init__(self, interviewer,candidate,interview,date_time):
        self.interviewer = interviewer
        self.candidate = candidate
        self.interview = interview
        self.date_time = date_time


####################
# Main
####################


user = Interviewer("011",'Ariel','Piotraut','ariel@gmail','060606','10 sept, 11 sept','Week of 13th','Job1, Job2')
print(user.employee_ID, user.firstName, user.last_name, user.email, user.phoneNum, user.planned_interview, user.availabilities, user.created_job_Postings)
print(user)

jobPost = Job_Posting('01', 'BARISTA', 'being the barista', '5', user.last_name, 'created') 
print(jobPost)
print(jobPost.ID, jobPost.title, jobPost.description, jobPost.num_of_jobOffers, jobPost.interviewer, jobPost.application_Forms)



############################
# FUNCTIONS
############################

def is_available(Candidate, Interviewer):
    interview = Interview(Interview_ID, Candidate, Interviewer, Candidate.tentative_appointment, 0)    
    return interview 

def send_timeSlots(self, Candidate,TimeSlot):
    self.Candidate.tentative_appointments.append([TimeSlot])

def inform(Interview, Candidate):
    if Interview.interview_Result == True: 
        Candidate.is_archived = False
    else: 
        Candidate.is_archived = True