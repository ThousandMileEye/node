#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, BOOLEAN
from base import BaseObject
import uuid

#
# 監視ポイント設定
#
class MonitoringConfiguration(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_MONITORING_CONFIGRATION'

	#
	# カラム定義
	#
	id		= Column('ID', String, primary_key=True)	# 識別子
	config		= Column('CONFIG', String)			# 設定情報
	enable		= Column('ENABLE', BOOLEAN)			# 設定有効化
	interval	= Column('INTERVAL', Integer)			# 監視頻度

	#
	# コンストラクタ
	#
	def __init__(self, config, enable = True, interval = 60):
		self.id = str(uuid.uuid4())	# 識別子
		self.config = config		# 監視設定情報
		self.enable = enable		# 監視設定の有効化
		self.interval = interval	# 監視頻度

	#
	# 文字列化
	#
	def __str__(self):
		return '<MonitoringConfiguration interval=%s>' %(self.interval)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'		: self.id,
			'config'	: self.config,
			'enable'	: self.enable,
			'interval'	: self.interval,
		}

