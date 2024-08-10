/*
function positionTooltip(trigger, tooltip) {
    const rect = trigger.getBoundingClientRect();
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    tooltip.style.top = '';
    tooltip.style.bottom = '';
    tooltip.style.left = '';
    tooltip.style.right = '';

    if (rect.top > viewportHeight / 2) {
        tooltip.style.bottom = '100%';
        tooltip.style.marginBottom = '5px';
    } else {
        tooltip.style.top = '100%';
        tooltip.style.marginTop = '5px';
    }

    if (rect.left > viewportWidth / 2) {
        tooltip.style.right = '0';
    } else {
        tooltip.style.left = '0';
    }

    const tooltipRect = tooltip.getBoundingClientRect();
    if (tooltipRect.right > viewportWidth) {
        tooltip.style.right = '0';
        tooltip.style.left = 'auto';
    }
    if (tooltipRect.left < 0) {
        tooltip.style.left = '0';
        tooltip.style.right = 'auto';
    }
}


function initTooltips() {
    document.querySelectorAll('.tooltip-content').forEach(tooltip => {
        const triggerSelector = tooltip.getAttribute('tooltip-target');
        const trigger = document.querySelector(triggerSelector);

        if (trigger) {
            trigger.addEventListener('mouseenter', () => {
                tooltip.classList.remove('invisible', 'opacity-0');
                tooltip.classList.add('visible', 'opacity-100');
                positionTooltip(trigger, tooltip);
            });

            trigger.addEventListener('mouseleave', () => {
                tooltip.classList.remove('visible', 'opacity-100');
                tooltip.classList.add('invisible', 'opacity-0');
            });
        }
    });
}

document.addEventListener('DOMContentLoaded', initTooltips);
*/


const FluidFrameTooltip = (function() {
    function positionTooltip(trigger, tooltip) {
        const rect = trigger.getBoundingClientRect();
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;

        tooltip.style.top = '';
        tooltip.style.bottom = '';
        tooltip.style.left = '';
        tooltip.style.right = '';

        if (rect.top > viewportHeight / 2) {
            tooltip.style.bottom = '100%';
            tooltip.style.marginBottom = '5px';
        } else {
            tooltip.style.top = '100%';
            tooltip.style.marginTop = '5px';
        }

        if (rect.left > viewportWidth / 2) {
            tooltip.style.right = '0';
        } else {
            tooltip.style.left = '0';
        }

        const tooltipRect = tooltip.getBoundingClientRect();
        if (tooltipRect.right > viewportWidth) {
            tooltip.style.right = '0';
            tooltip.style.left = 'auto';
        }
        if (tooltipRect.left < 0) {
            tooltip.style.left = '0';
            tooltip.style.right = 'auto';
        }
    }

    function initTooltip(tooltipElement) {
        const triggerSelector = tooltipElement.getAttribute('tooltip-target');
        const trigger = document.querySelector(triggerSelector);

        if (trigger) {
            const showTooltip = () => {
                tooltipElement.classList.remove('invisible', 'opacity-0');
                tooltipElement.classList.add('visible', 'opacity-100');
                positionTooltip(trigger, tooltipElement);
            };

            const hideTooltip = () => {
                tooltipElement.classList.remove('visible', 'opacity-100');
                tooltipElement.classList.add('invisible', 'opacity-0');
            };

            trigger.addEventListener('mouseenter', showTooltip);
            trigger.addEventListener('mouseleave', hideTooltip);

            // Store the event listeners so we can remove them later if needed
            tooltipElement._tooltipListeners = { showTooltip, hideTooltip };
        }
    }

    return {
        init: function(container = document) {
            container.querySelectorAll('.tooltip-content').forEach(initTooltip);
        },
        refresh: function(container = document) {
            container.querySelectorAll('.tooltip-content').forEach(tooltipElement => {
                if (tooltipElement._tooltipListeners) {
                    const triggerSelector = tooltipElement.getAttribute('tooltip-target');
                    const trigger = document.querySelector(triggerSelector);
                    if (trigger) {
                        trigger.removeEventListener('mouseenter', tooltipElement._tooltipListeners.showTooltip);
                        trigger.removeEventListener('mouseleave', tooltipElement._tooltipListeners.hideTooltip);
                    }
                }
                initTooltip(tooltipElement);
            });
        }
    };
})();
