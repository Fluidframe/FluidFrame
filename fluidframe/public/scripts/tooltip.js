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

function showTooltip(parentid, tooltipId) {
    const trigger = document.getElementById(parentid);
    const tooltip = document.getElementById(tooltipId);
    if (tooltip) {
        tooltip.classList.remove('invisible', 'opacity-0');
        tooltip.classList.add('visible', 'opacity-100');
        positionTooltip(trigger, tooltip);
    }
}

function hideTooltip(tooltipId) {
    const tooltip = document.getElementById(tooltipId);
    if (tooltip) {
        tooltip.classList.remove('visible', 'opacity-100');
        tooltip.classList.add('invisible', 'opacity-0');
    }
}
