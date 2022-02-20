#Final Project
#Operating Systems
#by Joshua Rigo

fhand=open('jobs.txt')
lines_list=[]
lines_list=fhand.readlines()

changed_list=[]
final_list=[]
frame_size=0

for line in lines_list:#takes '/n' out of list removes all leading or trailing spaces from string
    changed_list.append(line.strip())

frame_size=int(changed_list[0])
final_list=changed_list[1].split()#changes nested list item and loads it into one list.

def Add_page(val):  #Add page function
 print('ADDING PAGE: ', val)

def display(val,maxsize,arr):#Display Function
 Add_page(val)
 for int in range(0, maxsize):# For 0-maxsize execute & store 0-maxsize in int
  print(int, ':', arr[int])#print int & array[int] (arr(at index int))

 print('PHYSICAL MEMORY')
 print('FRAME PAGE\n')
 print("PAGE# | STATUS | ADDRESS |")
 print("--------------------------")
 for i in range(0,10): #For 0-9(which stands for the numbers the possible numbers in the frame) store
  if pagelist[i]>-1:status=1 #status update from 32 & 33
  else: status=0
  print(i,"        ", status,"        ", pagelist[i])
 print('\n')

phem_list = []
clean_list = []
pagelist = []


for i in range(0,10): #setting pagelist = -1
    pagelist.append(-1)

count = 0
tbp=0
fault=0

for i in range(0, len(final_list)): #set all items in final_list=ints makes value a valid index ln:57
    final_list[i] = int(final_list[i])

for counter, value in enumerate(final_list):#value stores each item. counter is the number of the loop                                              iter.
  if value not in phem_list: #if value not in frames it is a fault
   fault=fault+1
   if count<frame_size: #if frames are not completely full do the following
    pagelist[value] = count #update pagelist (ADDRESS COLUMN) with count value
    phem_list.append(value) #add value to frames
    display(value,len(phem_list),phem_list) #display function with new information
    count+=1
   else: #frames are full
    print('REMOVE: ', phem_list[tbp]) #remove frame
    pagelist[value] = tbp #Assigns new page a memory address in frame  page list at that value is (0-                                framesize)
    pagelist[phem_list[tbp]] = -1 #Assigns page thats been processed out -1
    phem_list[tbp]=value #places value inside of phem_list
    tbp = (tbp + 1)%frame_size #keeps returning the next index that needs to replaced in frame & starts                                   over at the beggining of frame
    display(value,len(phem_list) ,phem_list)
  elif value in phem_list: continue

#Fault & Fault_Rate Display
list_length = float(len(final_list))
#print('LIST LENGTH:', len(final_list)) #Length of final list prior to inserting frame_size
print("FAULTS:",float(fault))
fault_rate=(float(fault)/list_length)
print('FAULTS_RATE:' , str(fault_rate*100)+"%")
