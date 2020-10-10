from scipy.stats import sem, t
from scipy import mean
import matplotlib.pyplot as plt
import math
import numpy
xaxis=[]
AIAthru=[]
AIAvnfs = []
AIAnodes = []
AIAres = []
AIAdelay = []
AIAthru_final = []

algodelay=[]
algothru=[]
algovnfs = []
algonodes = []
algores = []
algothru_final = []

SPHdelay=[]
SPHthru=[]
SPHvnfs = []
SPHnodes = []
SPHres = []
SPHthru_final = []

GUSdelay=[]
GUSthru=[]
GUSvnfs = []
GUSnodes = []
GUSres = []
GUSthru_final = []

confidence = 0.95
def function(data):
	n = len(data)
	m = mean(data)
	std_err = sem(data)
	# h = std_err * t.ppf((1 + confidence) / 2, n - 1)
	variance = sum([((x - m) **2) for x in data])/len(data)
	res = variance ** 0.5
	h = 1.960 * res/(len(data)**0.5)
	return m,h

#print m-h,m,m+h

import os
cmd1="g++ min_path.cpp -o simulation -std=c++11"
os.system(cmd1)
for i in range(100,101,100):		# for i in range(i1,j,k)    => for (int i=i1;i<j;i+=k)
	cmd3="rm AIAres"+str(i)
	cmd4="rm AIAthru"+str(i)
	cmd5="rm AIAvnfs"+str(i)
	cmd6="rm AIAnodes"+str(i)
	cmd7="rm AIAdelay"+str(i)
	cmd71="rm AIAthru_final"
	cmd8="rm SPHres"+str(i)
	cmd9="rm SPHthru"+str(i)
	cmd10="rm SPHvnfs"+str(i)
	cmd11="rm SPHnodes"+str(i)
	cmd12="rm SPHdelay"+str(i)
        cmd81="rm SPHthru_final"
	cmd13="rm GUSres"+str(i)
	cmd14="rm GUSthru"+str(i)
	cmd15="rm GUSvnfs"+str(i)
	cmd16="rm GUSnodes"+str(i)
	cmd17="rm GUSdelay"+str(i)
        cmd91="rm GUSthru_final"
	cmd18="rm algores"+str(i)
	cmd19="rm algothru"+str(i)
	cmd20="rm algovnfs"+str(i)
	cmd21="rm algonodes"+str(i)
	cmd22="rm algodelay"+str(i)
        cmd101="rm algothru_final"
	cmd11="rm final_file.txt"
	os.system(cmd3)
	os.system(cmd4)
	os.system(cmd5)
	os.system(cmd6)
	os.system(cmd7)
	os.system(cmd8)
	os.system(cmd9)
	os.system(cmd10)
	os.system(cmd11)
	os.system(cmd12)
	os.system(cmd13)
	os.system(cmd14)
	os.system(cmd15)
	os.system(cmd16)
	os.system(cmd17)
	os.system(cmd18)
	os.system(cmd19)
	os.system(cmd20)
	os.system(cmd21)
	os.system(cmd22)
	os.system(cmd71)
        os.system(cmd81)
        os.system(cmd91)
        os.system(cmd101)

	for x in range(10):
		cmd2="./simulation "+str(i)
		os.system(cmd2)
for i in range(100,101,100):
	file11="AIAres"+str(i)
	file12="AIAthru"+str(i)
	file13="AIAvnfs"+str(i)
	file14="AIAnodes"+str(i)
	file15="AIAdelay"+str(i)
	file16="AIAthru_final"+str(i)
	file21="SPHres"+str(i)
	file22="SPHthru"+str(i)
	file23="SPHvnfs"+str(i)
	file24="SPHnodes"+str(i)
	file25="SPHdelay"+str(i)
        file26="SPHthru_final"+str(i)
	file31="GUSres"+str(i)
	file32="GUSthru"+str(i)
	file33="GUSvnfs"+str(i)
	file34="GUSnodes"+str(i)
	file35="GUSdelay"+str(i)
	file36="GUSthru_final"+str(i)
	file41="algores"+str(i)
	file42="algothru"+str(i)
	file43="algovnfs"+str(i)
	file44="algonodes"+str(i)
	file45="algodelay"+str(i)
        file46="algothru_final"+str(i)
	# Opening files in read mode 
	f11=open(file11,"r")
	f12=open(file12,"r")
	f13=open(file13,"r")
	f14=open(file14,"r")
	f15=open(file15,"r")
        f16=open(file16,"r")
	f21=open(file21,"r")
	f22=open(file22,"r")
	f23=open(file23,"r")
	f24=open(file24,"r")
	f25=open(file25,"r")
        f26=open(file26,"r")
        f46=open(file46,"r")
        f36=open(file36,"r")
	f31=open(file31,"r")
	f32=open(file32,"r")
	f33=open(file33,"r")
	f34=open(file34,"r")
	f35=open(file35,"r")
	f41=open(file41,"r")
	f42=open(file42,"r")
	f43=open(file43,"r")
	f44=open(file44,"r")
	f45=open(file45,"r")


	list1=[]
#	print "Number of requests = "+str(i)
	contents=f11.read()
	arr=contents.split() 
	arr = list(map(float, arr))
#	print "AIAres = "
	num11= function(arr)
#	print str(num11)        
	AIAres.append(num11)


	list1=[]
	contents=f12.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "AIAthru = "
	num12= function(arr) 
#	print str(num12)	
	AIAthru.append(num12)
	


	list1=[]
	contents=f13.read()
	arr=contents.split() 
	arr = list(map(float, arr))
#	print "AIAvnfs = "
	num13= function(arr)
#	print str(num13)        
	AIAvnfs.append(num13)


	list1=[]
	contents=f14.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "AIAnodes = "
	num14= function(arr) 
#	print str(num14)	
	AIAnodes.append(num14)
	


	list1=[]
	contents=f15.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "AIAdelay = "
#	print arr
	num15= function(arr) 
#	print str(num15)	
	AIAdelay.append(num15)
	
	list1=[]
        contents=f16.read()
        arr=contents.split()
        arr = list(map(float, arr))
#       print "AIAdelay = "
#       print arr
        num16= function(arr)
#       print str(num15)        
        AIAthru_final.append(num16)





	list1=[]
#	print "Number of requests = "+str(i)
	contents=f21.read()
	arr=contents.split() 
	arr = list(map(float, arr))
#	print "SPHres = "
	num21= function(arr)
#	print str(num21)        
	SPHres.append(num21)


	list1=[]
	contents=f22.read()
	arr=contents.split()
	arr = list(map(float, arr))
	#print "SPHthru = "
	num22= function(arr) 
	#print str(num22)	
	SPHthru.append(num22)
	


	list1=[]
	contents=f23.read()
	arr=contents.split() 
	arr = list(map(float, arr))
#	print "SPHvnfs = "
	num23= function(arr)
	#print str(num23)        
	SPHvnfs.append(num23)


	list1=[]
	contents=f24.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "SPHnodes = "
	num24= function(arr) 
#	print str(num24)	
	SPHnodes.append(num24)
	


	list1=[]
	contents=f25.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "SPHdelay = "
	num25= function(arr) 
#	print str(num25)	
	SPHdelay.append(num25)
	


        list1=[]
        contents=f26.read()
        arr=contents.split()
        arr = list(map(float, arr))
#       print "AIAdelay = "
#       print arr
        num26= function(arr)
#       print str(num15)        
        SPHthru_final.append(num26)



	list1=[]
#	print "Number of requests = "+str(i)
	contents=f31.read()
	arr=contents.split() 
	arr = list(map(float, arr))
#	print "GUSres = "
	num31= function(arr)
#	print str(num31)        
	GUSres.append(num31)


	list1=[]
	contents=f32.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "GUSthru = "
	num32= function(arr) 
#	print str(num32)	
	GUSthru.append(num32)
	


	list1=[]
	contents=f33.read()
	arr=contents.split() 
	arr = list(map(float, arr))
#	print "GUSvnfs = "
	num33 = function(arr)
#	print str(num33)        
	GUSvnfs.append(num33)


	list1=[]
	contents=f34.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "GUSnodes = "
	num34= function(arr) 
#	print str(num34)	
	GUSnodes.append(num34)
	


	list1=[]
	contents=f35.read()
	arr=contents.split()
	arr = list(map(float, arr))
#	print "GUSdelay = "
	num35= function(arr) 
#	print str(num35)	
	GUSdelay.append(num35)
	




        list1=[]
        contents=f36.read()
        arr=contents.split()
        arr = list(map(float, arr))
#       print "AIAdelay = "
#       print arr
        num36= function(arr)
#       print str(num15)        
        GUSthru_final.append(num36)









	list1=[]
	#print "Number of requests = "+str(i)
	contents=f41.read()
	arr=contents.split() 
	arr = list(map(float, arr))
	#print "algores = "
	num41= function(arr)
	#print str(num41)        
	algores.append(num41)


	list1=[]
	contents=f42.read()
	arr=contents.split()
	arr = list(map(float, arr))
	#print "algothru = "
	num42= function(arr) 
	#print str(num42)	
	algothru.append(num42)
	


	list1=[]
	contents=f43.read()
	arr=contents.split() 
	arr = list(map(float, arr))
	#print "algovnfs = "
	num43= function(arr)
	#print str(num43)        
	algovnfs.append(num43)


	list1=[]
	contents=f44.read()
	arr=contents.split()
	arr = list(map(float, arr))
	#print "algonodes = "
	num44= function(arr) 
	#print str(num44)	
	algonodes.append(num44)
	


	list1=[]
	contents=f45.read()
	arr=contents.split()
	arr = list(map(float, arr))
	#print "algodelay = "
	num45= function(arr) 
	#print str(num45)	
	algodelay.append(num45)
	


        list1=[]
        contents=f46.read()
        arr=contents.split()
        arr = list(map(float, arr))
#       print "AIAdelay = "
#       print arr
        num46= function(arr)
#       print str(num15)        
        algothru_final.append(num46)























	xaxis.append(i)
#	print "\n\n\n\n\n\n\n\n"
	write_file=open("final_file.txt","w")
	write_file.write("AIAres = "+str(num11))
	write_file.write("\nAIAthru = "+str(num12))
	write_file.write("AIAvnfs = "+str(num13))
	write_file.write("\nAIAnodes = "+str(num14))
	write_file.write("\nAIAdelay = "+str(num15))



	write_file.write("\nSPHres = "+str(num21))
	write_file.write("\nSPHthru = "+str(num22))
	write_file.write("\nSPHvnfs = "+str(num23))
	write_file.write("\nSPHnodes = "+str(num24))
	write_file.write("\nSPHdelay = "+str(num25))



	write_file.write("\nGUSres = "+str(num31))
	write_file.write("\nGUSthru = "+str(num32))
	write_file.write("\nGUSvnfs = "+str(num33))
	write_file.write("\nGUSnodes = "+str(num34))
	write_file.write("\nGUSdelay = "+str(num35))

	write_file.write("\nalgores = "+str(num41))
	write_file.write("\nalgothru = "+str(num42))
	write_file.write("\nalgovnfs = "+str(num43))
	write_file.write("\nalgonodes = "+str(num44))
	write_file.write("\nalgodelay = "+str(num45))


#print str(AIAres[0][0])
#print str(AIAres[1][0])
#print str(AIAres[2])
#print str(AIAres[3])
#print str(AIAres[4])
print("Resource Used - (AIA, SPH, GUS, algo")
print str([pt[0] for pt in AIAres])
print str([pt[0] for pt in SPHres])
print str([pt[0] for pt in GUSres])
print str([pt[0] for pt in algores])
print("CI")
print str([pt[1] for pt in AIAres])
print str([pt[1] for pt in SPHres])
print str([pt[1] for pt in GUSres])
print str([pt[1] for pt in algores])

print str("\n\n Satisfaction Ratio")
print str([pt[0] for pt in AIAthru])
print str([pt[0] for pt in SPHthru])
print str([pt[0] for pt in GUSthru])
print str([pt[0] for pt in algothru])
print("CI")
print str([pt[1] for pt in AIAthru])
print str([pt[1] for pt in SPHthru])
print str([pt[1] for pt in GUSthru])
print str([pt[1] for pt in algothru])


print str("\n\n Number of VNFs used")
print str([pt[0] for pt in AIAvnfs])
print str([pt[0] for pt in SPHvnfs])
print str([pt[0] for pt in GUSvnfs])
print str([pt[0] for pt in algovnfs])
print("CI")
print str([pt[1] for pt in AIAvnfs])
print str([pt[1] for pt in SPHvnfs])
print str([pt[1] for pt in GUSvnfs])
print str([pt[1] for pt in algovnfs])

print str("\n\nNodes ")
print str([pt[0] for pt in AIAnodes])
print str([pt[0] for pt in SPHnodes])
print str([pt[0] for pt in GUSnodes])
print str([pt[0] for pt in algonodes])
print("CI")
print str([pt[1] for pt in AIAnodes])
print str([pt[1] for pt in SPHnodes])
print str([pt[1] for pt in GUSnodes])
print str([pt[1] for pt in algonodes])

print str("\n\nDelay ")

print str([pt[0] for pt in AIAdelay])
print str([pt[0] for pt in SPHdelay])
print str([pt[0] for pt in GUSdelay])
print str([pt[0] for pt in algodelay])
print("CI")
print str([pt[1] for pt in AIAdelay])
print str([pt[1] for pt in SPHdelay])
print str([pt[1] for pt in GUSdelay])
print str([pt[1] for pt in algodelay])
print str("\n\n")


print str("\n\n Throughput")
print str([pt[0] for pt in AIAthru_final])
print str([pt[0] for pt in SPHthru_final])
print str([pt[0] for pt in GUSthru_final])
print str([pt[0] for pt in algothru_final])
print("CI")
print str([pt[1] for pt in AIAthru_final])
print str([pt[1] for pt in SPHthru_final])
print str([pt[1] for pt in GUSthru_final])
print str([pt[1] for pt in algothru_final])

#plt.plot(AIAres,'bo')
#plt.plot(algores,'r--')
#plt.plot(SPHres,'k')
#plt.plot(GUSres,'g')

#plt.show()
# plt.plot(xaxis,[pt[0] for pt in AIAthru],'b')
# plt.plot(xaxis,[pt[0] for pt in algothru],'r')
# plt.plot(xaxis,[pt[0] for pt in SPHthru],'k')
# plt.plot(xaxis,[pt[0] for pt in GUSthru],'g')
# plt.legend(['AIA','algo','SPH','GUS'])
# plt.show()

