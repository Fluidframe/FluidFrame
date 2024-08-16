// Track the loaded resources
let loadedResources = JSON.parse(localStorage.getItem('loadedResources')) || {
  scripts: [],
  styles: []
};
let resourceContent = JSON.parse(localStorage.getItem('resourceContent')) || {
  scripts: {},
  styles: {}
};

/*
// Set up Intersection Observer
const dependency_observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const target = entry.target;
      const dependencies = JSON.parse(target.getAttribute('data-dependencies'));
      loadDependencies(dependencies);
      dependency_observer.unobserve(target);  // Stop observing once dependencies are loaded
    }
  });
}, {
  root: null,
  rootMargin: '100px',  // Load when within 100px of viewport
  threshold: 0.1
});

// Observe all elements with data-dependencies attribute
document.querySelectorAll('[data-dependencies]').forEach(el => {
  dependency_observer.observe(el);
});
*/

function loadDependencies(dependencies) {
  return new Promise((resolve) => {
    const scripts = dependencies.scripts || [];
    const styles = dependencies.styles || [];

    const loadResource = (src, type) => {
      return new Promise((resolveResource) => {
        // Check if the resource is already loaded in the DOM
        let element = document.querySelector(`${type === 'script' ? 'script[src' : 'link[href'}="${src}"]`);
        if (element) {
          console.log(`${type} already loaded in the DOM:`, src);
          resolveResource();
          return;
        }

        // Check if the resource is already loaded in the array
        if (loadedResources[type + 's'].includes(src)) {
          console.log(`${type} already loaded:`, src);
          if (!element) {
            element = document.createElement(type === 'script' ? 'script' : 'link');
            if (type === 'script') {
              element.src = src;
              element.textContent = resourceContent.scripts[src];
            } else {
              element.rel = 'stylesheet';
              element.href = src;
              element.textContent = resourceContent.styles[src];
            }
            document.head.appendChild(element);
          }
          resolveResource();
          return;
        }

        // Load the resource
        element = document.createElement(type === 'script' ? 'script' : 'link');
        if (type === 'script') {
          element.src = src;
        } else {
          element.rel = 'stylesheet';
          element.href = src;
        }

        element.onload = () => {
          loadedResources[type + 's'].push(src);
          if (type === 'script') {
            resourceContent.scripts[src] = element.textContent;
          } else {
            resourceContent.styles[src] = element.sheet.cssRules[0].cssText;
          }
          localStorage.setItem('loadedResources', JSON.stringify(loadedResources));
          localStorage.setItem('resourceContent', JSON.stringify(resourceContent));
          console.log(`Loaded ${type}:`, src);
          resolveResource();
        };

        document.head.appendChild(element);
      });
    };

    const loadSequentially = async (resources, type) => {
      for (const resource of resources) {
        await loadResource(resource, type);
      }
    };

    Promise.all([
      loadSequentially(styles, 'style'),
      loadSequentially(scripts, 'script')
    ]).then(() => resolve());
  });
}