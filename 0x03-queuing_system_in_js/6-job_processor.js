import kue from 'kue';

const que = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

que.process('push_notification_code', (task, done) => {
  const { phoneNumber, message } = task.data;
  sendNotification(phoneNumber, message);
  done();
});
