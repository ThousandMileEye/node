#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults
from pyramid.response import Response

#
# RESTfulController
#
from api.v1.common.rest import RESTfulController, RESTsfulController

#
# Model
#
from api.v1.model import MonitoringPoint

#
# オブジェクト全数の取得
#
@view_defaults(route_name='api::v1:monitoringPoints:rest', renderer='json')
class PointsController(RESTsfulController):
	#
	# コンストラクタ
	#
	def __init__(self, request):
		RESTsfulController.__init__(self, MonitoringPoint)
		self.request = request

	#
	# GET
	#
	@view_config(request_method='GET')
	def get(self):
		return RESTsfulController.get(self)

	#
	# POST
	#
	@view_config(request_method = 'POST')
	def post(self):
		#
		# 新規仕様書登録用の書式定義
		#
		schema = {
			'type'          : 'object',
				'properties'	: {
				'name'		: {
					'type'		: 'string',
					'minLength'	: 2,
				},
			},
			'required'	: ['name']
		}

		#
		# データセンターの作成
		#
		return RESTsfulController.post(self, schema, self.request.json_body, unique_columns = [])

#
# 単数オブジェクトの取得
#
#@view_defaults(route_name='api::v1:issue:rest', renderer='json')
#class IssueController(RESTfulController):
#	#
#	# コンストラクタ
#	#
#	def __init__(self, request):
#		RESTfulController.__init__(self, {
#			'id' : request.matchdict['id']
#		}, Issue)
#		self.request = request
#
#	#
#	# GET
#	#
#	@view_config(request_method='GET')
#	def get(self):
#		return RESTfulController.get(self)


