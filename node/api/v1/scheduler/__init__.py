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
    config.add_route('api::v1:monitoring:rests', '/')
    config.add_route('api::v1:monitoring:test', '/test')
    config.add_route('api::v1:monitoring:bacnet_test', '/bacnet_test')
    config.scan('.controller')

#
# Public Package
#
__all__ = [bootstrap]

