def view_emp_records():
    with open('/workspaces/My-Profile/datastore/employees.txt', 'r') as f:
        for line in f.readlines():
            if(line != "\n"):
                data = line.rstrip()
                name, des = data.split(",") 
                print(name + "-" + des) 

def add_new_record():
    name = input("Enter Employee Name: ")
    des = input("Enter Employee Designation: ")

    with open('/workspaces/My-Profile/datastore/employees.txt', 'a') as f:
        f.write(name + ',' + des + "\n")

while True:
    resp = input("Do you want to view/add new record (V/A/Q for quit): ")
    if resp == 'q':
        break
    if resp == 'a':
        add_new_record()
    if resp == 'v':
        view_emp_records()

