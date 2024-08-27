import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';
import express from 'express';

const client = redis.createClient();
const que = kue.createQueue();
const app = express();
const port = 1245;
const getClient = promisify(client.get).bind(client);
const setClient = promisify(client.set).bind(client);

const reserveSeat = async (number) => await setClient('available_seats', number);
const getCurrentAvailableSeats = async () => await getClient('available_seats');

let reserveEnable;

app.get('/available_seats', async (req, res) => {
  const numberOfSeatsAvailable = await getCurrentAvailableSeats();
  res.json({numberOfSeatsAvailable});
});

app.get('/reserve_seat', async (req, res) => {
  if (!reserveEnable) res.json({ "status": "Reservation are blocked" });
  let availableSeats = await getCurrentAvailableSeats();
  const job = que.create('reserve_seat', {availableSeats}).save((err) => {
    if (!err) {
      res.json({ status: "Reservation in process" })
    } else {
      res.json({ status: "Reservation failed" });
    };
  });
  job.on('failed', (err) => console.log(`Seat reservation job ${job.id} failed: ${err}`));
  job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`));
});

app.get('/process', async (req, res) => {
  que.process('reserve_seat', async (job, done) => {
    console.log(job.data.availableSeats);
    let availableSeats = await getCurrentAvailableSeats();
    if (job.data.availableSeats <= 0) done(Error('Not enough seats available'));
    const updatedAvailableSeats = Number(job.data.availableSeats) - 1
    await reserveSeat(updatedAvailableSeats);
    if (updatedAvailableSeats === 0) reserveEnable = false;
    done();
  });
  res.json({ status: "Queue processing" });
});

app.listen(port, () => {
  reserveSeat(50);
  reserveEnable = true;
  console.log(`Server is Running in ` + port)
});
