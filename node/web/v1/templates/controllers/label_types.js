
<script type='text/javascript'>
app.controller('LabelTypesController', ['$scope', '$filter', '$http', '$q', 'api', 'SharedDataService', function ($scope, $filter, $http, $q, api, SharedDataService) {
	var orderBy = $filter('orderBy');
	$scope.shared_data = SharedDataService;

	/*
	 * 取得
	 */
	$scope.gets = function() {
		return api.label_types.gets($http).success(function(data, status, headers, config) {
			$scope.label_types = data;
		});
	};

	/*
	 * 追加
	 */
	$scope.add = function(name) {
		return api.label_types.add($http, name).success(function(data, status, headers, config) {
			$scope.gets();
		});
	};
}]);
</script>

