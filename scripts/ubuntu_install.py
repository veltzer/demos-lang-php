#!/usr/bin/python3

'''
this script will install all the required packages that you need on
ubuntu to compile and work with this package.
'''

import subprocess # for check_call

packs=[
	'libapache2-mod-php5',
	'php5',
	'php5-json',
	'php5-mysql',
	'php5-readline',
	'php5-cli',
]

args=['sudo','apt-get','install','--assume-yes']
args.extend(packs)
subprocess.check_call(args)
