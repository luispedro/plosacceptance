from scipy import stats
from mpltools import style
from matplotlib import pyplot as plt
import numpy as np
from lxml import etree
from datetime import date
from glob import glob
from sys import argv

def get_dates(ifile):
    et = etree.parse(ifile)
    dates = et.findall('//date')
    if len(dates) == 0:
        return None
    d0,d1 = dates
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

if len(argv) < 2:
    print 'Argument needed'

basedir = argv[1]
journal = basedir[len('data/'):]

deltas = []
for f in glob(basedir+'/*.xml'):
    dates = get_dates(f)
    if dates is not None:
        received, accepted = dates
        delta = accepted - received
        deltas.append(delta.days)
deltas = np.array(deltas)

style.use('ggplot')
gc = stats.kde.gaussian_kde(deltas)
c = gc(np.arange(800)) * len(deltas)

plt.hist(deltas,np.arange(802), color='k')
plt.plot(c, lw=8)
plt.xlabel('Nr days')
plt.ylabel("Papers (N={})".format(len(deltas)))
avg = np.mean(deltas)
median = np.median(deltas)
std = np.std(deltas)
mode = c.argmax()
plt.text(240,4,"Average is {} (std: {})\nMedian is {}\nMode (of KDE fit) is {}".format(int(avg),int(std),median,mode), fontdict={'size':24})
plt.savefig('stataccept-{}.png'.format(journal))

