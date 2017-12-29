#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, BOOLEAN
from base import BaseObject
import uuid

#
# 監視ポイント
#
class MonitoringPoint(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_MONITORING_POINT'

	#
	# カラム定義
	#
	id	= Column('ID', String, primary_key=True)	# 識別子
	name	= Column('NAME', String)			# 名前

	#
	# コンストラクタ
	#
	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name

	#
	# 文字列化
	#
	def __str__(self):
		return '<MonitoringPoint name=%s>' %(self.name)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'	: self.id,
			'name'	: self.name
		}

