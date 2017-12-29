#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from eyed.client import BACnetClient

#
# 監視ジョブの取得
#
@view_config(route_name='api::v1:monitoring:rests', request_method='GET', renderer='json')
def gets(request):
    #
    # スケジューラー内のジョブを取得
    #
    jobs = []
    for job in request.registry.scheduler.get_jobs():
        jobs.append({
            'id'    : job.id,
            'name'  : job.name,
        })

    #
    # ジョブを JSON 形式で返す
    #
    return jobs

#
# 監視ジョブの登録
#
@view_config(route_name='api::v1:monitoring:test', request_method='GET', renderer='json')
def test(request):
    def my_func():
        import requests
        url = "http://127.0.0.1:8888/api/icmp/"
        print requests.post(url, json = {
		'uuid'	: '',
		'ip'	: '8.8.8.8',
	}).json()
    request.registry.scheduler.add_job(my_func, 'interval', seconds = 1)
    return {}

#
# 監視ジョブの登録
#
@view_config(route_name='api::v1:monitoring:bacnet_test', request_method='GET', renderer='json')
def bacnet_test(request):
	def my_func2():
		client = BACnetClient('localhost', '8888')
        	print client.ReadPropertyRequest(123, 2, 6, 85)
	request.registry.scheduler.add_job(my_func2, 'interval', seconds = 1)
	return {}

