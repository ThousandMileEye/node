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
from api.v1.model import LabelType

#
# ラベル種別
#
@view_defaults(route_name='api::v1:label_types:rest', renderer='json')
class LabelTypesController(RESTsfulController):
	#
	# コンストラクタ
	#
	def __init__(self, request):
		RESTsfulController.__init__(self, LabelType)
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
		# 新規登録用の書式定義
		#
		schema = {
			'type'          : 'object',
				'properties'	: {
				'name'		: {
					'type'		: 'string',
				},
			},
			'required'	: ['name']
		}

		#
		# データセンターの作成
		#
		return RESTsfulController.post(self, schema, self.request.json_body, unique_columns = [])

#
# Issue の取得
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

