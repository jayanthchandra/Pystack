import os
print("Glance Services\n")
print("1.List accessible images\n"
	"2.Delete specified image\n"
	"3.Describe a specific image\n"
	"4.update image")
ip=int(input("Enter Option :=> "))
if ip == 1:
	os.system("glance image-list")
elif ip== 2:
	img=raw_input("Enter image name : ")
	os.system("glance image-delete "+ img)
elif ip==3:
	img=raw_input("Enter image name : ")
	os.system("glance image-show "+ img)
elif ip==4:
	img=raw_input("Enter image name : ")
	os.system("glance image-update "+ img)
