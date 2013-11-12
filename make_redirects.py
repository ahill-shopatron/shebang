#!/usr/bin/env python

# Reads in a CSV with source URLs in the first column, and destination URLs
# in the second column. Produces mod_rewrite rules on stdout.

def rewrite(src, dest):
    return 'RewriteRule ^{0}$ {1} [NC,QSA,R=301,L]'.format(src, dest)

if __name__ == '__main__':
    from urlparse import urlparse
    import argparse
    import csv

    def extract_path(url):
        return urlparse(url).path

    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    with open(args.infile, 'rb') as f:
        r = csv.reader(f)
        rules = (rewrite(extract_path(src)[1:], extract_path(dest))
                 for src, dest in r)

        for rule in rules:
            print rule
