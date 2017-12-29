
<script type='text/javascript'>
app.constant('api', {
	/*
	 * 監視ポイント
	 */
	points : {
		/*
		 * 追加
		 */
		add : function($http, name) {
			return $http({
				method	: 'POST',
				url     : "{{ request.route_path('api::v1:monitoringPoints:rest') }}",
				data	: {
					'name' : name,
				}
			})
		},

		/*
		 * 取得
		 */
		gets : function($http) {
			return $http({
				method  : "GET",
				url     : "{{ request.route_path('api::v1:monitoringPoints:rest') }}",
			})
		},
	},
	/*
	 * ラベル
	 */
	labels : {
		/*
		 * 追加
		 */
		add : function($http, name, label_type_id) {
			return $http({
				method	: 'POST',
				url     : "{{ request.route_path('api::v1:labels:rest') }}",
				data	: {
					'name'		: name,
					'label_type_id'	: label_type_id,
				}
			})
		},
		/*
		 * 取得
		 */
		gets : function($http) {
			return $http({
				method  : "GET",
				url     : "{{ request.route_path('api::v1:labels:rest') }}",
			})
		},
	},
	/*
	 * ラベル種別
	 */
	label_types : {
		/*
		 * 追加
		 */
		add : function($http, name) {
			return $http({
				method	: 'POST',
				url     : "{{ request.route_path('api::v1:label_types:rest') }}",
				data	: {
					'name' : name,
				}
			})
		},
		/*
		 * 取得
		 */
		gets : function($http) {
			return $http({
				method  : "GET",
				url     : "{{ request.route_path('api::v1:label_types:rest') }}",
			})
		},
	},
});
</script>

