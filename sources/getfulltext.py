from os import path
from itertools import chain
import re

journals = [
#   'plos1' :  'plosone',
    'ploscompbiol',
    'plosgenetics',
    'plosbiology',
    'plosntds',
]



def get_uris(journal, listf):
    def xml_uri(info_doi):
        return 'http://www.{}.org/article/fetchObjectAttachment.action?uri={}&representation=XML'.format(journal,info_doi)
    pat = re.compile(r'href="http://www.{}.org/article/(info.*);jsession'.format(journal))
    dois = set([mat.group(1) for mat in pat.finditer(open(listf).read())])
    return [xml_uri(d) for d in dois]

for journal in journals:
    for i,f in enumerate(chain(*[get_uris(journal, 'data/{}/list{}.html'.format(journal, i)) for i in xrange(30)])):
        outfile = "data/{}/output{}.xml".format(journal, i)
        if not path.exists(outfile):
            print "wget --output-document={} '{}'".format(outfile,f)
            print "sleep 1"

