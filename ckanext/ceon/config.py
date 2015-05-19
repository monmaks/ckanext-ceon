#!/usr/bin/python
# vim: set fileencoding=utf-8

from logging import getLogger

from pylons import config
from paste.deploy.converters import asbool


DOI_TEST_PREFIX = '10.5072'
DOI_ENDPOINT = 'https://mds.datacite.org'
DOI_TEST_ENDPOINT = 'https://test.datacite.org/mds'

def get_doi_prefix():
    return DOI_TEST_PREFIX if asbool(config.get("ckanext.ceon.doi_test_mode", True)) else config.get("ckanext.ceon.doi_prefix")
    
def get_doi_endpoint():
    return DOI_TEST_ENDPOINT if asbool(config.get("ckanext.ceon.doi_test_mode", True)) else DOI_ENDPOINT


