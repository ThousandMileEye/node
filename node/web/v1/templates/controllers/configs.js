
<script type='text/javascript'>
app.controller('ConfigsController', ['$scope', '$filter', '$http', '$q', 'api', function ($scope, $filter, $http, $q, api) {
	var orderBy = $filter('orderBy');
	$scope.name = "";
	$scope.points = [];

	/*
	 * 取得
	 */
	$scope.gets = function() {
		return api.configs.gets($http).success(function(data, status, headers, config) {
			$scope.configs = data;
		});
	};

	/*
	 * 追加
	 */
	$scope.add = function(name) {
		return api.configs.add($http, name).success(function(data, status, headers, config) {
			$scope.gets();
		});
	};
}]);
</script>

