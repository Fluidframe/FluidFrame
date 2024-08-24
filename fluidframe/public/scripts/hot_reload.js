class WebSocketManager {
  constructor() {
      this.socket = null;
      this.url = this.determineWebSocketURL();
      this.reconnectAttempts = 0;
      this.maxReconnectAttempts = 5;
      this.reconnectInterval = 1000; // Start with 1 second
      this.pingInterval = 20000; // Send a ping every 10 seconds
      this.shouldRefresh = false; // Flag to check if the browser should refresh
  }

  determineWebSocketURL() {
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const host = window.location.host;
      const wsEndpoint = '/live-reload';
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

      // If this is a reconnection, refresh the page
      if (this.shouldRefresh) {
          console.log('Reconnected - refreshing the page');
          window.location.reload();
      } else {
          this.shouldRefresh = true; // Set the flag for future reconnections
          this.startPinging(); // Start pinging if this is the first connection
      }
  }

  onClose() {
      console.log('WebSocket disconnected');
      this.reconnect();
  }

  onError(error) {
      console.error('WebSocket error:', error);
  }

  onMessage(event) {
      if (event.data === "pong") {
          console.log('Received pong from server');
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

  startPinging() {
      setInterval(() => {
          if (this.socket && this.socket.readyState === WebSocket.OPEN) {
              this.socket.send('ping');
              console.log('Sent ping to server');
          }
      }, this.pingInterval);
  }
}

// Usage
window.addEventListener('load', () => {
  let wsManager = new WebSocketManager();
  wsManager.connect();
});
