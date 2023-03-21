define
(
    'Widget/js/Main',
    [
        // 3DEXPERIENCE Cloud Platform JS modules 
        'DS/PlatformAPI/PlatformAPI',

        // Custom modules
        'Modules/Util'
    ],
    function
    (
        PlatformAPI,
        Util
    )
    {

        // Declare public functions or variables here. Accessible by other modules. Call it by "Main.<function>". Usage sample, e.g. Main.onLoad() 
        var exports = {
            onLoad: function() {
                const TEST = prompt('Give test value:');
                const PASSWORD = prompt('Enter password:');
                console.info("Global var widget", widget);

                console.log("Widget is running!");
                let count = 0;
                const container = document.createElement('div');
                const button = document.createElement('button');
                button.innerText = 'click me';
                const text = document.createElement('div');
                text.innerHTML = "The button has been clicked 0 times";

                button.addEventListener('click', () => {
                    count++;
                    text.innerHTML = `The button has been clicked ${count} times`;
                })

                console.info("Random number: " + Util.myFunction(10));
                console.info(TEST);
                console.info(PASSWORD);

                container.appendChild(button);
                container.appendChild(text);
                widget.body.innerHTML = '';
                widget.body.appendChild(container);
            },

            onResize: function() {
                console.info("onResize");
            },

            onViewChange: function() {
                console.info("onViewChange");
            },

            onEdit: function() {
                console.info("onEdit");
            },

            onRefresh: function() {
                console.info("onRefresh");
            },

            endEdit: function() {
                console.info("endEdit");
            }
        };

        return exports;
    }
);