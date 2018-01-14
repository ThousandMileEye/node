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
from api.v1.model import MonitoringConfiguration

#
# オブジェクト全数の取得
#
@view_defaults(route_name='api::v1:monitoringConfigurations:rest', renderer='json')
class ConfigurationsController(RESTsfulController):
	#
	# コンストラクタ
	#
	def __init__(self, request):
		RESTsfulController.__init__(self, MonitoringConfiguration)
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
				'config'	: {
					'type'		: 'string',
					'minLength'	: 2,
				},
				'enable'	: {
					'type'		: 'boolean',
				},
				'interval'	: {
					'type'		: 'integer',
				},
			},
			'required'	: ['config']
		}

		#
		# 監視設定の登録
		#
		config = RESTsfulController.post(self, schema, self.request.json_body, unique_columns = [])
		print config

		from module import ping
		self.request.registry.scheduler.add_job(ping, 'interval', args = [config['id']], seconds = 30)

		return config

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


