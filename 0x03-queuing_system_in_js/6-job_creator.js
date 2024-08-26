import kue from 'kue';

const que = kue.createQueue();

const dataP = {
  phoneNumber: '2348033999309',
  message: 'This is the code to verify your account',
};

const task = que.create('push_notification_code', dataP).save(
  (err) => {
    if (!err) console.log(`Notification job created: ${task.id}`);
  });
task.on('complete', () => console.log('Notification job completed'));
task.on('failed', () => console.log('Notification job failed'));
