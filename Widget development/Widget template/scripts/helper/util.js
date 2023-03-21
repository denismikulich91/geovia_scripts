define
(
    'Widget/Helper',
    [
    ],
    function
    (
    )
    {
        var exports = {
            onLoad: function() {
                console.log(Math.round(Math.random() * 20));
            }
        }

        return exports;
    }
);