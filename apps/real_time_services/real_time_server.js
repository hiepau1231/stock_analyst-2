const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Real-time server is running');
});

io.on('connection', (socket) => {
  console.log('A user connected');

  socket.on('disconnect', () => {
    console.log('User disconnected');
  });

  // Add more socket event handlers here
});

http.listen(PORT, () => {
  console.log(`Real-time server running on port ${PORT}`);
});
