import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
const client = redis.createClient();
const asyncGet = promisify(client.get).bind(client);

const app = express();
const port = 1245;

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    InitialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 0,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}

client
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.meesage}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await asyncGet(`item.${itemId}`);
  return stock;
}

const notfound = { status: 'Product not found' };

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json(notfound);
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  console.log(currentStock);
  const stock = currentStock !== null ? currentStock : item.stock;
  console.log(stock);

  item.currentQuantity = stock;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  const noStock = { status: 'Not enough stock available', itemId };
  const reserveConfirm = { status: 'Reservation confirmed', itemId };

  if (!item) {
    res.json(notfound);
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) currentStock = item.stock;

  if (currentStock <= 0) {
    res.json(noStock);
    return;
  }

  reserveStockById(itemId, Number(currentStock) - 1);
  res.json(reserveConfirm);
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
