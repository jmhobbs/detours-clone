# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
	name='detours',
	version='1.0',
	description='Easy Hosts File Editor',
	author='John Hobbs',
	author_email='john@velvetcache.org',
	url='http://github.com/jmhobbs/detours-clone',
	py_modules=['detours'],
	scripts=['detoursd','detours-gtk','detours-http'],
	data_files=[
		( '/etc/init.d', ['init.d/detoursd'] ),
		( '/etc', ['detoursd.conf'] )
	]
)