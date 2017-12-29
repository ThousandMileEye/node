#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config

import monitoringPoints
import labels
import label_types

#
# Bootstrap
#
def bootstrap(config):
	#
	# URL Mapping
	#
	#config.add_route('API::V1:MONITORING:RESTS', '/')
	#config.add_route('API::V1:MONITORING:TEST', '/test')
	#config.scan('.controller')

	config.include(monitoringPoints.bootstrap, route_prefix='/monitoringPoints/')
	config.include(labels.bootstrap, route_prefix='/labels/')
	config.include(label_types.bootstrap, route_prefix='/label_types/')

	pass

#
# Public Package
#
__all__ = [bootstrap]

