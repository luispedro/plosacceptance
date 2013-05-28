from itertools import chain
import re

def xml_uri(info_doi):
    return 'http://www.plosone.org/article/fetchObjectAttachment.action?uri={}&representation=XML'.format(info_doi)

def get_uris(listf):
    pat = re.compile(r'href="http://www.plosone.org/article/(info.*);jsession')
    dois = set([mat.group(1) for mat in pat.finditer(open(listf).read())])
    return [xml_uri(d) for d in dois]

for i,f in enumerate(chain(*[get_uris('data/list{}.html'.format(i)) for i in xrange(10)])):
    print "wget --output-document=data/output{}.xml '{}'".format(i,f)
    print "sleep 1"

