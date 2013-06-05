from os import mkdir, path


journals = [
    ('plosone' , 'PLoSONE',),
    ('ploscompbiol','PLoSCompBiol',),
    ('plosgenetics', 'PLoSGenetics',),
    ('plosbiology', 'PLoSBiology',),
    ('plosntds', 'PLoSNTD',),
    ('plospathogens', 'PLoSPathogens'),
    ('plosmedicine', 'PLoSMedicine'),
]

def retrieve_for(journal, slug):
    baseurl = 'http://www.{}.org/search/advanced?sort=Date%2C+newest+first&filterStartDate=2012-06-04T00%3A00%3A00Z&filterEndDate=2013-06-04T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage={}&filterJournals={}'.format(journal, '{}', slug)
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
    for j,base in journals:
        retrieve_for(j,base)
