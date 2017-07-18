/* Open and parse the data log with the following commented code that turns the log file into data Python data structures.
 *
 */
 
fileHandle=open('DDEC10 20321029.xls','r') #Opens the log file of interest
datalines=fileHandle.readlines() #reads the logfile contents into memory as a list
fileHandle.close()
#print(datalines[0:10]) #shows the first few entries in the list. These entries should match the log file

#Parse the log file and create data structure to hold the data for further processing
DLCs={} #Data length Code Dictionary that will be used to find all IDs.
timeList=[] #store the timestamp from the log file
IDList=[] #store the IDs in sequence
rawData=[] #Store the data fields in sequence

for line in datalines[3:]: #iterate through the entire file starting at line 3
    elements=line.split(',') #Separate the entries by commas

    timeList.append(float(elements[0])) #convert the first entry into a floating point number and add it to the list       
    
    ID=elements[7] #extract the text associated with the CAN identifier
    IDList.append(ID) #add the ID to a list       
    
    DLCText=elements[5].split(':') #The DLC text field has a colon, so separate the label from the text
    DLC=int(DLCText[1]) #Get the data length code as an integer
    DLCs[ID]=DLC #Store the DLC in a dictionary with the ID as a key. This will ensure only unique IDs are used as keys.
    
    rawData.append(elements[9:-1]) #store the data field as a list of text strings
  
IDs=DLCs.keys() #the keys in the DLCs dictionary are all the unique IDs that have not been duplicated.

print('\nID\tDLC') #Print the heading of a table with a preceding blank line
for ID in sorted(DLCs.keys()): #iterate through all the sorted dictionary keys
    print('%s\t%i' %(ID,DLCs[ID])) #display the dictionary contents
    
print('Number of Unique IDs: %i' %len(IDs)) #display the total number of messages
