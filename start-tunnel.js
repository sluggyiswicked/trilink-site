const localtunnel = require('localtunnel');
const fs = require('fs');

console.log('Starting tunnel connection...');

(async () => {
  try {
    console.log('Requesting tunnel for port 1313...');
    const tunnel = await localtunnel({
      port: 1313,
      host: 'https://loca.lt'
    });

    console.log('Tunnel URL:', tunnel.url);
    console.log('Share this URL with others!');
    fs.writeFileSync('tunnel-url.txt', tunnel.url);

    tunnel.on('close', () => {
      console.log('Tunnel closed');
    });

    tunnel.on('error', (err) => {
      console.error('Tunnel error:', err);
    });
  } catch (err) {
    console.error('Failed to create tunnel:', err);
    process.exit(1);
  }
})();
