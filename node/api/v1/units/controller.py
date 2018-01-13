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
from api.v1.model import Unit

#
# データ型の定義
#
@view_defaults(route_name='api::v1:units:rest', renderer='json')
class UnitsController(RESTsfulController):
	#
	# コンストラクタ
	#
	def __init__(self, request):
		RESTsfulController.__init__(self, Unit)
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
				'type'		: {
					'type'		: 'string',
				},
			},
			'required'	: ['name', 'type']
		}

		#
		# データセンターの作成
		#
		return RESTsfulController.post(self, schema, self.request.json_body, unique_columns = [])

if __name__ == '__main__':
	UnitsController()

