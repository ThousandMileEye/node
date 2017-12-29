
<script type='text/javascript'>
app.controller('PointsController', ['$scope', '$filter', '$http', '$q', 'api', function ($scope, $filter, $http, $q, api) {
	var orderBy = $filter('orderBy');
	$scope.name = "";
	$scope.points = [];

	/*
	 * 取得
	 */
	$scope.gets = function() {
		return api.points.gets($http).success(function(data, status, headers, config) {
			$scope.points = data;
		});
	};

	/*
	 * 追加
	 */
	$scope.add = function(name) {
		return api.points.add($http, name).success(function(data, status, headers, config) {
			$scope.gets();
		});
	};
}]);
</script>

