// Import the speed-highlighter library
import { highlightElement } from 'speed-highlighter';

/**
 * Highlights the code snippets within a given parent element.
 * @param {string} parentId - The ID of the parent element containing the code snippets.
 * @param {string} [language] - The programming language of the code snippets (optional).
 */
function highlightCodeSnippets(parentId, language) {
  // Get the parent element
  const parentElement = document.getElementById(parentId);

  // Get all the pre and code elements within the parent element
  const codeElements = parentElement.querySelectorAll('pre > code');

  // Highlight each code snippet
  codeElements.forEach((codeElement) => {
    highlightElement(codeElement, language);
  });
}