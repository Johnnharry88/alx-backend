export default function createPushNotificationsJobs( jobs, queue) {
  if (Object.getPrototypeOf(jobs) !== Array.prototype) throw Error('Jobs is not an array');
  jobs.forEach((j) => {
    const task = queue.create('push_notification_code_3', j).save(
      (err) => {
        if (!err) console.log(`Notification job created: ${task.id}`);
      });
    task.on('complete', () => console.log(`Notification job ${task.id} completed`));
    task.on('failed', (err) => console.log(`Notification job ${task.id} failed ${err}`));
    task.on('progress', (progress) => console.log(`Notification job ${task.id} ${progress}% complete`));
  });
}
