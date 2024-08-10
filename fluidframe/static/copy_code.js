function copyCodeToClipboard(id) {
    const parentDiv = document.getElementById(id);
    const codeElement = parentDiv.querySelector('code');

    if (codeElement) {
        // Get the innerHTML of the <code> element and normalize whitespace
        const codeText = codeElement.innerText;

        navigator.clipboard.writeText(codeText)
            .then(() => alert('Code copied to clipboard!'))
            .catch(err => console.error('Failed to copy:', err));
    }
}