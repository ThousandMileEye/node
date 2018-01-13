#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import BaseObject
import uuid

#
# ラベル
#
class Unit(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_UNIT'

	#
	# カラム定義
	#
	id	= Column('ID', String, primary_key=True)	# 識別子
	name	= Column('NAME', String, unique=True)		# 名前
	type	= Column('TYPE', String)			# 型

	#
	# コンストラクタ
	#
	def __init__(self, name, type):
		self.id = str(uuid.uuid4())
		self.name = name
		self.type = type

	#
	# 文字列化
	#
	def __str__(self):
		return '<Unit name=%s, type=%s>' %(self.name, self.type)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'	: self.id,
			'name'	: self.name,
			'type'	: self.type
		}

