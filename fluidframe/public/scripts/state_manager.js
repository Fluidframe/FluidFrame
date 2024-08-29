(function() {
    const StateManager = {
        states: {},
        bindings: {},

        getState: function(id, key) {
            return this.states[id] && this.states[id][key];
        },

        setState: function(id, key, value) {
            if (!this.states[id]) this.states[id] = {};
            this.states[id][key] = value;
        },

        updateState: function(id, newState) {
            if (!this.states[id]) this.states[id] = {};
            Object.assign(this.states[id], newState);
        },

        getBindings: function(id) {
            return this.bindings[id] || {};
        },

        setBindings: function(id, bindings) {
            this.bindings[id] = bindings;
        },

        processStateAttribute: function(element) {
            const state = element.getAttribute('state');
            if (state) {
                try {
                    this.updateState(element.id, JSON.parse(state));
                    element.removeAttribute('state');
                } catch (e) {
                    console.error('Error parsing state attribute:', e);
                }
            }
        },

        processBindStateAttribute: function(element) {
            const bindState = element.getAttribute('bind-state');
            if (bindState) {
                try {
                    this.setBindings(element.id, JSON.parse(bindState));
                    element.removeAttribute('bind-state');
                } catch (e) {
                    console.error('Error parsing bind-state attribute:', e);
                }
            }
        },

        updateStateFromResponse: function(id, newState) {
            this.updateState(id, newState);
            const bindings = this.getBindings(id);
            Object.entries(bindings).forEach(([targetId, bindInfo]) => {
                const keys = bindInfo.keys || Object.keys(newState);
                const boundState = {};
                keys.forEach(key => {
                    if (key in newState) {
                        boundState[key] = newState[key];
                    }
                });
                this.updateState(targetId, boundState);
            });
        }
    };

    function handleTriggerInfo(element) {
        const triggerInfo = element.getAttribute('hx-trigger-info');
        if (triggerInfo) {
            try {
                const triggers = JSON.parse(triggerInfo);
                Object.entries(triggers).forEach(([eventType, config]) => {
                    element.addEventListener(eventType, createEventHandler(element, config));
                });
                element.removeAttribute('hx-trigger-info');
                
            } catch (e) {
                console.error('Error parsing hx-trigger-info attribute:', e);
            }
        }
    }

    function createEventHandler(element, config) {
        return function(event) {
            event.preventDefault();
            const detail = {
                elt: element,
                event: event,
                path: config.path|| element.getAttribute('hx-get'),
                target: config.target || element.getAttribute('hx-target'),
                swap: config.swap || element.getAttribute('hx-swap'),
                params: config.params || {},
                headers: config.headers || {},
                values: config.values || {},
                method: config.method || 'GET'
            };

            if (!htmx.trigger(element, 'htmx:configRequest', detail).defaultPrevented) {
                if (!htmx.trigger(element, 'htmx:beforeRequest', detail).defaultPrevented) {
                    if (!htmx.trigger(element, 'htmx:beforeSend', detail).defaultPrevented) {
                        htmx.ajax(detail.method, detail.path, detail);
                    }
                }
            }
        };
    }

    function processNewElements(elements) {
        // Ensure elements is always an array
        const elementsArray = Array.from(elements);

        elementsArray.forEach(node => {
            if (node.nodeType === Node.ELEMENT_NODE) {
                if (node.id) {
                    StateManager.processStateAttribute(node);
                    StateManager.processBindStateAttribute(node);
                    handleTriggerInfo(node);
                }
                processNewElements(node.children);
            }
        });
    }

    function setupObserver() {
        if (!window.fluidFrameObserver) {
            window.fluidFrameObserver = new MutationObserver(mutations => {
                mutations.forEach(mutation => {
                    if (mutation.type === 'childList') {
                        processNewElements(mutation.addedNodes);
                    } else if (mutation.type === 'attributes') {
                        const { target, attributeName } = mutation;
                        if (target.id) {
                            if (attributeName === 'state') StateManager.processStateAttribute(target);
                            else if (attributeName === 'bind-state') StateManager.processBindStateAttribute(target);
                            else if (attributeName === 'hx-trigger-info') handleTriggerInfo(target);
                        }
                    }
                });
            });

            window.fluidFrameObserver.observe(document.body, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['state', 'bind-state', 'hx-trigger-info']
            });
        }
    }

    function initializeEventListeners() {
        document.body.addEventListener('htmx:configRequest', event => {
            const { elt, headers } = event.detail;
            if (elt.id) {
                const state = { ...StateManager.states[elt.id] };
                const bindings = StateManager.getBindings(elt.id);
                Object.entries(bindings).forEach(([targetId, bindInfo]) => {
                    const targetState = StateManager.states[targetId];
                    if (targetState) {
                        const keys = bindInfo.keys || Object.keys(targetState);
                        keys.forEach(key => {
                            if (key in targetState) {
                                state[`${key}`] = targetState[key];
                            }
                        });
                    }
                });
                if (Object.keys(state).length > 0) {
                    headers['X-Component-State'] = JSON.stringify(state);
                    headers['HX-Trigger'] = elt.id;
                }
            }
        });

        document.body.addEventListener('htmx:beforeOnLoad', event => {
            const { xhr, elt } = event.detail;
            const newState = xhr.getResponseHeader('X-Component-State');
            const id = xhr.getResponseHeader('HX-Trigger-Id');
            if (newState) {
                try {
                    const parsedState = JSON.parse(newState);
                    if (Object.keys(parsedState).length > 0) {
                        if (id) {
                            StateManager.updateStateFromResponse(id, parsedState);
                            console.log(`Updated state for ${id}:`, StateManager.states[id]);
                        } else {
                            console.warn('No id found for element, state update skipped');
                        }
                    }
                } catch (e) {
                    console.error('Error parsing X-Component-State header:', e);
                }
            }
        });

        setupObserver();
    }

    function initialize() {
        processNewElements([document.body]);
        initializeEventListeners();
    }

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initialize);
    } else {
        initialize();
    }

    // Expose API
    window.FluidFrameState = StateManager;

    console.log('Initial states:', StateManager.states);
    console.log('Initial bindings:', StateManager.bindings);
})();
