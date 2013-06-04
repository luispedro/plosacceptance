from os import mkdir

try:
    mkdir('data')
except:
    pass

baseurl= 'http://www.plosone.org/search/advanced?pageSize=12&sort=Date%2C+newest+first&filterStartDate=2013-04-28T00%3A00%3A00Z&filterEndDate=2013-05-28T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSONE'

for i in range(30):
    fullurl = baseurl.format(i)
    print( 'wget {} --output-document="data/list{}.html"'.format(fullurl, i))
    print('sleep 1')
