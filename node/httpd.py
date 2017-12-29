#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# WEB Server & WEB Application Framework
#
from waitress import serve
from pyramid.config import Configurator

#
# Job Scheduler
#
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

#
# Entry Point
#
if __name__ == '__main__':
    #
    # 設定の読み込み
    #
    config = Configurator()

    #
    # ライブラリの読み込み
    #
    config.add_settings({
        'sqlalchemy.url' : 'sqlite:///../tuntunkun.db'
    })
    config.include('pyramid_sqlalchemy')

    #
    # スケジューラの設定
    #
    config.registry.scheduler = BackgroundScheduler({
        #
        # スレッドプールの設定
        #
        'apscheduler.executors.default' : {
            'class'         : 'apscheduler.executors.pool:ThreadPoolExecutor',
            'max_workers'   : '256'
        },
        'apscheduler.job_defaults.coalesce'         : 'false',
        'apscheduler.job_defaults.max_instances'    : '128',
        'apscheduler.timezone'                      : 'UTC',
    })

    #
    # スケジューラの開始
    #
    config.registry.scheduler.start()

    #
    # API の マッピング
    #
    #import api.v1.scheduler
    #config.include(api.v1.scheduler.bootstrap, route_prefix='/api/v1/scheduler')
    import api.v1
    config.include(api.v1.bootstrap, route_prefix='/api/v1')

    #
    # WEB の マッピング
    #
    import web.v1
    config.include(web.v1.bootstrap, route_prefix='/')

    #
    # HTTPDサーバの設定と起動
    #
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=8000)

