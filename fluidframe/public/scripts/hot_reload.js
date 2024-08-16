(function() {
  // Get the current page's URL
  const pageUrl = new URL(window.location.href);

  // Construct the WebSocket URL
  const wsUrl = `ws://${pageUrl.host}/ws`;

  // Create a WebSocket connection
  let ws = new WebSocket(wsUrl);
  let reconnectInterval;
  let reconnectTimeout;

  // Function to handle WebSocket reconnection
  function reconnectWebSocket() {
    // Check if the client has been trying to reconnect before
    const isReconnecting = localStorage.getItem('isReconnecting') === 'true';

    // Try to reconnect the WebSocket connection every 500ms
    reconnectInterval = setInterval(function() {
      ws = new WebSocket(wsUrl);
    }, 500);

    // Set a 1-second timeout to stop trying to reconnect
    reconnectTimeout = setTimeout(function() {
      clearInterval(reconnectInterval);
      console.log('Giving up on reconnecting after 1 seconds');

      // Reload the page only if the client was previously reconnecting
      if (isReconnecting) {
        localStorage.setItem('isReconnecting', 'false');
        window.location.reload();
      }
    }, 1000);
  }

  // When the WebSocket connection is established
  ws.onopen = function() {
    console.log('WebSocket connection opened');
    // Clear the reconnect interval and timeout if they exist
    clearInterval(reconnectInterval);
    clearTimeout(reconnectTimeout);
    // Reset the reconnection flag in local storage
    localStorage.setItem('isReconnecting', 'false');
  };

  // When the WebSocket connection is closed
  ws.onclose = function() {
    console.log('WebSocket connection closed');
    // Set the reconnection flag in local storage
    localStorage.setItem('isReconnecting', 'true');
    // Try to reconnect the WebSocket connection
    reconnectWebSocket();
  };

  // When the WebSocket receives a message
  ws.onmessage = function(event) {
    console.log('Received message:', event.data);
  };

  // When the WebSocket encounters an error
  ws.onerror = function(event) {
    console.error('WebSocket error:', event);
  };
})();
