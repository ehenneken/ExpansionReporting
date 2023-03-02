# ============================= LOGGING ======================================== #
LOGGING_LEVEL = 'INFO'
LOG_STDOUT = False
# ============================= ADS ============================================ #
ADS_API_TOKEN = "<secret>"
ADS_API_URL = "https://ui.adsabs.harvard.edu/v1"
CLASSIC_FULLTEXT_INDEX = "/tmp/all.links"
CLASSIC_USAGE_INDEX = {
    'reads':'/tmp/reads.links',
    'downloads':'/tmp/downloads.links'
}
ADS_REFERENCE_DATA = "/references/resolved"
# The root of the output location
OUTPUT_DIRECTORY = '/tmp/reports'
# ============================= APPLICATION ==================================== #
# 
# Collections we are reporting on
COLLECTIONS = ['AST', 'HP', 'PS', 'HP_AST', 'PS_AST', 'CORE']
# Report formats supported
FORMATS = ['NASA', 'CURATORS', 'MISSING']
# Report types supported
SUBJECTS = ['FULLTEXT', 'REFERENCES', 'SUMMARY']
# Which journals are we reporting on per collection
JOURNALS = {
    'AST': ['A&A','A&ARv','A&AS','AJ','AN','APh','ApJ','ApJL','ApJS','ARA&A','ARep','AsBio','AstL','CeMDA','FrASS','Galax','GeCoA','IAUS','IJAsB','JCAP','MNRAS','NatAs','PASA','PASJ','PASP','RAA','RNAAS','SCPMA','Univ','ASPC'],
    'PS': ["AREPS","ASTRA","AdSpR","AnGeo","Ap&SS","AsBio","CeMDA","E&PSL","EM&P","GeCoA","IJAsB","Icar","JAtS",
           "JGRA","JGRD","JGRE","M&PS","M&PSA","Metic","NatGe","P&SS","PEPI","RvGeo","SSRv","SoSyR","SoPh",
           "SpWea","PSJ","Moon","SpPol"],
    'HP': ['SoPh','SpWea'],
    'CORE': ['A&A','A&ARv','A&AS','AJ','AN','APh','ApJ','ApJL','ApJS','ARA&A','ARep','AsBio','ASPC','AstL',
    'CeMDA','FrASS','Galax','GeCoA','IAUS','IJAsB','JCAP','MNRAS','NatAs','PASA','PASJ','PASP','RAA','RNAAS',
    'SCPMA','Univ','ApOpt','ARPC','Chaos','Entrp','FrCh','JBO','JEI','JInst','NaPho','NatCC','NatCh','NatEn',
    'NatMa','NatNa','NatSR','NatSy','OExpr','OptEn','OptL','PCCP','PNAS','RScI','RSPTA','SciA','SPIE','NatCo',
    'Natur','Sci','AGUA','AmMin','AMT','AnGeo','ARMS','AtmEn','Atmos','AtmRe','BGeo','ChGeo','Clim','E&PSL',
    'EnGeo','EnST','ESRv','FrEaS','GeoJI','GeoRL','GGG','GMD','JAG','JASTP','JAtS','JGeod','JGRA','JGRB','JGRC',
    'JGRD','JGRE','JGRF','JGRG','NatGe','PApGe','PEPS','QJRMS','RemS','RvGeo','ScTEn','Senso','Tecto','Tectp',
    'EFM','ACP','AdSpR','Ap&SS','E&SS','EM&P','EP&S','ESC','ESSD','Icar','JSWSC','M&PS','Metic','Moon','P&SS',
    'PEPI','PSJ','SoPh','SoSyR','SpPol','SpWea','SSRv','AREPS','AIPC','AnPhy','AnRMS','ApPhA','ApPhB','ApPhL',
    'ApSS','ARCMP','ARNPS','ChPhC','ChPhL','CoPhC','CP','CPL','CQGra','EL','EPJA','EPJC','EPJD','EPJP','FlDyR',
    'FoPh','FoPhL','FrMat','FrP','GReGr','IJMPA','IJMPB','IJMPC','IJMPD','IJMPE','JAP','JChPh','JCoPh','JFM',
    'JHEP','JMoSp','JMoSt','JPCA','JPhA','JPhB','JPhD','JPhG','JPlPh','JQSRT','LRR','MPLA','MPLB','NatPh','NatRP',
    'NIMPA','NIMPB','NJPh','NuPhA','NuPhB','Parti','PDU','PhFl','PhLA','PhLB','PhPl','PhR','PhRvA','PhRvB','PhRvC',
    'PhRvD','PhRvE','PhRvF','PhRvL','PhRvP','PhRvR','PhRvX','PhyA','PhyB','PhyC','PPCF','PPN','PrPNP','PTEP','RPPh',
    'RvMP','ScPP','SSCom','SurSc','SurSR'],
    'HP_AST': ["ApJ","ApJL","ApJS","AJ","MNRAS","A&A","A&AS"],
    'PS_AST': ["ApJ","ApJL","ApJS","AJ","MNRAS","A&A","A&AS"]
}
# For some collection we define filters (to e.g. get the right content from multidisciplinary journals)
COLLECTION_FILTERS = {
    'HP_AST':'keyword:"sun*"',
    'PS_AST':'keyword:("planets*" OR meteor OR asteroid OR "celestial*" OR "solar system") -exoplanet -interstellar'
}
# Filtering to help us get recent content (i.e. entered in the past year)
CONTENT_QUERIES = {
    'HP':'{0} entdate:[NOW-365DAYS TO *]',
    'HP_AST':'{0} entdate:[NOW-365DAYS TO *]',
    'PS':'{0} entdate:[NOW-365DAYS TO *]',
    'PS_AST':'{0} entdate:[NOW-365DAYS TO *]',
    'AST':'{0} entdate:[NOW-365DAYS TO *]'
}
# For specific types of metadata, specify the sources we are considering
SOURCES = {
    'FULLTEXT': ['publisher','arxiv'],
    'REFERENCES': ['publisher', 'crossref']
}
# Column definitions for Summary Report
SUMMARY_COLUMNS = {
    "nrecs":"The current number of records in the collection being reported",
    "ftrecs":"How many of these records have full text associated/indexed with them?",
    "refrecs":"How many of these records are refereed?",
    "oarecs":"How many of these records are Open Access?",
    "dlrecs":"How many of these records have at least one data link?",
    "citnum":"The current total number of citations for these records",
    "recent_citnum":"How many citations have been added during the current year?",
    "reads":"The amount of ADS reads for these records",
    "recent_reads":"How many reads have been added during the current year?",
    "downloads":"The amount of ADS downloads for these records",
    "recent_downloads":"How many downloads have been added during the current year?"
}
# Row definitions for Summary Report
SUMMARY_ROWS = {
    "AST":"Core astronomy collection",
    "HP":"Core heliophysics collection",
    "PS":"Core Planetary Science collection",
    "HP_AST":"Heliophysics content in main astronomy journals (filter: keyword:'sun*')",
    "PS_AST":"Planetary Science content in main astronomy journals (filter: keyword:('planets*' OR meteor OR asteroid OR 'celestial*' OR 'solar system') -exoplanet -interstellar)",
    "AST recent sample":"Core Astronomy collection including references and citations, filtered on entry date (entdate:[NOW-365DAYS TO *])",
    "HP recent sample":"Core Heliophysics collection including references and citations, filtered on entry date (entdate:[NOW-365DAYS TO *])",
    "HP_AST recent sample":"Heliophysics in Main Astronomy collection including references and citations, filtered on entry date (entdate:[NOW-365DAYS TO *])",
    "PS recent sample":"Core Planetary Science collection including references and citations, filtered on entry date (entdate:[NOW-365DAYS TO *])",
    "PS_AST recent sample":"Planetary Science in Main Astronomy collection including references and citations, filtered on entry date (entdate:[NOW-365DAYS TO *])",
}
# For these collections we need to skip the calculation of usage
# (because it would involve retrieving all bibcodes)
SKIP_USAGE = ['HP_AST', 'PS_AST']
# For these publications (bibstem) the volume is treated as volume. This dictionary lists the start year
YEAR_IS_VOL = {
    'JCAP':2003
}
# Specification of volume ranges where coverage should not be calculated
# Example: for some volumes there will be no full text (the publisher does not have it
#          and the ADS will not digitize)
NO_FULLTEXT = {
    'AnGeo': '1-13',
    'SoSyR': '1-36',
    'SoPh': '101',
}

