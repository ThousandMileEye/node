#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config

#
# Bootstrap
#
def bootstrap(config):
	#
	# URL Mapping
	#
	config.add_route('api::v1:units:rest', '/')
	config.scan('.controller')

#
# Public Package
#
__all__ = [bootstrap]

