import os
import sys
from io import open
def access():
	ruta=os.getcwd()
	arch="main.sh"
		  			
	if ruta == os.getcwd():
		crear=open(arch,"a")
	#	argv=True
	#	crear.close()
	#	if argv:
	
#		crear=open(arch,"w")
		crear.write("git clone https://github.com/xelAStone/HackSt/\n")
		crear.close()
	else:
#			argv=False		
#	return(arch,argv)
		sys.exit(1)

def start():
	os.system("bash main.sh")

if __name__=="__main__":
	access()
	import time
	time.sleep(1)
	start()

