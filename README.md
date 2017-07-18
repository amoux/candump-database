# candump-database
Using a Database to Decode J1939 Messages

Python script written to decode a CAN data dump from a J1939 Network. The goal of the program is to decode messages on the J1939 communications bus present in the vehicle.

Assumptions:

The reader knows about J1939. In a nut shell, J1939 is a standard created by the Society of Automotive Engineers that standardizes serial communications between electronic control units in commercial vehicles. J1939 uses a Controller Area Network (CAN) at 250kbps.

The reader understands that the same number can be written in different bases. We will be using decimal (base 10), hexadecimal (base 16), and binary (base 2) when discussing messages. Converting between bases is quite simple with the built-in Windows calculator in programmer mode. For example, 0xFEF1 is the hexadecimal number for 65265, as shown below.

# Importing the data
The python script should turn the log file into Python data structures.
  This code should produce the following output:
*Example  8 
18ffa53d	8
18ffaa01	8
18ffab01	8
18ffac01	8
1ce8ff00	8
1cebff00	8
1cebff0f	8
1cecff00	8
1cecff0f	8
1cfe9201	8
cf00300	8
cf00400	8
cf00421	8
cf00a01	8
Number of Unique IDs: 108

*Now the data is in Python data structures within memory. The next step is to make meaning from it using the J1939 Standard.

#Parsing the data
There are two things that are needed to make meaning of the data. First, a set of rules that tell us how to decode the information, and second, the logic to do so. We'll start with the rules (standards) to decode the data.
