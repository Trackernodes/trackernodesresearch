# -*- coding: utf-8 -*-

import socket
import sys
import random
import time

def help():
	print "help:\n\t%s <slave id> <host> " % sys.argv[0]
	print '\tSlave Id = 0x00 to 0xF7'

	print '\n'
	print "Ej:\t%s 01 21*.***.***.211\n" % sys.argv[0]

	print 'nota: Ideal for test in devices \'Schneider Electric\'\n'

	exit(1)

try:
	SID 		= sys.argv[1]   # - SLAVE ID
	host 		= sys.argv[2]   # - Host with Modbus

except Exception, e:
	help()
	print '\n'+e

portModbus	= 502

class Colors:
    BLUE 		= '\033[94m'
    GREEN 		= '\033[32m'
    RED 		= '\033[0;31m'
    DEFAULT 	= '\033[0m'
    ORANGE 		= '\033[33m'
    WHITE 		= '\033[97m'
    BOLD 		= '\033[1m'
    BR_COLOUR 	= '\033[1;37;40m'

_modbus_exceptions = {  
						1: "Illegal function",							# 
						2: "Illegal data address",		   				# 
						3: "Illegal data value",  						# 
						4: "Slave device failure",						# 
						5: "Acknowledge", 								# 
						6: "Slave device busy", 						# 
						8: "Memory parity error", 						# 
						10: "Gateway path unavailable", 				# 
						11: "Gateway target device failed to respond"	# 
					}


_modbus_obj_description = {  
						0: "VendorName",	
						1: "ProductCode",	
						#2: "MajorMinorRevision",
						2: "Revision",		
						3: "VendorUrl",	
						4: "ProductName",	
						5: "ModelName",	
						#6: "UserApplicationName",
						6: "User App Name",
						7: "Reserved",	
						8: "Reserved",	
						9: "Reserved",	
						10: "Reserved",	
						128: "Private objects",
						255: "Private objects"		

}
# --MBAP 7 Bytes --------------------------------------------------------  #
# Return a string with the modbus header
def create_header_modbus(length,unit_id):
    trans_id = hex(random.randrange(0000,65535))[2:].zfill(4)
    proto_id = "0000"
    protoLen = length.zfill(4)
    unit_id = unit_id

    return trans_id + proto_id + protoLen + unit_id.zfill(2)

# mbap = create_header_modbus('4','1')


# Function Code 43 : "Read Device Identification"

func_code 	= '2b'  # Device Identification
meiType 	= '0e'  # MODBUS Encapsulated Interface - 0e / 0d
read_code	= '03'  # 01 / 02 / 03 / 04 
obj_id 		= '00' 


READ_CODE =  '''
		
		# var: read_code

		01 =>	'BASIC'			device identification (stream access)
		02 => 	'REGULAR 		device identification (stream access)
		03 => 	'EXTENDED' 		device identification (stream access)
		04 => 	'ESPECIFIC'     device identification (individual access)
	'''

modbusRequest = 	create_header_modbus('5',SID)

modbusRequest +=	func_code
modbusRequest += 	meiType
modbusRequest += 	read_code
modbusRequest += 	obj_id

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(100)

def iniConnection(h,p):

		client.connect((h,int(p)))

def getAllsIdObj(reqMD):


	try:
		iniConnection(host,portModbus)

	except Exception, e:
	 	print e
		sys.exit(0)
	
	# ------------------------------------------------------------------------------------
	
	request  = reqMD

	request2  = Colors.RED+request+Colors.DEFAULT

	client.send(request.decode('hex'))
	aResponse1 = client.recv(2048)
	
	#time.sleep(0.7) ###########################################################################


	resp = aResponse1.encode('hex')


	aframe  = resp
	print  Colors.BLUE+'Host: \t\t' +Colors.RED+host+Colors.DEFAULT
	print  Colors.BLUE+'Slave ID: \t' +Colors.RED+aframe[12:14]+Colors.DEFAULT

	respCode =  aframe[14:16]
	msg = ''

	'''
	Revisar esta condicion.

	ErrorFunctionCode = FunctionCode + 0x80

	respCode  =  ErroFunctionCode

	'''

	if respCode == 'ab':
		respCode = Colors.RED+respCode+Colors.DEFAULT
		errorCode = int(aframe[-2:],16)

		try:
			msgError = _modbus_exceptions[errorCode]
			msg = 'Exceptions['+str(errorCode)+']: '+msgError
		except:
			msg = 'Exceptions['+str(errorCode)+']'


		#print ' Function Code: \t'		+respCode + '\t'+msg

	totalObjs = aframe[26:28]
	firstObj = 28

	try:
		try:
			objTot = aframe[26:28]
			nObjeto = int(objTot,16)
		except:
			objTot = '0'
			nObjeto = int('0',10)

	

		print Colors.BLUE+'totalObj: \t'+Colors.RED+str(nObjeto)+Colors.DEFAULT
		print ''
		pInicial = 28

		for i in xrange(0,nObjeto):
			pInicial+=4
			longitud = aframe[pInicial-2:pInicial]
			longitud = int(longitud,16) 
				
						
			valueStr = aframe[pInicial:pInicial+longitud *2 ]

			try:
				obj_nm =_modbus_obj_description[i]
			except:
				obj_nm ='objName X'

			print Colors.GREEN+ obj_nm +': \t'+Colors.ORANGE+valueStr.decode('hex')+Colors.DEFAULT
			pInicial+=longitud*2
	
	except Exception, e:
			# print e
		print  Colors.BR_COLOUR+Colors.RED+'\nno device info' + Colors.DEFAULT
		print e
		print 'fail 2'
	
	client.close()


	print '--------------------------------------------------------------------------------------------'

def main():
	if len(sys.argv) != 3:
		help()
	else:
		getAllsIdObj(modbusRequest)

main()