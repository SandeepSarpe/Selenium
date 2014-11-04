__author__ = 'sandeeps'

import time

class ExpetcedChargesTime:

    def expectedTime(self,record):
        a = time.strptime(record[2]+'T'+record[1]+'Z', '%m/%d/%YT%H:%MZ')
        b = time.strptime(record[4]+'T'+record[3]+'Z', '%m/%d/%YT%H:%MZ')
        a = time.mktime(a)
        b = time.mktime(b)
        diff = b - a
        days = int(diff) / 86400
        hours = int(diff) / 3600 % 24
        minutes = int(diff) / 60 % 60
        diffdisplay =  '(' +str(days)+' Days, '+str(hours)+' Hours, '+str(minutes)+' Minutes)'
        thours =  (days * 24 + hours + abs(minutes/60))

        if record[0] == 'Short-Term Parking':
            pcharge = thours * 2
        elif record[0] == 'Economy Parking':
            pcharge = thours * 4
        elif record[0] == 'Long-Term Surface Parking':
            pcharge = thours * 2
        elif record[0] == 'Long-Term Garage Parking':
            pcharge = thours * 2
        elif record[0] == 'Valet Parking':
            pcharge = thours * 12

        return diffdisplay,'$ ' + str("%.2f" % pcharge)

    '''def expectedCharges(self,record):
        diff, thours = self.expectedTime(record)
        if record[0] == 'Short-Term Parking':
            pcharge = thours * 2
        elif record[0] == 'Economy Parking':
            pcharge = thours * 4
        elif record[0] == 'Long-Term Surface Parking':
            pcharge = thours * 2
        elif record[0] == 'Long-Term Garage Parking':
            pcharge = thours * 2
        elif record[0] == 'Valet Parking':
            pcharge = thours * 12

        return '$ ' + str("%.2f" % pcharge)'''





