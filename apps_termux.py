import sys
import os
import time
#App Strings
###
#┌────────[pro@host]──────
#│
#└──────>
###
system1 = "figlet Termux"
os.system('pkg install figlet')
time.sleep(2)
os.system('clear')
os.system(system1)
print("\033[1;34mInstall You favorites programs\n\033[0m")
print("~~~~~~~~~~~~(Install Programs)~~~~~~")
print("|")
input1 = input("~~~~~~~> ")
if input1 == "--help":
	print("Ups! Error no found shell_install.sh please install")
elif input1 == "--list":
		os.system('apt list')
elif input1 == "--mode install":
	print("|\033[1;32mMode install apps activate ✓\033[0m")
	print("|")
	input2 = input("~~~~~~~~[install]~~~~> ")
	os.system('apt install '+input2)
elif input1 == "--unistall":
	print("| unistall programs ")
	input3 = input("~~~~~~> ")
	os.system('apt remove '+input3)
elif input1 == "--run":
	os.system('python run_module.py')
else:
	print("UPS")			
