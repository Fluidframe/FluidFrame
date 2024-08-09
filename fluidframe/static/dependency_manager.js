// Track the loaded scripts and styles
let loadedScripts = JSON.parse(localStorage.getItem('loadedScripts')) || [];
let loadedStyles = JSON.parse(localStorage.getItem('loadedStyles')) || [];
let scriptContent = JSON.parse(localStorage.getItem('scriptContent')) || {};
let styleContent = JSON.parse(localStorage.getItem('styleContent')) || {};

function checkAndLoadScript(src) {
  // Check if the script is already loaded in the DOM
  let script = document.querySelector(`script[src="${src}"]`);
  if (script) {
    console.log('Script already loaded in the DOM:', src);
    return '';
  }

  // Check if the script is already loaded in the array
  if (loadedScripts.includes(src)) {
    console.log('Script already loaded:', src);
    // If the script is not in the DOM, create a new script element and append it
    if (!script) {
      script = document.createElement('script');
      script.src = src;
      script.textContent = scriptContent[src];
      document.head.appendChild(script);
    }
    return '';
  }

  // Load the script
  script = document.createElement('script');
  script.src = src;
  script.onload = () => {
    // Add the script to the loaded scripts
    loadedScripts.push(src);
    scriptContent[src] = script.textContent;
    localStorage.setItem('loadedScripts', JSON.stringify(loadedScripts));
    localStorage.setItem('scriptContent', JSON.stringify(scriptContent));
  };
  document.head.appendChild(script);

  console.log('Loaded script:', src);
  return '';
}

function checkAndLoadStyle(href) {
  // Check if the style is already loaded in the DOM
  let link = document.querySelector(`link[href="${href}"]`);
  if (link) {
    console.log('Style already loaded in the DOM:', href);
    return '';
  }

  // Check if the style is already loaded in the array
  if (loadedStyles.includes(href)) {
    console.log('Style already loaded:', href);
    // If the style is not in the DOM, create a new link element and append it
    if (!link) {
      link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = href;
      link.textContent = styleContent[href];
      document.head.appendChild(link);
    }
    return '';
  }

  // Load the style
  link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = href;
  link.onload = () => {
    // Add the style to the loaded styles
    loadedStyles.push(href);
    styleContent[href] = link.sheet.cssRules[0].cssText;
    localStorage.setItem('loadedStyles', JSON.stringify(loadedStyles));
    localStorage.setItem('styleContent', JSON.stringify(styleContent));
  };
  document.head.appendChild(link);

  console.log('Loaded style:', href);
  return '';
}