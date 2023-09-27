import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const port = 1245;

const client = redis.createClient();
const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

reserveSeatAsync('available_seats', 50);

let reservationEnabled = true;

const queue = kue.createQueue();

app.use(express.json());

// Route for getting the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
  res.json({ numberOfAvailableSeats });
});

// Route for reserving a seat
app.get('/reserve_seat', async (req, res) => {
  const currentAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
  if (reservationEnabled === false || currentAvailableSeats === null || currentAvailableSeats <= 0) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });

  const newAvailableSeats = currentAvailableSeats - 1;
  await reserveSeatAsync('available_seats', newAvailableSeats);

  if (newAvailableSeats === 0) {
    reservationEnabled = false;
  }
});

// Route for processing the reservation queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
  if (currentAvailableSeats !== null && currentAvailableSeats > 0) {
    queue.create('reserve_seat').save((err) => {
      if (err) {
        console.log(`Seat reservation job failed: ${err.message}`);
      }
    });
  } else {
    reservationEnabled = false;
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

