#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

#
# Sqlalchemy
#
import transaction
from pyramid_sqlalchemy import Session
from api.v1.model import MeasurementValue

#
# ICMP PROTOCOL
#
def ping(uuid):
	#
	# トランザクションの開始
	#
	with transaction.manager:
		#session = Session()
		#session.add(MeasurementValue(uuid, '0.0', datetime.now()))
		print 'OK'

