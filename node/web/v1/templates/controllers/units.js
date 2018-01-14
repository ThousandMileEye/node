
<script type='text/javascript'>
app.controller('UnitsController', ['$scope', '$filter', '$http', '$q', 'api', 'SharedDataService', function ($scope, $filter, $http, $q, api, SharedDataService) {
	var orderBy = $filter('orderBy');
	$scope.shared_data = SharedDataService;

	/*
	 * 取得
	 */
	$scope.gets = function() {
		return api.units.gets($http).success(function(data, status, headers, config) {
			$scope.units = data;
		});
	};

	/*
	 * 追加
	 */
	$scope.add = function(name, label_type_id) {
		return api.units.add($http, name, label_type_id).success(function(data, status, headers, config) {
			$scope.gets();
		});
	};
}]);
</script>

