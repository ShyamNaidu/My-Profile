def chktxtfile(username):
    with open('datastore/emppwman.txt','r') as f:
        for line in f:
            if username in line:
                return True
        return False


def create_account():
    user = input("Enter User Name: ")

    if user.strip == "":
        print("Wrong Entry. Try Again.")
        return

    if chktxtfile(user):
        print("User Name already exists. Please try again.")
        return
    
    pw = input("Enter password: ")
        
    if pw.strip == "":
        print("Invalid password. Account creation aborted. Try again.") 
        return   

    with open('datastore/emppwman.txt','a') as f:
        f.write(user + '|' + pw + '\n')

def veiw_account():
    user = input("Enter Your User Name: ")


create_account()

