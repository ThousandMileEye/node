#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults
from pyramid.response import Response

#
# 監視ジョブの取得
#
@view_config(route_name='WEB::V1:ADMIN', renderer='./templates/index.html')
def gets(request):
    return {}

