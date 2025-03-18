from flask import Flask
from flask_socketio import SocketIO, emit

print("Starting server...")  # Debugging statement

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow connections from any origin

cart = []  # Shared cart data

@app.route('/')
def index():
    return "<h1>WebSocket server is running.</h1>"

@socketio.on('connect')
def handle_connect():
    print('A client connected')
    emit('cart_update', cart)  # Send current cart to the connected client

@socketio.on('add_item')
def handle_add_item(data):
    cart.append(data['item'])  # Add item to the cart
    emit('cart_update', cart, broadcast=True)  # Broadcast updated cart to all clients

@socketio.on('disconnect')
def handle_disconnect():
    print('A client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)