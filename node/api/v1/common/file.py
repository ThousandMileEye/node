#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid_simpleform import Form
from pyramid.httpexceptions import HTTPNotFound, HTTPOk
from pyramid.response import Response

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
# File 操作用のコントローラー
#
class FileController:
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
	# GET (ダウンロード処理)
	#
	def get(self):
		#
		# UUIDからファイルを取得
		#
		file = self._filtered_query.first()
		if file == None: return HTTPNotFound()

		#
		# ファイルをダウンロードさせる
		#
		return Response(
			#content_type='application/force-download',
			content_disposition='attachment; filename=%s' % (file.name),
			content_encoding='binary',
			content_length=len(file.data),
			body=file.data,
		)

	#
	# POST (アップロード処理)
	#
	def post(self, schema, data):
		#
		# ファイルアップロード用のスキーマ
		#
		form = Form(data, schema = schema)
		if form.validate():
			#
			# トランザクションの開始
			#
			with transaction.manager:
				#
				# セッションの作成
				#
				session = Session()

				#
				# ファイル名、ファイルのデータ取得
				#
				storage = form.request.params.getone('file')
				model = self._Model(**{
					'name'  : storage.filename,
					'data'  : storage.file.read(),
				})

				#
				# セッションに要素の追加
				#
				session.add(model)

				#
				# 登録
				#
				session.flush()

				#
				# 辞書として返す
				#
				return model.to_dict()

		#
		# 失敗した場合の処理
		#
		return HTTPNotFound()

