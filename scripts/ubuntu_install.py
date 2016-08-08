#!/usr/bin/python3

'''
this script will install all the required packages that you need on
ubuntu to compile and work with this package.
'''

import subprocess # for check_call

packs=[
	'libapache2-mod-php7.0',
	'php7.0',
	'php7.0-json',
	'php7.0-mysql',
	'php7.0-readline',
	'php7.0-cli',
]

args=['sudo','apt-get','install','--assume-yes']
args.extend(packs)
subprocess.check_call(args)
