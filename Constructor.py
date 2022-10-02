#Name: your_name
#Date: today_date
#Comments: Comments on what was done on this commit.

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

####################
# Main
####################

if __name__ == "__main__":
    user1 = Candidate('Amine', 'Hadji', 'aamine.hadji.99@gmail.com')
    print(user1)