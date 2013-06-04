from os import mkdir, path


journaldata = {
    #'plos1' : 'http://www.plosone.org/search/advanced?pageSize=12&sort=Date'
    #            '%2C+newest+first&filterStartDate=2013-04-28T00%3A00%3A00Z&'
    #            'filterEndDate=2013-05-28T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSONE',
    'ploscompbiol' : 'http://www.ploscompbiol.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2012-06-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSCompBiol',
    'plosgenetics': 'http://www.plosgenetics.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2012-06-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSGenetics',
    'plosbiology': 'http://www.plosbiology.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2012-06-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSBiology',
    'plosntds': 'http://www.plosntds.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2012-06-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals=PLoSNTD',
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
        outfile = "{}/list{}.html".format(outputdir, i)
        if not path.exists(outfile):
            print( 'wget "{}" --output-document="{}"'.format(fullurl, outfile))
            print('sleep 1')

if __name__ == '__main__':
    for j,base in journaldata.items():
        retrieve_for(j,base)
