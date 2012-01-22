(function(window) {
    if (window.location !== window.top.location) {
        window.top.location = window.location;
    }
})(this);

