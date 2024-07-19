const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const db = new sqlite3.Database('mydatabase.db'); // Используйте файл базы данных

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname)));



// Создаем таблицу для хранения данных формы
db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, birthDate TEXT, salary INTEGER)");
});

// Маршрут для обработки данных формы
app.post('/submit', (req, res) => {
  const { firstName, lastName, birthDate, salary } = req.body;

  console.log('Form data received:', { firstName, lastName, birthDate, salary });

  // Вставка нового сотрудника без указания ID, он будет автоматически присвоен
  db.run("INSERT INTO employees (firstName, lastName, birthDate, salary) VALUES (?, ?, ?, ?)", [firstName, lastName, birthDate, salary], function(err) {
    if (err) {
      console.error("Error inserting data:", err.message);
      return res.status(500).send("Error inserting data: " + err.message);
    }
    console.log("New employee added with ID:", this.lastID);
    res.redirect('/');
  });
});

// Маршрут для получения всех сотрудников
app.get('/employees', (req, res) => {
  db.all("SELECT * FROM employees", [], (err, rows) => {
    if (err) {
      console.error("Error retrieving employees:", err.message);
      return res.status(500).send("Error retrieving data: " + err.message);
    }
    res.json(rows);
  });
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
