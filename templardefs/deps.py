'''
dependencies for this project
'''

def populate(d):
    d.packs=[
        'libapache2-mod-php7.0',
        'php7.0',
        'php7.0-json',
        'php7.0-mysql',
        'php7.0-readline',
        'php7.0-cli',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
