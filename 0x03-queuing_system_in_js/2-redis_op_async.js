import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({
  host: 'localhost',
  port: 6379,
});

const getFromClientAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.error(`Error setting value for ${schoolName}: ${error}`);
    } else {
      redis.print(`Reply: ${reply}`);
    }
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getFromClientAsync(schoolName);
    if (value === null) {
      console.log(`No value found for ${schoolName}`);
    } else {
      console.log(`${value}`);
    }
  } catch (error) {
    console.error(`Error fetching value for ${schoolName}: ${error}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
