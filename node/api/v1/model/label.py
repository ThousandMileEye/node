#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import BaseObject

#
# ラベル
#
class Label(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_LABEL'

	#
	# カラム定義
	#
	id		= Column('ID', Integer, primary_key=True)	# 識別子
	name		= Column('NAME', String)			# 名前
	label_type_id	= Column('LABEL_TYPE_ID', Integer, ForeignKey('M_LABEL_TYPE.ID')) # ラベル種別

	""" テーブル関係定義 """
	label		= relationship('LabelType')

	#
	# コンストラクタ
	#
	def __init__(self, name, label_type_id):
		self.name		= name
		self.label_type_id	= label_type_id

	#
	# 文字列化
	#
	def __str__(self):
		return '<Label name=%s>' %(self.name)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'	: self.id,
			'name'	: self.name
		}

#
# ラベル種別
#
class LabelType(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_LABEL_TYPE'

	#
	# カラム定義
	#
	id	= Column('ID', Integer, primary_key=True)	# 識別子
	name	= Column('NAME', String)			# 名前

	#
	# コンストラクタ
	#
	def __init__(self, name):
		self.name = name

	#
	# 文字列化
	#
	def __str__(self):
		return '<Label-Type name=%s>' %(self.name)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'	: self.id,
			'name'	: self.name
		}

