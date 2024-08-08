/* function positionTooltip(element, tooltip) {
    const rect = element.getBoundingClientRect();
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    // Reset position
    tooltip.style.top = '';
    tooltip.style.bottom = '';
    tooltip.style.left = '';
    tooltip.style.right = '';

    // Vertical positioning
    if (rect.top > viewportHeight / 2) {
        tooltip.style.bottom = '100%';
        tooltip.style.marginBottom = '5px';
    } else {
        tooltip.style.top = '100%';
        tooltip.style.marginTop = '5px';
    }

    // Horizontal positioning
    if (rect.left > viewportWidth / 2) {
        tooltip.style.right = '0';
    } else {
        tooltip.style.left = '0';
    }

    // Ensure tooltip is within viewport
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
    const triggers = document.querySelectorAll('.tooltip-trigger');
    
    triggers.forEach(trigger => {
        const tooltip = trigger.nextElementSibling;
        
        if (tooltip && tooltip.classList.contains('tooltip-content')) {
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