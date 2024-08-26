(function() {
    if (typeof window.fluidFrameStateStore === 'undefined') {
        window.fluidFrameStateStore = {
            states: {},
            bindings: {}
        };
    }

    const stateStore = window.fluidFrameStateStore.states;
    const bindingStore = window.fluidFrameStateStore.bindings;

    const updateStateStore = function(element) {
        const {id} = element;
        const state = element.getAttribute('state');
        const bindState = element.getAttribute('bind-state');
        
        if (state) {
            try {
                stateStore[id] = JSON.parse(state);
                element.removeAttribute('state');
            } catch (e) {
                console.error('Error parsing state attribute:', e);
            }
        }
        
        if (bindState) {
            try {
                const bindRelations = JSON.parse(bindState);
                for (const [targetId, bindInfo] of Object.entries(bindRelations)) {
                    if (!bindingStore[id]) {
                        bindingStore[id] = {};
                    }
                    bindingStore[id][targetId] = bindInfo;
                }
                element.removeAttribute('bind-state');
            } catch (e) {
                console.error('Error parsing bind-state attribute:', e);
            }
        }
    };

    const cleanupStateStore = function(id) {
        if (id) {
            delete stateStore[id];
            delete bindingStore[id];
        }
    };

    const initializeEventListeners = function() {
        document.body.addEventListener('htmx:afterSettle', (event) => {
            updateStateStore(event.detail.elt);
        });

        document.body.addEventListener('htmx:beforeCleanupElement', (event) => {
            const {id} = event.detail.elt;
            cleanupStateStore(id);
        });

        document.body.addEventListener('htmx:configRequest', (event) => {
            const {elt} = event.detail;
            const {id} = elt;
            if (id) {
                let requestState = {};
                if (stateStore[id]) {
                    requestState = {...stateStore[id]};
                }
                if (bindingStore[id]) {
                    for (const [targetId, bindInfo] of Object.entries(bindingStore[id])) {
                        if (stateStore[targetId]) {
                            const keys = bindInfo.keys || Object.keys(stateStore[targetId]);
                            for (const key of keys) {
                                if (key in stateStore[targetId]) {
                                    requestState[key] = stateStore[targetId][key];
                                }
                            }
                        }
                    }
                }
                if (Object.keys(requestState).length > 0) {
                    event.detail.headers['X-Component-State'] = JSON.stringify(requestState);
                }
            }
        });

        document.body.addEventListener('htmx:beforeOnLoad', (event) => {
            const {xhr, elt} = event.detail;
            const newTarget = xhr.getResponseHeader('HX-Target-Update');
            const newState = xhr.getResponseHeader('X-Component-State');
            if (newTarget) {
                try {
                    const targetMapping = JSON.parse(newTarget);
                    if (typeof targetMapping === 'object' && targetMapping !== null) {
                        // Get the current hx-target attribute value
                        let currentTargets = elt.getAttribute('hx-target');
                        if (currentTargets) {
                            // Split the current hx-target value into individual targets
                            let targetList = currentTargets.split(' ');
        
                            // Update only the specified targets based on the JSON mapping
                            targetList = targetList.map(target => {
                                const strippedTarget = target.startsWith('#') ? target.substring(1) : target;
                                return targetMapping[strippedTarget] ? `#${targetMapping[strippedTarget]}` : target;
                            });
        
                            // Join the updated targets back into a single string and set it
                            elt.setAttribute('hx-target', targetList.join(' '));
                            console.log(`hx-target updated to: ${targetList.join(' ')}`);
                        }
                    }
                } catch (e) {
                    console.error('Error parsing HX-Retarget header as JSON:', e);
                }
            }
            if (newState) {
                try {
                    const parsedState = JSON.parse(newState);
                    if (Object.keys(parsedState).length > 0) {
                        const {id} = event.detail.elt;
                        if (stateStore[id]) {
                            Object.assign(stateStore[id], parsedState);
                        } else {
                            stateStore[id] = parsedState;
                        }
                        
                        // Update bound states
                        if (bindingStore[id]) {
                            for (const [targetId, bindInfo] of Object.entries(bindingStore[id])) {
                                if (stateStore[targetId]) {
                                    const keys = bindInfo.keys || Object.keys(parsedState);
                                    for (const key of keys) {
                                        if (key in parsedState) {
                                            stateStore[targetId][key] = parsedState[key];
                                        }
                                    }
                                }
                            }
                        }
                    }
                } catch (e) {
                    console.error('Error parsing X-Component-State header:', e);
                }
            }
        });

        // setInterval(cleanupStateStore, 60000);
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('[state], [bind-state]').forEach(updateStateStore);
            initializeEventListeners();
        });
    } else {
        document.querySelectorAll('[state], [bind-state]').forEach(updateStateStore);
        initializeEventListeners();
    }

    console.log('Initial stateStore:', stateStore);
    console.log('Initial bindingStore:', bindingStore);
})();
