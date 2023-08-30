import { createClient } from 'redis';
const redis = require('redis');

const client = createClient();
client.on('error', err => console.log('Redis client not connected to the server: ', err));

const setNewSchool = async (schoolName, value) => {
    await client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
    const result = await client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

client.on('ready', async () => {
    console.log('Redis client connected to the server');
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
