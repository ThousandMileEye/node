#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid_simpleform import Form
from pyramid.httpexceptions import HTTPNotFound, HTTPOk

#
# JSON Validator
#
import jsonschema

#
# Sqlalchemy
#
import transaction
from pyramid_sqlalchemy import Session

#
# RESTsful API 用のコントローラー
#
class RESTsfulController(object):
	#
	# コンストラクタ
	#
	def __init__(self, model, filter = {}):
		#
		# モデル型の中から ID で指定された要素を検索
		#
		self._query = Session().query(model)
		self._query = self._query.filter_by(**filter)
		self._Model = model

	#
	# GET
	#
	def get(self, filter = {}):
		#
		# クエリの取得
		#
		query = self._query.filter_by(**filter)

		#
		# 要素を JSON のリストとして取得
		#
		elements = [element.to_dict() for element in query.all()]

		#
		# 要素リストを返す
		#
		return elements

	#
	# POST
	#
	def post(self, schema, data, unique_columns = []):
		#
		# JSONの書式確認
		#
		try:
			jsonschema.validate(data, schema)

		#
		# JSON内のデータ書式に問題がある場合
		#
		except jsonschema.ValidationError as e:
			return { 'error' : e.message }

		#
		# JSONの書式に問題がある場合
		#
		except ValueError:
			return { 'error' : 'Syntax error...' }

		#
		# 既存レコードとの重複確認するための辞書作成
		#
		unique_dict = {}
		for column in unique_columns:
			if column in data: unique_dict[column] = data[column]

		#
		# 既存レコードとの重複確認
		#
		if not len(unique_columns) == 0 \
			and not self._query.filter_by(**unique_dict).first() == None:
			return { 'error' : 'Record duplicated...' }

		#
		# トランザクションの開始
		#
		with transaction.manager:
			#
			# セッションの作成
			#
			session = Session()
			model = self._Model(**data)

			#
			# セッションに要素の追加
			#
			session.add(model)
			session.flush()

			#
			# 辞書として返す
			#
			return model.to_dict()

		#
		# HTTPOk
		#
		return HTTPOk()

#
# RESTful API 用のコントローラー
#
class RESTfulController(object):
	#
	# コンストラクタ
	#
	def __init__(self, idmap, model):
		#
		# モデル型の中から ID で指定された要素を検索
		#
		self._query = Session().query(model)
		self._filtered_query = self._query.filter_by(**idmap)

	#
	# GET
	#
	def get(self):
		#
		# 要素を ID から検索取得
		#
		element = self._filtered_query.first()

		#
		# 要素を発見できなかった場合の処理
		#
		if element == None: return HTTPNotFound()

		#
		# 要素を辞書として返す
		#
		return element.to_dict()

	#
	# PATCH
	#
	def patch(self, schema, data, unique_columns = []):
		#
		# 要素を ID から検索取得
		#
		element = self._filtered_query.first()

		#
		# 要素を発見できなかった場合の処理
		#
		if element == None: return HTTPNotFound()

		#
		# JSONの書式確認
		#
		try:
			jsonschema.validate(data, schema)

		#
		# JSON内のデータ書式に問題がある場合
		#
		except jsonschema.ValidationError as e:
			return { 'error' : e.message }

		#
		# JSONの書式に問題がある場合
		#
		except ValueError:
			return { 'error' : 'Syntax error...' }

		#
		# 既存レコードとの重複確認するための辞書作成
		#
		unique_dict = {}
		for column in unique_columns:
			if column in data: unique_dict[column] = data[column]

		#
		# 既存レコードとの重複確認
		# (DB内に既に指定されたカラムがあり、IDで検索したレコードでない場合は重複と判断する)
		#
		if not len(unique_columns) == 0 \
			and not self._query.filter_by(**unique_dict).first() == None \
			and self._filtered_query.filter_by(**unique_dict).first() == None:
			return { 'error' : 'Record duplicated...' }

		#
		# トランザクションの開始
		#
		with transaction.manager:
			self._filtered_query.update(data)

		#
		# 要素を辞書として返す
		#
		return self._filtered_query.first().to_dict()

	#
	# DELETE
	#
	def delete(self):
		#
		# 要素を ID から検索取得
		#
		element = self._filtered_query.first()

		#
		# 要素を発見できなかった場合の処理
		#
		if element == None: return HTTPNotFound()

		#
		# トランザクションの開始
		#
		with transaction.manager:
			#
			# 動画を削除
			#
			self._filtered_query.delete()

		#
		# HTTPOk
		#
		return HTTPOk()

