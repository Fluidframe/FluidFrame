/*
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

*/
class WebSocketManager {
  constructor(url) {
    this.socket = null;
    this.url = this.determineWebSocketURL();
    this.socket = null;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
    this.reconnectInterval = 1000; // Start with 1 second
    this.handlers = {};
  }

  determineWebSocketURL() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const host = window.location.host;
    const wsEndpoint = '/ws';

    // Check for environment-specific overrides
    if (window.WS_ENDPOINT) {
      return window.WS_ENDPOINT;
    }

    // Check for a load balancer endpoint
    if (window.WS_LOAD_BALANCER) {
      return `${protocol}//${window.WS_LOAD_BALANCER}${wsEndpoint}`;
    }

    // Default to the current host
    return `${protocol}//${host}${wsEndpoint}`;
  }

  connect() {
    this.socket = new WebSocket(this.url);
    this.socket.onopen = this.onOpen.bind(this);
    this.socket.onclose = this.onClose.bind(this);
    this.socket.onerror = this.onError.bind(this);
    this.socket.onmessage = this.onMessage.bind(this);
  }

  onOpen() {
    console.log('WebSocket connected');
    this.reconnectAttempts = 0;
    this.reconnectInterval = 1000;
  }

  onClose() {
    console.log('WebSocket disconnected');
    this.reconnect();
  }

  onError(error) {
    console.error('WebSocket error:', error);
  }

  onMessage(event) {
    const data = JSON.parse(event.data);
    if (this.handlers[data.type]) {
      this.handlers[data.type](data.payload);
    }
  }

  reconnect() {
    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
      console.log('Max reconnect attempts reached');
      return;
    }

    setTimeout(() => {
      console.log('Attempting to reconnect...');
      this.connect();
      this.reconnectAttempts++;
      this.reconnectInterval *= 2; // Exponential backoff
    }, this.reconnectInterval);
  }

  send(type, payload) {
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({ type, payload }));
    } else {
      console.error('WebSocket is not open');
    }
  }

  addMessageHandler(type, handler) {
    this.handlers[type] = handler;
  }
}

// Usage
let wsManager = new WebSocketManager();
wsManager.connect();
wsManager.send('chat', { message: 'Hello, world!' });