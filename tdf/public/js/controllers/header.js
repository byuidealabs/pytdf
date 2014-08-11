angular.module('tdf.system').controller('HeaderController',
    ['$scope',
    function($scope) {

        $scope.set_menu = function() {
            $scope.menu = [$scope.public_menu];
        }

        $scope.public_menu = {
            'title': 'Leagues',
            'link': 'leagues/'
        }

    }]);
