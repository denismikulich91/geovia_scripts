define
(
    "Modules/Util",
    [
        
    ],
    function
    (
        
    )
    {
        console.info('Util loaded');

        // global variables (widget, UWA, document)

        // Private functions. Not accessible by other modules. Accesible within this module only

        function getRandomNumber(upperLimit) {
            return Math.round(Math.random() * upperLimit);
        }

        // Declare public functions or variable here. Accessible by other modules.
        var exports = {
            myFunction: function(arg1) {
                console.info(arg1);

                return getRandomNumber(arg1);
            }
        };

        return exports;
    }
);