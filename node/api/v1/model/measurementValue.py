#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from sqlalchemy.types import DateTime
from base import BaseObject
import uuid

#
# 計測値
#
class MeasurementValue(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_MEASUREMENT_VALUE'

	#
	# カラム定義
	#
	id		= Column('ID', String, primary_key=True)	# 識別子
	value		= Column('VALUE', String)			# 値
	datetime	= Column('DATETIME', DateTime, nullable=False)  # 日付
	config_id	= Column('CONFIG_ID', String, ForeignKey('M_MONITORING_CONFIGRATION.ID'))
	#monitoring_point_id	= Column('MONITORING_POINT_ID', String, ForeignKey('M_MONITORING_POINT.ID'))

	#
	# コンストラクタ
	#
	def __init__(self, config_id, value, datetime):
		self.id = str(uuid.uuid4())
		self.config_id = config_id
		self.datetime = datetime
		#self.monitoring_point_id = monitoring_point_id
		self.value = value

	#
	# 文字列化
	#
	def __str__(self):
		return '<MeasurementValue value=%s>' %(self.value)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'		: self.id,
			'config_id'	: self.config_id,
			'value'		: self.value
		}

