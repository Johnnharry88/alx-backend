import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, resp) => {
    print(`Replyy: ${resp}`);
  });
}

async function displaySchoolValue(schoolName) {
  const resp = await getAsync(schoolName);
  console.log(resp);
}

(async () => {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  displaySchoolValue("HolbertonSanFrancisco");
})();
