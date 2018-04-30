# name,code,country,lat,lon,elev,style,rwdir,rwlen,freq,desc,userdata,pics

import csv
import simplekml
import sys,re
import pdb

inputfile = csv.reader(open (sys.argv[1], 'r'))
outputfile = sys.argv[1][:-4]+".kml"
#inputfile = csv.reader(open ("Test.cup", 'r'))
#outputfile = "Test.kml"
kml=simplekml.Kml()
style = simplekml.Style()
style.labelstyle.color = simplekml.Color.red  # Make the text red
#style.labelstyle.scale = 2  # Make the text twice as big
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png'

#pdb.set_trace()
for row in inputfile:
    if(row[0]=='name'):
        print("title row found")
    elif (len(row)==1):
        print ("end row found")
        break
    elif( len(row[4])==10):
        lat = float(row[3][0:2])+ float(row[3][2:8])/60
        if(row[3][8]=="S"):
            lat = lat*(-1)
        lon = float(row[4][0:3])+ float(row[4][3:9])/60
        if(row[4][9]=='W'):
            lon = lon*-1
        #now deal with the altitude    
        if (row[5].endswith('m')):
            height = int(float(row[5][0:len(row[5])-1]))
        elif(row[5].endswith('ft')):
            height = int(float(row[5][0:len(row[5])-2])* 0.3048 )
        pnt = kml.newpoint(name=row[0] + ' (' + str(height)+'m)', description= 'freq = ' + row[9]+ ': desc = ' + row[10],coords = [(lon, lat, height)])
        pnt.lookat.latitude = lat
        pnt.lookat.longitude = lon
        pnt.lookat.range = 5000
        pnt.lookat.heading = 0
        pnt.lookat.tilt = 30

        print(row[0],lon,lat, height)
       
    else:
        print ("Error incorrect length of co-ordinate", row[0])
print ("end of program")
kml.save(outputfile)
 
 

              

