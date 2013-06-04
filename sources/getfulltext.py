from itertools import chain
import re

journaldata = {
    'plos1' :  'plosone',
    'ploscb' : 'ploscompbiol',
    'plosgen': 'plosgenetics',
    'plosbio': 'plosbiology',
    'plosntd': 'plosntds',
}



def get_uris(hostname, listf):
    def xml_uri(info_doi):
        return 'http://www.{}.org/article/fetchObjectAttachment.action?uri={}&representation=XML'.format(hostname,info_doi)
    pat = re.compile(r'href="http://www.{}.org/article/(info.*);jsession'.format(hostname))
    dois = set([mat.group(1) for mat in pat.finditer(open(listf).read())])
    return [xml_uri(d) for d in dois]

for journal, hostname in journaldata.items():
    for i,f in enumerate(chain(*[get_uris(hostname, 'data/{}/list{}.html'.format(journal, i)) for i in xrange(30)])):
        print "wget --output-document=data/{}/output{}.xml '{}'".format(journal, i,f)
        print "sleep 1"

