from scipy import stats
from mpltools import style
from matplotlib import pyplot as plt
import numpy as np
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

deltas = []
for i in xrange(360):
    received, accepted = get_dates('data/output{}.xml'.format(i))
    delta = accepted - received
    deltas.append(delta.days)

deltas = np.array(deltas)

style.use('ggplot')
gc = stats.kde.gaussian_kde(deltas)
c = gc(np.arange(800)) * len(deltas)

plt.hist(deltas,np.arange(802))
plt.plot(c, lw=8)
plt.xlabel('Nr days')
plt.ylabel("Papers (N=360)")
avg = np.mean(deltas)
median = np.median(deltas)
std = np.std(deltas)
mode = c.argmax()
plt.text(240,4,"Average is {} (std: {})\nMedian is {}\nMode (of KDE fit) is {}".format(int(avg),int(std),median,mode), fontdict={'size':24})
plt.savefig('stataccept.png')

