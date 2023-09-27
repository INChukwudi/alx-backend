import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = redis.createClient();
const getFromClientAsync = promisify(client.get).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.itemId === id);
};

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
};

async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getFromClientAsync(`item.${itemId}`);
  return parseInt(reservedStock) || 0;
};

app.use(express.json());

// Route for getting a list of all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route for getting product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  product.currentQuantity = product.initialAvailableQuantity - currentReservedStock;
  res.json(product);
});

// Route for product reservation by itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const availableStock = product.initialAvailableQuantity - currentReservedStock;

  if (availableStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  reserveStockById(itemId, currentReservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

