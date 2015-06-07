import os
print("Neutron Services\n")
print("1.Create another  network\n"
	"2.Create a subnet\n"
	"3.List Network\n"
	"4.List Subnet\n"
	"5.Examine details of Network\n"
	"6.Examine details of Subnet")
ip=int(input("Enter Option :=> "))
if ip == 1:
	neu=raw_input("Enter Network Name : ")
	os.system("neutron net-create"+ neu)
elif ip== 2:
	neu=raw_input("Enter Network name")
	addr=raw_input("Enter Ip and Port :")
	os.system("neutron subnet-create "+ neu + addr)
elif ip==3:
	os.system("neutron net-list")
elif ip == 4:
	os.system("neutron subnet-list")
elif ip==5:
	j=raw_input("Enter id/name of network : ")
	os.system("neutron net-show "+ j)
elif ip==6:
	j=raw_input("Enter id/name of network : ")
	os.system("neutron subnet-show "+ j)
else :
	print("Wrong Option")
