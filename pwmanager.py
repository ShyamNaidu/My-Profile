def create_account():
    user = input("Enter User Name: ")
    pw = input("Enter password: ")

    with open('/workspaces/My-Profile/datastore/emppwman.txt','a') as f:
        f.write(user + '|' + pw + '\n')

create_account()

