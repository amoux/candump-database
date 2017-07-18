# candump-database
Using a Database to Decode J1939 Messages

Python script written to decode a CAN data dump from a J1939 Network. The goal of the program is to decode messages on the J1939 communications bus present in the vehicle.

Assumptions:

The reader knows about J1939. In a nut shell, J1939 is a standard created by the Society of Automotive Engineers that standardizes serial communications between electronic control units in commercial vehicles. J1939 uses a Controller Area Network (CAN) at 250kbps.

The reader understands that the same number can be written in different bases. We will be using decimal (base 10), hexadecimal (base 16), and binary (base 2) when discussing messages. Converting between bases is quite simple with the built-in Windows calculator in programmer mode. For example, 0xFEF1 is the hexadecimal number for 65265, as shown below.
