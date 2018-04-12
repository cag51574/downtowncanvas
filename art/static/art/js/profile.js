$("#type-color-on-page").spectrum({
    color: color.toHexString(),
    change: function(color) {
        $("#basic-log").text("change called: " + color.toHexString());
    }
});
