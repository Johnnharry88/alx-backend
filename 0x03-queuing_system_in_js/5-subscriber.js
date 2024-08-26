import { createClient } from 'redis';

const subsx = createClient();

subsx.on('connect', function() {
  console.log('Redis client connected to the server');
});

subsx.on('error', function(error) {
  console.error(`Redis client no connected to the server: ${error.message}`);
});

subsx.subscribe('holberton school channel');

subsx.on('message', function(channel, message) {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subsx.unsubscribe(channel);
    subsx.quit();
  }
});
