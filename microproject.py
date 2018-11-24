employee={}
n=input("ENTER THE NUMBER OF EMPLOYEES ")
salary=0
print"1.STAFF"
print"2.SUPERVISOR"
print"3.MANAGER"
print"4.CHAIRMAN"
print"5.CEO"
for i in range(n):
	Empid=input("Enter the id no.")
    	Name=raw_input("Enter the name of the employee ")
    	Address=raw_input("Enter the adress of the employee ")
    	Phone=input("Enter the contact number of the employee ")
    	Attendance =input("ENter the attadence of the employee ")
    	Bonus=input("Enter the extra working hours of the employee ")
    	Grade=raw_input("Enter the post of the employee ")
    	if(Grade=="STAFF" or Grade=="staff"):	
       		salary=(330*Attendance)+(Bonus*100)
    	elif(Grade=="SUPERVISOR" or Grade=="supervisor"):
        	salary=(500*Attendance)+(Bonus*200)
    	elif(Grade=="MANAGER" or Grade=="manager"):
        	salary=(660*Attendance)+(Bonus*300)
    	elif(Grade=="CHAIRMAN" or Grade=="chairman"):
            	salary=(1300*Attendance)+(Bonus*400)
    	elif(Grade=="CEO" or Grade=="ceo"):
            	salary=(2600*Attendance)+(Bonus*500)
    	else:
            	print"invalid entry"
	employee[Empid]=salary

    	employee['name']=Name
    	employee['address']=Address
    	employee['phone']=Phone
    	employee['bonus']=Bonus
    	employee['grade']=Grade
    	
    	print "Name : ",employee['name'],"\nAddress : ",employee['address'],"\nContact Number :",employee['phone'],"\nGrade :",employee['grade'],"\nBonus :",employee['bonus'],"\nSalary :",employee[Empid]
	print ("DO YOU WANT TO CHANGE SALARY?")
	ch= raw_input("Enter the choice (Y/N):") 
	if(ch=='Y'):
		inc=input("Enter the amount to be incremented")
		employee[Empid]=employee[Empid]+inc
		print ("New details are:")
                print "Name : ",employee['name'],"\nAddress : ",employee['address'],"\nContact Number :",employee['phone'],"\nGrade :",employee['grade'],"\nBonus :",employee['bonus'],"\nSalary :",employee[Empid]


print "****************\n\n\n\n\n\t\tCREATORS\n\t1.FRANJO JOY\n\t2.ANEETTA MARIYA WILSON\n\t3.SUSAN REBI MATHEW\n****************"
