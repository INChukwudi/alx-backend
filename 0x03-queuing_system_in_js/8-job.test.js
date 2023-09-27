import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: 'redis://localhost:6379' });
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create jobs with valid job data', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 1234 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    const jobIds = queue.testMode.jobs.map((job) => job.id);
    expect(jobIds).to.include('1');
    expect(jobIds).to.include('2');
  });

  it('should create jobs and verify the type and data', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 1234 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const createdJobs = queue.testMode.jobs;
    createdJobs.forEach((job) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.have.property('phoneNumber');
      expect(job.data).to.have.property('message');
    });
  });

  it('should throw an error for invalid jobs parameter', () => {
    const invalidJobsArray = 'not_an_array';

    expect(() => createPushNotificationsJobs(invalidJobsArray, queue)).to.throw('Jobs is not an array');
    expect(queue.testMode.jobs.length).to.equal(0);
  });
});

