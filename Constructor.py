import email


import email


class Candidate:
    def __init__(self,candidate_ID,firstName,lastName,dateOfBirth,email,phoneNum, applicationForm, tentative_appointment, interview, is_archived):
        self.candidate_ID = candidate_ID
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phoneNum = phoneNum
        self.applicationForm = Application_Form
        self.tentative_appointment = [TimeSlot]
        self.interview = Interview
        self.is_archived = is_archived

    def is_available(self,TimeSlot):
        interview_av = Interview(" ", self, TimeSlot.interviewer, TimeSlot, " ")
        return interview_av

class Trainee(Candidate):
        def __init__(self,trainee_ID,start_date):
            self.trainee_ID = trainee_ID
            self.start_date = start_date


class Interviewer:
    def __init__(self,employee_ID,firstName,lastName,dateOfBirth,email,phoneNum, planned_interview,availabilities,created_job_Postings):
        self.employee_ID = employee_ID
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phoneNum = phoneNum
        self.planned_interview = [Interview] 
        self.availabilities = [TimeSlot] 
        self.created_job_Postings = [Job_Posting]

    def add_TimeSlot(self,TimeSlot):
        self.availabilities.append(TimeSlot)

class Job_Posting:
    def __init__(self, post_ID, title, description, num_of_jobOffers, interviewer, application_Forms):
        self.post_ID = post_ID
        self.title = title
        self.description = description
        self.num_of_jobOffers = num_of_jobOffers
        self.interviewer = Interviewer
        self.Application_Forms = [Application_Form]

<<<<<<< HEAD
class Application_Form:
    def __init__(self, ID, candidate, jobPosting, CV):
        self.ID = ID
        self.candidate = Candidate
        self.jobPosting = Job_Posting
        self.CV = CV


class Interview:
    def __init__(self,ID,candidate,interviewer,timeslot,interview_Results):
        self.ID = ID
        self.candidate = Candidate
        self.interviewer = Interviewer
        self.timeslot = TimeSlot
=======
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
>>>>>>> 69a5b37d4e544d853d3564faf42b373f70fb3fe1
        self.interview_Results = interview_Results

    def inform(self, Interview, Candidate):
        if Interview.interview_Results:
            Candidate.is_archived = False
        else:
            Candidate.is_archived = True

class TimeSlot:
<<<<<<< HEAD
    def __init__(self,ID,interviewer,candidate,interview,date_time):
        self.ID = ID
        self.interviewer = Interviewer
        self.candidate = Candidate
        self.interview = Interview
        self.date_time = date_time

    def send_timeSlots(self, Candidate):
        Candidate.tentative_appointment.append([TimeSlot])
    
=======
    def __init__(self, interviewer,candidate,interview,date_time):
        self.interviewer = interviewer
        self.candidate = candidate
        self.interview = interview
        self.date_time = date_time

>>>>>>> 69a5b37d4e544d853d3564faf42b373f70fb3fe1

####################
# Main
####################

interviewer_01 = Interviewer("01","John","Doe","01/01/1964","johndoe@gmail.com","514-815-6677",[],[],[])

<<<<<<< HEAD

job_post_01 = Job_Posting("01", "Cashier", "Assure the welcoming of customers and cash register operations.", "8", interviewer_01, [])
#appending job posting into interviewer object
interviewer_01.created_job_Postings.append(job_post_01)


app_form_01 = Application_Form("01", " ", job_post_01, "C:Users\JohnDoe\Desktop\Candidate_CV\CV_1")
#appending application_form into interviewer job_posting object 
job_post_01.Application_Forms.append(app_form_01)



candidate_01 = Candidate("01", "Bruce", "Banner", "02/02/1993", "brucebannerhulk@gmail.com", "438-661-7389", app_form_01, [], " ", 0) #not archived
#appending candidate into application_form object 
app_form_01.candidate = candidate_01
=======
user = Interviewer("011",'Ariel','Piotraut','ariel@gmail','060606','10 sept, 11 sept','Week of 13th','Job1, Job2')
print(user.employee_ID, user.firstName, user.last_name, user.email, user.phoneNum, user.planned_interview, user.availabilities, user.created_job_Postings)
print(user)

jobPost = Job_Posting('01', 'BARISTA', 'being the barista', '5', user.last_name, 'created') 
print(jobPost)
print(jobPost.ID, jobPost.title, jobPost.description, jobPost.num_of_jobOffers, jobPost.interviewer, jobPost.application_Forms)
>>>>>>> 69a5b37d4e544d853d3564faf42b373f70fb3fe1


interview_01 = Interview("01", candidate_01, interviewer_01, " ", "Candidate has successfully passed the interview")
#appending Interview into interviewer object
interviewer_01.planned_interview.append(interview_01)
#appending interview into candidate object
candidate_01.interview = interview_01

############################
# FUNCTIONS
############################

<<<<<<< HEAD
timeslot_01 = TimeSlot("01", interviewer_01, candidate_01, interview_01, "December 2nd 2022 - 1PM")
#appending timeslot into interview object
interview_01.timeslot = timeslot_01
#appending timeslot into candidate object
candidate_01.tentative_appointment.append(timeslot_01)
#appending timeslot into interviewer object
interviewer_01.availabilities.append(timeslot_01)


############################
# FUNCTIONS
############################

#add_timeslot method:
timeslot_02 = TimeSlot("02", interviewer_01, " ", " ", "December 5th 2022 - 3PM")
timeslot_03 = TimeSlot("03", interviewer_01, " ", " ", "December 6th 2022 - 5PM")
interviewer_01.add_TimeSlot(timeslot_02)
interviewer_01.add_TimeSlot(timeslot_03)

#send_timeSlots:
timeslot_01.send_timeSlots(candidate_01)
timeslot_02.send_timeSlots(candidate_01)
timeslot_03.send_timeSlots(candidate_01)
print(candidate_01.tentative_appointment)

#is_available method:
print(candidate_01.is_available(timeslot_03))

#inform method:
interview_02 = Interview("2", candidate_01, interviewer_01, timeslot_02, False)
interview_02.inform(interview_02,candidate_01)
print(candidate_01.is_archived)
=======
def is_available(Candidate, Interviewer):
    interview = Interview(Interview_ID, Candidate, Interviewer, Candidate.tentative_appointment, 0)    
    return interview 
>>>>>>> 69a5b37d4e544d853d3564faf42b373f70fb3fe1

def send_timeSlots(self, Candidate,TimeSlot):
    self.Candidate.tentative_appointments.append([TimeSlot])

def inform(Interview, Candidate):
    if Interview.interview_Result == True: 
        Candidate.is_archived = False
    else: 
        Candidate.is_archived = True