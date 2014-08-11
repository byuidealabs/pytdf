/**
 * Initializes the angular.js app.
 */
window.bootstrap = function() {
    angular.bootstrap(document, ['tdf']);
};

window.init = function() {
    window.bootstrap();
};

$(document).ready(function() {
    window.init();
});
