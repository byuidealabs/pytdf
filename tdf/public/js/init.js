window.bootstrap = function() {
    angular.bootstrap(document, ['tdf']);
};

window.init = function() {
    window.bootstrap();
};

$(document).ready(function() {
    //Then init the app
    window.init();
});
