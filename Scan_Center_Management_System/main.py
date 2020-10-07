import csv
from os import system, name
import time
#Clear Function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
#Print Statements
def Notation1Text():
    clear()
    print("\n\n************************************************************")
    print("*         Teresa Scan Center Management System             *")
    print("************************************************************")
    print("")
    print("")
    print("\n\n************************************************************")
    print("*         Press 1 for Administrative Officer               *")
    print("************************************************************")
    print("*               Press 2 for Doctor                         *")
    print("************************************************************")
    print("*               Press 3 to Exit                            *")
    print("************************************************************")
    print("")

def Notation2Text():
    clear()
    print("\n\n************************************************************")
    print("*       Welcome to Administrative officer mode             *")
    print("************************************************************")
    print("\n\n-----------------------------------------")
    print("|To manage patients Enter 1 		|\n|To manage docotrs Enter 2	 	|\n|To Change Password Enter 3 	     |\n|To go Back Enter 4  	 	|")
    print("-----------------------------------------")


def DoctorManagementText():
    clear()
    print("******************************************************")
    print("              Doctor Management Area                 *")
    print("******************************************************")
    print("\n\n-----------------------------------------")
    print("|To Search Doctor Enter 1 		|\n|To Add Docotrs Enter 2	 	|\n|To go Back Enter 3  	|")
    print("-----------------------------------------")

#Password Management
def password_check():
    clear()
    print("")
    print("****************************************")
    password_input=input("Please enter your password : ")
    password_file=open('password.txt')
    password_file.seek(0)
    original_password=password_file.read()
    return password_input==original_password

def changePassword():
    clear()
    new_password=input("Please enter the new password : ")
    with open('password.txt',mode='w') as f:
        f.write(new_password)

    print("***************Password Updated Successfully******************")
    time.sleep(5)

#Read The DataBases
def Read_Doctors_DataBase():
    with open('Doctors.csv',mode='r',encoding='utf-8') as f:
        csv_data=csv.reader(f)
        database=list(csv_data)
        return database

def Read_Patients_DataBase():
    with open('Patients.csv',mode='r',encoding='utf-8') as f:
        csv_data=csv.reader(f)
        database=list(csv_data)
        return database

Doctors_Database=Read_Doctors_DataBase()
Doctors_Database=[item for item in Doctors_Database if item!=[]]
Patients_Database=Read_Patients_DataBase()
Patients_Database=[item for item in Patients_Database if item!=[]]

#OverWrite the Databases
def Write_Doctors_Database():
    with open('Doctors.csv',mode='w') as f:
        csv_writer=csv.writer(f)
        for item in Doctors_Database:
            csv_writer.writerow(item)

def Write_Patients_Database():
    with open('Patients.csv',mode='w') as f:
        csv_writer=csv.writer(f)
        for item in Patients_Database:
            csv_writer.writerow(item)

#Add Doctor and Patient Section
def AddDoctor():
    clear()
    print("**************Enter the Doctor Details****************\n\n")
    name=input("1.Name : ")
    title=input("2.Title (Radiologist/Cardiologist/Pathologist) : ")
    gender=input("3.Gender : ")
    dob=input("4.Date of Birth : ")
    qualification=input("5.Qualification : ")
    lsno=input("6.Medical License No. : ")
    address=input("7.Address : ")
    contactno=input("8.Contact number : ")
    email=input("9.Email ID : ")
    if len(Doctors_Database)>0:
        id_no=max([int(i[0]) for i in Doctors_Database])+1
    else:
        id_no=1
    Doctors_Database.append([id_no,name,title,gender,dob,qualification,lsno,address,contactno,email])
    Write_Doctors_Database()
    print("\n**************Doctor Added Successfully  "+"Teresa Scan Center ID no Gnerated is :"+str(id_no)+"  ****************\n\n")
    time.sleep(2)

def AddPatient():
    clear()
    print("\n\n**************Enter the Patient Details****************\n\n")
    name=input("1.Name : ")
    gender=input("2.Gender : ")
    dob=input("3.Date of Birth : ")
    address=input("4.Address : ")
    contactno=input("5.Contact number : ")
    test_type=input("6.Test type (X-ray/ECG/CT Scan/MRI Scan/Cardiac CT) : ")
    fees=input("7.Fees : ")
    docotrs_name=input("8.Doctors Name : ")
    refered_by=input("9.Hospital Referred by : ")
    reg_date=input("10.Registration Date : ")
    test_date=input("11.Test Date : ")
    if len(Patients_Database)>0:
        reg_no=max([int(i[0]) for i in Patients_Database])+1
    else:
        reg_no=1
    Patients_Database.append([reg_no,name,gender,dob,address,contactno,test_type,fees,docotrs_name,refered_by,reg_date,test_date])
    Write_Patients_Database()
    print("\n**************Patient Added Successfully  "+"Registration no:"+str(reg_no)+" ****************\n\n")
    time.sleep(2)

#Print Doctor And Patient Details Section
def printDoctorDetails(item):
    clear()
    print("Teresa Scan Center ID : "+str(item[0]))
    print("1.Name : "+str(item[1]))
    print("2.Title (Radiologist/Cardiologist/Pathologist) : "+str(item[2]))
    print("3.Gender : "+str(item[3]))
    print("4.Date of Birth : "+str(item[4]))
    print("5.Qualification : "+str(item[5]))
    print("6.Medical License No. : "+str(item[6]))
    print("8.Contact number : "+str(item[8]))
    print("7.Address : "+str(item[7]))
    print("9.Email ID : "+str(item[9]))

def printPatientDetails(item):
    clear()
    print("Regestration Number is : "+str(item[0]))
    print("1.Name : "+str(item[1]))
    print("2.Gender : "+str(item[2]))
    print("3.Date of Birth : "+str(item[3]))
    print("4.Address : "+str(item[4]))
    print("5.Contact number : "+str(item[5]))
    print("6.Test type (X-ray/ECG/CT Scan/MRI Scan/Cardiac CT) : "+str(item[6]))
    print("7.Fees : "+str(item[7]))
    print("8.Doctors Name : "+str(item[8]))
    print("9.Hospital Referred by : "+str(item[9]))
    print("10.Registration Date : "+str(item[10]))
    print("11.Test Date : "+str(item[11]))

#Edit Doctor and Patient Details
def editDoctorDetails():
    while True:
        clear()
        print("******************************************************")
        print("              Search Doctor Portal                   *")
        print("******************************************************\n")
        print("********************Enter the method of Search**********************\n")
        print("|To Search Doctor by Medical License No. Enter 1|\n|To Search Doctor by Teresa Scan Center Id Enter 2|\n|To Search Doctor by Name Enter 3|\n|To Search Doctor by Contact number Enter 4|\n|To Exit Enter 5|")
        print("******************************************************\n")
        Search_doctor_choice=input("Please Choose the required option : ")
        while not(Search_doctor_choice=='1' or Search_doctor_choice=='2' or Search_doctor_choice=='3' or Search_doctor_choice=='4' or Search_doctor_choice=='5'):
            Search_doctor_choice=input("Please Choose the required option : ")
        if Search_doctor_choice=='5':
            break
        elif Search_doctor_choice=='1':
            num=input("Please enter the Medical License No. of the required Doctor : ")
            p=6
        elif Search_doctor_choice=='2':
            num=input("Please enter the Teresa Scan Center Id of the required Doctor : ")
            p=0
        elif Search_doctor_choice=='3':
            num=input("Please enter the Name of the required Doctor(Name Must Be In Capitalized Format) : ")
            p=1
        elif Search_doctor_choice=='4':
            num=input("Please enter the Contact no of the required Doctor : ")
            p=8

        for i in range(len(Doctors_Database)):
            if str(Doctors_Database[i][p])==num:
                printDoctorDetails(Doctors_Database[i])
                while True:
                    print("\n\n|To Edit Doctor Details Enter 1\n|To Exit Enter 2                \n")
                    n=input("Please enter your option : ")
                    if n=='2':
                        break
                    elif n=='1':
                        slno=''
                        while type(1)!=type(slno):
                            try:
                                slno=int(input("Enter the serial no of the details you want to edit : "))
                            except:
                                print("Please enter an INTEGER")
                        if slno==1 or slno==6:
                            print("Name and Medical licsense no Cannot be edited : ")
                        else:
                            Doctors_Database[i][slno]=input("Please enter the new Placeholder ")
                            Write_Doctors_Database()
                            clear()
                            print("\n\n*********Printing the updated deteils************\n\n")
                            printDoctorDetails(Doctors_Database[i])
                break
        else:
                print("Item Not found")
                print("Redirecting to the previous portal.")
                time.sleep(4)

def editPatientDetails():
    while True:
        clear()
        print("******************************************************")
        print("              Search Patient Portal                   *")
        print("******************************************************\n")
        print("********************Enter the method of Search**********************\n")
        print("|To Search Patient by Regestration Number Enter 1|\n|To Search Patient by Name Enter 2|\n|To Search Patient by Contact number Enter 3|\n|To Exit Enter 4|")
        print("******************************************************\n")
        selection=input("Please Choose the required option : ")
        while not(selection=='1' or selection=='2' or selection=='3' or selection=='4'):
            selection=input("Please Choose the required option : ")
        if selection=='1':
            num=input("Please enter the Registration number of the required Patient : ")
            p=0
        elif selection=='2':
            num=input("Please enter the Name of the required Patient : ")
            p=1
        elif selection=='3':
            num=input("Please enter the Contact no of the required Patient : ")
            p=5
        else:
            break

        for i in range(len(Patients_Database)):
            if str(Patients_Database[i][p])==num:
                printPatientDetails(Patients_Database[i])
                while True:
                    print("\n\n|To Edit Patient Details Enter 1\n|To Exit 2                |\n")
                    n=input("Please enter your option : ")
                    if n=='2':
                        break
                    elif n=='1':
                        slno=''
                        while type(1)!=type(slno):
                            try:
                                slno=int(input("Enter the serial no of the details you want to edit : "))
                            except:
                                print("Please enter an INTEGER")
                        if slno==1:
                            print("Name Cannot be edited : ")
                        else:
                            Patients_Database[i][slno]=input("Please enter the new Placeholder ")

                            Write_Patients_Database()
                            print("\n\n*********Printing the updated deteils************\n\n")
                            printPatientDetails(Patients_Database[i])
                break
        else:
                print("Item Not found")
                print("Redirecting to the previous portal.")
                time.sleep(4)

#Login System As a Doctor
def DoctorLogin():
    Doctors_id_Database=[i[0] for i in Doctors_Database]
    Doctors_Name_Database=[i[1].lower() for i in Doctors_Database]
    while True:
        clear()
        print("\n******************************************************")
        print("*                     Doctor Login                   *")
        print("******************************************************\n")
        go_back=input("\nTo Go Back Enter 5, Else any character : ")
        if go_back=='5':
            break
        name=input("\nPlease enter your name : ")
        id=''
        while type(id)!=type(1):
            try:
                id=int(input("\nPlease enter your Teresa Scan Center ID : "))
            except :
                print('\nPlease enter an INTEGER')
        for i in range(len(Doctors_Database)):
            if str(id)==str(Doctors_id_Database[i]) and name.lower()==Doctors_Name_Database[i].lower():
                clear()
                print("\n\n*********************You are logged in as***********************\n\n")
                printDoctorDetails(Doctors_Database[i])
                print("\n\n*********************Redirecting to patient management portal**********************")
                time.sleep(5)
                PatientManagementPortal()
                break
        else:
            print('\nInvalid ID NO or Name\n press 5 to try again  ')
            if input()!='5':
                break

#Patient Management Portal
def PatientManagementPortal():
    while True:
        clear()
        print("******************************************************")
        print("              Patient Management Area                 *")
        print("******************************************************")
        print("\n\n-----------------------------------------")
        print("|To Search Patient Enter 1 		\n|To Add Patient Enter 2	 	\n|To go Back Enter 3  	")
        print("-----------------------------------------\n")
        patient_area_choice=input("Enter Your Choice : ")
        while not(patient_area_choice=='1' or patient_area_choice=='2' or patient_area_choice=='3'):
            patient_area_choice=input("Please Enter Correct Choice : ")

        if patient_area_choice=='1':
            editPatientDetails()
        elif patient_area_choice=='2':
            AddPatient()
        else:
            break


##Body, Administrative officer Portion
while True:
    Notation1Text()
    choice1='4'
    while not(choice1=='1' or choice1=='2' or choice1=='3'):
        choice1=input("Enter the correct choice :")
    if choice1=='1':
        while not password_check():
            print("Incorrect password try again")
        while True:
            Notation2Text()
            admin_choice=input("\nEnter the correct choice : ")
            while not(admin_choice=='1' or admin_choice=='2' or admin_choice=='3' or admin_choice=='4'):
                admin_choice=input("\nEnter the correct choice : ")
            if admin_choice=='3':
                changePassword()
            elif admin_choice=='2':
                while True:
                    DoctorManagementText()
                    admin_doctor_choice=input('Please enter your choice : ')
                    while not(admin_doctor_choice=='1' or admin_doctor_choice=='2' or admin_doctor_choice=='3'):
                        admin_doctor_choice=input('Please enter your choice again : ')
                    if admin_doctor_choice=='1':
                        editDoctorDetails()
                    elif admin_doctor_choice=='2':
                        AddDoctor()
                    elif admin_doctor_choice=='3':
                        break
            elif admin_choice=='4':
                break
            elif admin_choice=='1':
                PatientManagementPortal()
    elif choice1=='2':
        DoctorLogin()

    else:
        break
