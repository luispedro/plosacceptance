from os import mkdir


journaldata = {
    #'plos1' : 'http://www.plosone.org/search/advanced?pageSize=12&sort=Date'
    #            '%2C+newest+first&filterStartDate=2013-04-28T00%3A00%3A00Z&'
    #            'filterEndDate=2013-05-28T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSONE',
    'ploscb' : 'http://www.ploscompbiol.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2013-05-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSCompBiol',
    'plosgen': 'http://www.plosgenetics.org/search/advanced;jsessionid=BADC342F94563D2D30B0643156770E46?sort=Date%2C+newest+first&filterStartDate=2013-05-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSGenetics',
    'plosbio': 'http://www.plosbiology.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2013-05-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSBiology',
    'plosntd': 'http://www.plosntds.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2013-05-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSNTD',
}


def retrieve_for(journal, baseurl):
    outputdir = 'data/{}'.format(journal)
    try:
        mkdir('data')
    except:
        pass
    try:
        mkdir(outputdir)
    except:
        pass

    for i in range(30):
        fullurl = baseurl.format(i)
        print( 'wget "{}" --output-document="{}/list{}.html"'.format(fullurl, outputdir, i))
        print('sleep 1')

if __name__ == '__main__':
    for j,base in journaldata.items():
        retrieve_for(j,base)
