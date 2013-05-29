from lxml import etree
from datetime import date

def get_dates(ifile):
    et = etree.parse(ifile)
    d0,d1 = et.findall('//date')
    received = None
    accepted = None
    for d0 in et.findall('//date'):
        val = date(int(d0.findtext('year')), int(d0.findtext('month')), int(d0.findtext('day')))
        if d0.attrib['date-type'] == 'received':
            received = val
        elif d0.attrib['date-type'] == 'accepted':
             accepted = val
        else:
             print d0.attrib
    return received, accepted

for i in xrange(120):
    received, accepted = get_dates('data/output{}.xml'.format(i))
    print accepted - received
