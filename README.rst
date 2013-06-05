=====================
PLoS Acceptance Times
=====================

See `the blog post <http://metarabbit.wordpress.com/2013/06/05/how-long-does-plos-take-to-review-a-paper-all-plos-journals-now/>`__

This was not really meant to be reusable, but here is how you generate the
plots::

    cd sources
    python downloaddata.py | sh -
    python getfulltext.py | sh -
    for d in data/*; do
        python statdates.py $d
    done

Yes, you pipe the Python scripts to ``sh -``


