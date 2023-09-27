import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0801-576-2351',
  message: 'Sample notification message.',
};

const job = queue.create('push_notification_code', jobData)
  .priority('high')
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating notification job:', err);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.error('Notification job failed', err);
});

