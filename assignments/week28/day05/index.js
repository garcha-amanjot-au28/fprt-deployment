const express = require("express");
const app = express();
const Promise = require("promise");
port = 3000;

const fs = require("fs");

app.get("/", (req, res) => {
  res.send(`<a href="/fileone">Fileone</a></br> <a href="/filetwo">Filetwo</a> 
  <h1>hello Home !!</h1>`);
});

app.get("/fileone", (req, res) => {
  fs.readFile("./fileone.txt", "utf8", (err, data) => {
    if (err) throw err;
    res.send(`<a href="/">Home</a><h1>This is File one </h1> <p>${data} </p>`);
  });
});

app.get("/filetwo", (req, res) => {
  fs.readFile("./filetwo.txt", "utf8", (err, data) => {
    if (err) throw err;
    res.send(`<a href="/">Home</a><h1>This is File two </h1> <p>${data} </p>`);
  });
});

app.use((req, res, next) => {
  res.send(`<h1>page not found</h1>`);
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
