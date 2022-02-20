#First-in-First-Out Memory Manager Program

ref_string = []
my_list = []
def Add_page(val):
 print("ADDING PAGE:", val)

def display(val,counter, maxsize, arr):
 Add_page(val)
 for int in range(0, maxsize):
  print(int, ':', arr[int])

 print("PHYSICAL MEMORY")
 print("FRAME PAGE\n")
 print("PAGE# | STATUS | ADDRESS |")
 print("--------------------------")

 for i in range(0,8):
  if pagelist[i]>-1:status=1
  else: status=0
  print(i,"      ", status,"      ", pagelist[i])
 print('\n')
phem_list = []
clean_list = []
pagelist = []
for i in range(0,8):
    pagelist.append(-1)

count = 0
clean_indice = 4
tbp=0
fault=0


 #FUNCTIONS:
 #Element Add.
def element_add():

 Elem_count=input("ENTER NUMBER OF ELEMENTS IN REF STRING:  ")
 Elem_count = int(Elem_count)
 print("ENTER REF STRING(MANUALLY): ")
 for j in range(Elem_count):
     ref_item=input()
     my_list.append(ref_item)


#print(ref_string[0:Elem_count])
    #print(index)
print('****************************')
print('MAIN MENU')
print("ENTER 1) EXECUTE FIFO ALG ")
print("ENTER 2) QUIT ")
print('****************************')
choice=input("ENTER CHOICE: ")


while choice==1:
 element_add()
 for counter, value in enumerate(my_list):
  #load First 4 positions of FIFO Array without Duplicates
  if value not in phem_list:
    fault=fault+1
    if count<4:
     pagelist[value] = count
     phem_list.append(value)
     clean_list.append(value)
     display(value,count,len(phem_list) ,phem_list)
     count+=1
    else:
     print('REMOVE: ', phem_list[tbp])
     pagelist[value] = tbp
     #pagelist[value] phem_list[tbp]
     pagelist[phem_list[tbp]] = -1
     phem_list[tbp]=value #clean_list[tbp]=value
     tbp = (tbp + 1)%4
     display(value,count,len(phem_list) ,phem_list)
  elif value in phem_list: continue

 choice = int(choice)
 choice += 1

len_mylist=float(len(my_list))
print("FAULTS:",float(fault))
fault_rate=(fault/len_mylist)
print('FAULTS_RATE:' , str(fault_rate*100)+"%")
