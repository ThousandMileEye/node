#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config

#
# Bootstrap
#
def bootstrap(config):
	#
	# Include Template Engne
	#
	config.include('pyramid_jinja2')
	config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')

	#
	# Configure Static File Path
	#
	config.add_static_view(name='panels', path='web:v1/panels', cache_max_age=0)

	#
	# URL Mapping
	#
	config.add_route('WEB::V1:ADMIN', '/')
	config.scan('.controller')

#
# Public Package
#
__all__ = [bootstrap]

