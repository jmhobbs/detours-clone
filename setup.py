# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
	name='detours',
	version='1.0.1',
	description='Easy Hosts File Editor',
	author='John Hobbs',
	author_email='john@velvetcache.org',
	url='http://github.com/jmhobbs/detours-clone',
	py_modules=['detours'],
	package_dir = { '': 'lib' },
	scripts=['scripts/detoursd','scripts/detours-gtk','scripts/detours-http', 'scripts/detours-qt'],
	data_files=[
		( '/etc/init.d', ['assets/init.d/detoursd'] ),
		( '/etc', ['assets/detoursd.conf'] )
	]
)
