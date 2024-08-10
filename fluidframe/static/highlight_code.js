// Import the speed-highlighter library
import { highlightElement } from 'speed-highlighter';

/**
 * Highlights the code snippets within a given parent element.
 * @param {string} parentId - The ID of the parent element containing the code snippets.
 * @param {Object} options - Optional parameters for customization.
 * @param {string} [options.language] - The programming language of the code snippets.
 * @param {string} [options.theme] - The theme to use for highlighting.
 * @param {boolean} [options.showLineNumbers] - Whether to show line numbers.
 */

function highlightCodeSnippets(parentId, options = {}) {
  // Get the parent element
  const parentElement = document.getElementById(parentId);
  if (!parentElement) {
    console.error(`Parent element with id "${parentId}" not found.`);
    return;
  }

  // Get all the pre and code elements within the parent element
  const codeElements = parentElement.querySelectorAll('pre > code, code');

  // Highlight each code snippet
  codeElements.forEach((codeElement) => {
    const { language, theme, showLineNumbers } = options;
    
    // Configure highlighting options
    const highlightOptions = {
      language: language || 'auto', // Default to auto-detection if not specified
      theme: theme || 'default',    // Default theme if not specified
      showLineNumbers: showLineNumbers || false // Default to false if not specified
    };

    // Apply highlighting
    highlightElement(codeElement, highlightOptions);

    // If line numbers are requested, add them
    if (showLineNumbers) {
      addLineNumbers(codeElement);
    }
  });
}

/**
 * Adds line numbers to a code element.
 * @param {HTMLElement} codeElement - The code element to add line numbers to.
 */
function addLineNumbers(codeElement) {
  const lines = codeElement.innerHTML.split('\n');
  const numberedLines = lines.map((line, index) => 
    `<span class="line-number">${index + 1}</span>${line}`
  );
  codeElement.innerHTML = numberedLines.join('\n');
}