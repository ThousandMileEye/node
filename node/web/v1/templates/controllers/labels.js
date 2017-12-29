
<script type='text/javascript'>
app.controller('LabelsController', ['$scope', '$filter', '$http', '$q', 'api', 'SharedDataService', function ($scope, $filter, $http, $q, api, SharedDataService) {
	var orderBy = $filter('orderBy');
	$scope.shared_data = SharedDataService;

	/*
	 * 取得
	 */
	$scope.gets = function() {
		return api.labels.gets($http).success(function(data, status, headers, config) {
			$scope.labels = data;
		});
	};

	/*
	 * 追加
	 */
	$scope.add = function(name, label_type_id) {
		console.log(name)
		console.log(label_type_id)

		return api.labels.add($http, name, label_type_id).success(function(data, status, headers, config) {
			$scope.gets();
		});
	};
}]);
</script>

