for spage in `seq 0 29`; do
    wget 'http://www.plosone.org/search/advanced?pageSize=12&sort=Date%2C+newest+first&filterStartDate=2013-04-28T00%3A00%3A00Z&filterEndDate=2013-05-28T23%3A59%3A59Z&unformattedQuery=*%3A*&startPage='$seq'&filterJournals=PLoSONE' --output-document="list${spage}.html"
    sleep 1
done
