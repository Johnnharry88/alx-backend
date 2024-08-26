import kue from 'kue';

const que = kue.createQueue();

const blacklist = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, alx, done) {
  alx.progress(0, 100);

  if (blacklist.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    alx.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
    done();
  }
}

que.process('push_notification_code_2', 2, (j, done) => {
  const { phoneNumber, message } = j.data;
  sendNotification(phoneNumber, message, j, done);
});
