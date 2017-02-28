MODBUS TOOLS
=============

# TOOLS:
Modbus device info V 0.2.1
---------------------------
Features
+ python: 			v2.7 
+ appName: 			mbusDevInfo-v0.2.1.py
+ Defaulth port: 	502
+ Protocol: 		Modbus/tcp
+ Function Code: 	0x5a

+ Ideal for device of vendor 'Scheider Electric'

RUN
> python mbusDevInfo-v0.2.1.py [SID] [HOST] 
  Slave Id = 0x00 to 0xF7

FORMAT OUTPUT

	Host: 			217.***.***.3
	Slave ID: 		00
	totalObj: 		9

	VendorName: 	00010000
	ProductCode: 	002
	Revision: 		10-98-00
	VendorUrl: 		03-20-00
	ProductName: 	01-14-00
	ModelName: 		17/02/2017 02:38
	User App Name: 	03/06/2015 09:12 
	Reserved: 		16/02/2017 15:35 
	Reserved: 		20/11/15,11:25:12,2,SU,Modification CA

********************************************************************
	Host: 			94.**.*.2*0
	Slave ID: 		01
	totalObj: 		8

	VendorName: 	Schneider Electric
	ProductCode: 	XBTGT6340
	Revision: 		V6.1.4.705
	VendorUrl: 		www.schneider-electric.com
	ProductName: 	Magelis
	ModelName: 		XBTGT6340
	User App Name: 	Pergola_11OTT2016/Office
	Reserved: 		A15

********************************************************************
	Host: 			188.**.***.150
	Slave ID: 		00
	totalObj: 		7

	VendorName: 	Schneider Electric
	ProductCode: 	(EAN13)3303430597803
	Revision: 		V8.02
	VendorUrl: 		www.schneider-electric.com
	ProductName: 	Sepam serie 40
	ModelName: 		S50 - Substation
	User App Name: 	CM_BALAZOTE 

********************************************************************

PENDING 
+ clear code \ fix code
+ Add Function Code: 0x5a
+ add formats output: xml, csv, json

---------------------------------------------
[Bertin Jose ](https://twitter.com/bertinjoseb)
 @bertinjoseb

[Ezequiel Fernandez](https://twitter.com/capitan_alfa)
 @capitan_alfa
