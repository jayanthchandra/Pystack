import os
print("1.List all user\n"
	"2.List identity service catalog\n"
	"3.Discover keystone endpoints\n"
	"4.List all Service")
ip=int(input())
if ip==1:
	os.system("keystone user-list")
	
elif ip==2:
	os.system("keystone catalog")
	
elif ip==3:
	os.system("keystone discover")
	
elif ip==3:
	os.system("keystone service-list")

else:
	print("Wrong Option")