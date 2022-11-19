import pybliometrics
# c1a9a0aa724682d53a7883b3db11644b
pybliometrics.scopus.utils.create_config()

from pybliometrics.scopus import AffiliationRetrieval
aff1 = AffiliationRetrieval(60032057)
aff1.author_count