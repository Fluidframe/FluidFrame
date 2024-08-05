function positionTooltip(element, tooltip) {
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

function addTooltip(element, text) {
    // Add necessary classes
    element.classList.add('tooltip-trigger');

    // Create tooltip content
    const tooltip = document.createElement('span');
    tooltip.className = 'tooltip-content';
    tooltip.textContent = text;
    element.appendChild(tooltip);

    // Position tooltip on hover
    element.addEventListener('mouseenter', () => positionTooltip(element, tooltip));
}