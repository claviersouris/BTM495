#Name: Ariel
#Date: 22/10
#Comments: all class created

####################
#Importing modules
####################



####################
# Consructors
####################

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
    def __init__(self, ID, title, description, num_of_jobOffers, interviewer, application_Forms):
        self.ID = ID
        self.title = title
        self.description = description
        self.num_of_jobOffers = num_of_jobOffers
        self.interviewer = interviewer
        self.application_Forms = application_Forms

class application_Forms:
    def __init__(self, ID, candidate, jobPosting,CV):
        self.ID = ID
        self.candidate = candidate
        self.jobPosting = jobPosting
        self.CV = CV

class Candidate:
    def __init__(self,candidate_ID,firstName,lastName,dateOfBirth,email,phoneNum,applicationForm,tentative_appointment,interview,is_archived):
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
    def __init_(self,trainee_ID,start_date):
        self.trainee_ID = trainee_ID
        self.start_date = start_date

class Interview:
    def __init__(self,ID,candidate,interviewer,timeslot,interview_Results):
        self.ID = ID
        self.candidate = candidate
        self.interviewer = interviewer
        self.timeslot = timeSlot
        self.interview_Results = interview_Results

class TimeSlot:
    def __init__(self, ID, interviewer,candidate,interview,date_time):
        self.ID = ID
        self.interviewer = interviewer
        self.candidate = candidate
        self.interview = interview
        self.date_time = date_time




####################
# Main
####################


user2 = Interviewer("011",'Ariel','Piotraut','ariel@gmail','060606','10 sept, 11 sept','Week of 13th','Job1, Job2')
print(user2.employee_ID, user2.firstName, user2.last_name, user2.email, user2.phoneNum, user2.planned_interview, user2.availabilities,user2.created_job_Postings)
print(user2)



jobPost = Job_Posting('01', 'BARISTA', 'being the barista', '5', user2.last_name, 'created') 
print(jobPost)
print(jobPost.ID, jobPost.title, jobPost.description, jobPost.num_of_jobOffers, jobPost.interviewer, jobPost.application_Forms)





