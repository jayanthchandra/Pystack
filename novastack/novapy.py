import os
#os.system("source openrc admin admin")
print("1.Status of Nova Service\n"
	"2.List all Nova Service\n"
	"3.List all Images\n"
	"4.List all Flavours")
ip=int(input("Enter Option :=> "))
if ip==1:
	os.system("./jay.sh")
elif ip == 2:
	os.system("nova list")
elif ip == 3:
	os.system("nova image-list")
elif ip ==  4:
	os.system("nova flavor-list")
else :
	print("Wrong Option")