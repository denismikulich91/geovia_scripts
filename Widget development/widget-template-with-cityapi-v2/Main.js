define
(
    'Widget/Main',
    [
        // 3DEXPERIENCE Cloud Platform JS modules 
        'DS/PlatformAPI/PlatformAPI'

        // Custom template modules
        ,'Modules/WidgetManager'
        ,'Modules/VariableManager'

        // Your custom modules
        ,'Modules/Custom'

        // ,'DS/Controls/Button'
    ],
    function
    (
        PlatformAPI
        ,WidgetManager
        ,VariableManager
        ,Custom
        // ,WUXButton
    )
    {
        // global variables (widget, UWA, document)

        // Private functions or variables. Not accessible by other modules. Accesible within this module only
        var _input = {};

        // ===== Helper function to make request to City API for any available topic
        function makeAPIRequest(topic, data) {
            var request = {
                messageId: UWA.Utils.getUUID(),
                publisher: widget.id
            };

            if(UWA.is(data, 'object')) {
                request.data = data;
            }

            // Get target city widget ID
            if(topic != 'ping' && topic != 'pair') {
                request.widgetId = WidgetManager.getSameTabWidgets()[0].id;
            }

            console.info('xCity.' + topic, request);
            PlatformAPI.publish('xCity.' + topic, request);
        }

        // ===== Function to setup basic City API subscription 
        function setupSubscriptions() {
            // unsubscribe common city topics to prevent double subscriptions
            PlatformAPI.unsubscribe('xCity.resolve');
            PlatformAPI.unsubscribe('xCity.catch');

            // subscribes to common city topics
            PlatformAPI.subscribe('xCity.resolve', resolve.bind(this)); // Good API result will be funneled to "resolve" function
            PlatformAPI.subscribe('xCity.catch', reject.bind(this)); // Bad API result will be funneled to "reject" function
        }

        // ===== Helper functions to receive all API result before funneled further to each individual topic function
        function resolve(res) {
            if(isValidResultMessage(res)) {
                console.info('Resolve: ', res);

                switch(res.topic) {
                    case 'xCity.ping': ping(res); break;
                    case 'xCity.pair': pair(res); break;
                    case 'xCity.moveTo': moveTo(res); break;
                    case 'xCity.onClick': onClick(res); break;
                    case 'xCity.onSelect': onSelect(res); break;
                    case 'xCity.onDeselect': onDeselect(res); break;
                    // case 'xCity.<topic>': topicFunction(res); break;
                    default: console.info('No setup for ' + res.topic + ' topic');
                }

            }
        }

        function reject(res) {
            if(isValidResultMessage(res)) {
                console.warn('Reject: ', res);
            }
        }

        // ===== Individual functions to process API result for each topic
        function onClick(res) {
            console.info('onClick: ', res);
        }

        function onSelect(res) {
            console.info('onSelect: ', res);
        }

        function onDeselect(res) {
            console.info('onDeselect: ', res);
        }

        function ping(res) {
            console.info('ping: ', res);
        }

        function pair(res) {
            console.info('pair: ', res);
            if(UWA.is(res.data, 'object')) {

                if((res.data.status === 'pairing-success' || res.data.status === 'paired') && !WidgetManager.isPaired(res.publisher)) {
                    WidgetManager.addPairedWidget(res.publisher, res.data.title);
                }
                else if(res.data.status === 'pairing-removed') {
                    WidgetManager.removePairedWidget(res.publisher);
                }
            } 
        }

        function moveTo(res) {
            console.info('moveTo: ', res);
        }

        // ===== Helper functions to verify API result is valid
        function isValidResultMessage(res) {
            if(UWA.is(res, 'object')) {

                // If result is broadcast type to dashboard
                if(res.messageType === 'broadcast' && res.subscribeType === 'dashboard') {
                    return true;
                }
                // Else always check if it is for this widget
                else if(isForThisWidget(res.widgetId)) {
                    return true;
                }
            }

            return false;
        }

        function isForThisWidget(widgetId) {
            if(
                (UWA.is(widgetId, 'string') && widgetId === widget.id) ||
                (UWA.is(widgetId, 'array') && widgetId.includes(widget.id))
            ) {
                return true;
            }

            return false;
        }

        function createUserInterface() {
            var container = new UWA.createElement('div');
            container.inject(widget.body);

            _input.btnPing = new UWA.createElement('button', {value: 'Ping', title: 'Ping', name: 'Ping', html: 'Ping'});
            _input.btnPing.addEventListener('click', function(e) {
                makeAPIRequest('ping');
            });

            _input.btnPair = new UWA.createElement('button', {value: 'Pair', title: 'Pair', name: 'Pair', html: 'Pair'});
            _input.btnPair.addEventListener('click', function(e) {
                makeAPIRequest('pair', {title: widget.title});
            });
            
            for(var key in _input) {
                _input[key].inject(container);
            }
        }

        // Declare public functions or variables here. Accessible by other modules. Call it by "Main.<function>". Usage sample, e.g. Main.onLoad() 
        var exports = {
            onLoad: function() {
                console.info("Global var widget", widget);

                setupSubscriptions();
                WidgetManager.refreshTabWidgetList();

                widget.setBody('Subscription setup complete. Try to click on 3DView map of City widget then observe the console log for API input/output.'); // Set widget user interface container to empty to remove "Loading" message.

                Custom.myHello;
                Custom.myGet;
                Custom.myFunction('arg1', 'arg2');

                createUserInterface();
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

                setupSubscriptions();
                WidgetManager.refreshTabWidgetList();
                VariableManager.setData('test');
            },

            endEdit: function() {
                console.info("endEdit");
            }
        };

        return exports;
    }
);