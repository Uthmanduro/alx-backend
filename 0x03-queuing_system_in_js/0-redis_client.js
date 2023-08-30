import { createClient } from 'redis';

const newClient = async () => {
    const client = createClient();

    client.on('error', err => console.log('Redis client not connected to the server: ', err));

    client.on('ready', async () => {
      console.log('Redis client connected to the server');

      await client.set('key', 'value');
      const value = await client.get('key');
    });
}

newClient();
