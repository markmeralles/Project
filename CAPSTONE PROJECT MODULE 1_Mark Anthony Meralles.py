listEmployee =[
    {"Employee ID" : '22001',
     "Name" : "Robert Langdon",
     "Age" : 24,
     "Sex" : "Male",
     "Department" : "Research and Development",
     "Job Title" : "Research and Development Officer",
     "Date Hired" : "January 10, 2022"
    },
    {"Employee ID" : '22002',
     "Name" : "Edmond Kirsch",
     "Age" : 27,
     "Sex" : 'Male',
     "Department" : "Accounting",
     "Job Title" : "Accounting Supervisor",
     "Date Hired" : "February 14, 2022"
    },
    {"Employee ID" : '22003',
     "Name" : "Ambra Vidal",
     "Age" : 30,
     "Sex" : 'Female',
     "Department" : "Information Technology",
     "Job Title" : "Information Security Specialist",
     "Date Hired" : "March 21, 2022"
    },
    {"Employee ID" : '22004',
     "Name" : "Antonio Valdespino",
     "Age" : 35,
     "Sex" : "Male",
     "Department" : "Human Resources",
     "Job Title" : "Compensation and Benefits Manager",
     "Date Hired" : "April 18, 2022"
    },
    {"Employee ID" : '22005',
     "Name" : "Monica Martín",
     "Age" : 31,
     "Sex" : "Female",
     "Department" : "Marketing",
     "Job Title" : "Brand Manager",
     "Date Hired" : "May 22, 2018"
    }
]

# Selection Menu
def main_menu() :
    select = input('''
    ***Company Profile***

    Menu List:
    1. Show company employee profile
    2. Add an employee profile
    3. Update an employee profile
    4. Delete an employee profile
    5. Exit Program

    Enter the selected menu number: 
    ''')

    while True:
        if select == '1' :
            read_data()
        elif select == '2' :
            create_data()
        elif select == '3' :
            update_data()
        elif select == '4' :
            delete_data()
        elif select == '5' :
            break
        else :
            print ('\nThe value you entered is not in the options.')
            main_menu()

# Show All data
def show_all() :
    print('\n***List of Company Employees***\n')
    for i in range(len(listEmployee)) :
        print('''
            Index: {}
            Employee ID : {}
            Name : {}
            Age : {}
            Sex : {}
            Department : {}
            Job Title : {}
            Date Hired : {}
            '''.format((i+1), listEmployee[i]["Employee ID"], listEmployee[i]["Name"], listEmployee[i]["Age"],
            listEmployee[i]["Sex"], listEmployee[i]["Department"], listEmployee[i]["Job Title"], 
            listEmployee[i]["Date Hired"]))

# Check data - To check if a value is present in our dictionary
def check(sample_dict, employee_ID):
    for elem in sample_dict:
        if employee_ID in elem.values():
            return True
    return False
    
# Read data (Main Menu Option 1)
def read_data() :
    print('''
        1. Show all company employee profile
        2. Show a specific company employee profile
        3. Back to Main Menu
        ''')
    read = input("Please choose from the following options (1, 2, or 3): ")
    if read == '1' :
        if len(listEmployee) != 0 :
            show_all()
        else:
           print("\nNo data found.") 
    elif read == '2' :
        if len(listEmployee) != 0 :
            emp_no = input("Please input employee ID: ")
            if check(listEmployee, emp_no) == True :
                for index in range(len(listEmployee)) :
                    for key in listEmployee[index] :
                        if listEmployee[index][key] == emp_no :
                            print('''
                            Employee ID : {}
                            Name : {}
                            Age : {}
                            Sex : {}
                            Department : {}
                            Job Title : {}
                            Date Hired : {}
                            '''.format(listEmployee[index]["Employee ID"], listEmployee[index]["Name"], 
                            listEmployee[index]["Age"], listEmployee[index]["Sex"],listEmployee[index]["Department"], 
                            listEmployee[index]["Job Title"], listEmployee[index]["Date Hired"]))
            else :
                print('The employee ID you entered does not exist.')
        else :
            print("\nNo data found.")
    elif read == '3' :
        main_menu()
    else :
        print("\n\nThe value you entered is not in the options.")

# Create Data (Main Menu Option 2)
def create_data() :
    print('''
        1. Create an employee profile
        2. Back to Main Menu
    ''')
    create = input("Please choose from the following options (1 or 2): ")
    if create == '1' :
        employee_number = input("Enter Employee ID: ")
        if check(listEmployee, employee_number) is True :
            print('\nThe employee ID you entered is already taken.')
        else:
            name = input("Enter name of employee: ")
            age = input("Enter age of employee: ")
            sex = input("Enter sex of employee: ")
            department = input("Enter department of employee: ")
            job_title = input("Enter job title of employee: ")
            date_hired = input("Enter date the employee was hired: ")
            save = input('\nDo you want to save the changes? (Y/N): ')
            if save == 'Y' or save == 'y' :
                listEmployee.append({
                            "Employee ID" : employee_number,
                            "Name" : name,
                            "Age" : age,
                            "Sex" : sex,
                            "Department" : department,
                            "Job Title" : job_title,
                            "Date Hired" : date_hired
                            })
                print("\nData Saved.")
                show_all()
            elif save == 'N' or save == 'n' :
                create_data()
            else:
                print('\nThe value you entered is not in the options.')
    
    elif create == '2' :
        main_menu()
    else :
        print('\nThe value you entered is not in the options.')

# Update Data (Main Menu Option 3)
def update_data() :
    print('''
        1. Update an employee profile
        2. Back to Main Menu
    ''')
    updt_data = input("Please choose from the following option: ")
    if updt_data == '1':
        if len(listEmployee) != 0 :
            show_all()
            index_employee = int(input("Please input the index of employee ID you want to update: "))
            if 0 < index_employee <= len(listEmployee):
                print('''
                    Employee ID : {}
                    Name : {}
                    Age : {}
                    Sex : {}
                    Department : {}
                    Job Title : {}
                    Date Hired : {}
                    '''.format(listEmployee[index_employee-1]["Employee ID"], listEmployee[index_employee-1]["Name"], 
                    listEmployee[index_employee-1]["Age"], listEmployee[index_employee-1]["Sex"],
                    listEmployee[index_employee-1]["Department"], listEmployee[index_employee-1]["Job Title"],
                    listEmployee[index_employee-1]["Date Hired"]))
                upd = input("Are you sure want to update this employee profile (Y/N)? ")
                if upd == 'Y' or upd == 'y' :
                    updt = input('''
                                1. Employee ID
                                2. Name
                                3. Sex
                                4. Department
                                5. Job Title
                                6. Date Hired

                                Please choose the information you want to update: (Input the number)

                                ''')
                    if updt == '1' :
                        new_employee_number = input('Please input the new value for employee ID: ')
                        listEmployee[index_employee-1]['Employee ID'] = new_employee_number
                        show_all()
                    elif updt == '2' :
                        new_name = input('Please input the new value for name: ')
                        listEmployee[index_employee-1]['Name'] = new_name
                        show_all()
                    elif updt == '3' :
                        new_sex = input('Please input the new value for sex: ')
                        listEmployee[index_employee-1]['Sex'] = new_sex
                        show_all()
                    elif updt == '4' :
                        new_dept = input('Please input the new value for department: ')
                        listEmployee[index_employee-1]['Department'] = new_dept
                        show_all()
                    elif updt == '5' :
                        new_job_title = input('Please input the new value for job title: ')
                        listEmployee[index_employee-1]['Job Title'] = new_job_title
                        show_all()
                    elif updt == '6' :
                        new_date_hired = input('Please input the new value for date hired: ')
                        listEmployee[index_employee-1]['Date Hired'] = new_date_hired
                        show_all()
                    else :
                        print('\nThe value you entered is not in the options.')
                elif upd == 'N' or upd == 'n' :
                    update_data()
                else :
                    print('\nThe value you entered is not in the options.')
            else :
                print('\nThe index of employee ID you entered does not exist.')
        else :
            print('\nNo data found.')
    elif updt_data == '2':
        main_menu()
    else :
        print('\nThe value you entered is not in the options.')

# Delete Data (Main Menu Option 4)
def delete_data() :
    print('''
        1. Delete an employee profile
        2. Back to Main Menu
    ''')
    del_data = input("Please choose from the following option: ")
    if del_data == '1':
        if len(listEmployee) != 0 :
            show_all()
            index_employee = int(input("Please input the index of the employee ID you want to delete: "))
            if 0 < index_employee <= len(listEmployee):
                print('''
                    Employee ID : {}
                    Name : {}
                    Age : {}
                    Sex : {}
                    Department : {}
                    Job Title : {}
                    Date Hired : {}
                    '''.format(listEmployee[index_employee-1]["Employee ID"], listEmployee[index_employee-1]["Name"], 
                    listEmployee[index_employee-1]["Age"], listEmployee[index_employee-1]["Sex"],
                    listEmployee[index_employee-1]["Department"], listEmployee[index_employee-1]["Job Title"],
                    listEmployee[index_employee-1]["Date Hired"]))
                erase = input("Are you sure want to delete this employee profile (Y/N)? ")
                if erase == 'Y' or erase == 'y' :
                    del listEmployee[(index_employee-1)]
                    print('\nEmployee data has been deleted.')
                    show_all()
                elif erase == 'N' or erase == 'n' :
                    delete_data()
                else :
                    print('\nThe value you entered is not in the options.')
            else:
                print('\nThe index number of employee ID you entered does not exist.')
        else :
            print('\nNo data found.')
    elif del_data == '2':
        main_menu()       
    else :
        print('\nThe value you entered is not in the options.')
    
main_menu()