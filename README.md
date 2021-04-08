Apache Fundraising Website
====================

## How to build the Site
This builds the website and puts pages in output/

    `virtualenv $venvname`
    `source $venvname/bin/activate`
    `pip install -r requirements.txt`
    Edit all the markdown! (pages/)
    `pelican content`

To preview:

    `python -m pelican.server`

## Technical site documentation

Fundraising site default copied from default Apache Infra future website:
https://github.com/apache/infrastructure-website

http://docs.getpelican.com/en/stable/content.html#articles-and-pages

Anytime you checkin a file, the site is regenerated:
https://ci.apache.org/builders/fundraising-site

## User notes
Users must be [set up on gitbox](https://gitbox.apache.org/setup/)
