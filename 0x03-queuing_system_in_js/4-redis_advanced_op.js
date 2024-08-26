import { createClient, print } from "redis";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

const name = "HolbertonSchools";
const set = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};
for (const [k, v] of Object.entries(set)) {
  client.hset(name, k, v, (_, resp) => print(`Reply: ${resp}`));
}
client.hgetall(name, (_, resp) => console.log(resp));
