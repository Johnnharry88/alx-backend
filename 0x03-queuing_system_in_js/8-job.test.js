import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const que = kue.createQueue();

describe('createPushNofiticationsJobs', () => {
  before(() => {
    que.testNode.enter();
  });

  afterEach(() => {
    que.testNode.clear();
  })

  after(() => {
    que.testNode.exit();
  });

  it("if jobs is not an array passing Number", () => {
    expect(() => {
      createPushNotificationsJobs(2, que);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an arrya passing object", () => {
    expect(() => {
      createPushNotificationsJob({}, que);
    }).to.throw("Jobs is not an array");
  })

  it("if jobs is not an array passing String", () => {
    expect(() => {
      createPushNotificationsJobs("Hello", que);
    }).to.throw("Jobs is not an array");
  });
});
