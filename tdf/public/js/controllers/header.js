/**
 * Defines the elements on the upper navigation bar of the page.
 */
angular.module('tdf.system').controller('HeaderController',
    ['$scope',
    function($scope) {

        ///////////////////////////////////////////////////////////////////////
        //  Properties
        ///////////////////////////////////////////////////////////////////////

        /**
         * Defines the elements on the public menu (accessible always,
         * regardless of whether a user is logged in or not.
         *
         * See set_menu() for acceptable formats.
         */
        $scope.public_menu = [{
            'title': 'Leagues',
            'link': 'leagues/'
        }]

        ///////////////////////////////////////////////////////////////////////
        //  Methods
        ///////////////////////////////////////////////////////////////////////

        /**
         * Sets the menu items as determined by the login state.
         *
         * If the login state is that no user is logged in, then the menu
         * consists only of the elements defined by $scope.public_menu.
         *
         * All menu definitions should be arrays of dicts, where each dict
         * has attributes 'title' (the text of the menu item) and 'link'
         * (the page, relative to http://<host>/ pointed to by the menu item).
         */
        $scope.set_menu = function() {
            // TODO Other login states.
            $scope.menu = $scope.public_menu;
        }

    }]);
