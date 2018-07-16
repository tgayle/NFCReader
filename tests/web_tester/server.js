const express = require('express');
const mustache = require('mustache');
const app = express()
app.set('view engine', 'ejs');
app.use(express.static('public'));

let currentId = ''
let atqa = ''
let sak = ''
let ats = ''

const defaults = {
  atqa: '00 00',
  sak: '00',
  ats: '00 00 00 00'
}


app.get('/', function (req, res) {
  res.render('index', getCurrentCardInfo())
})

app.get('/id', function(req, res) {
  res.json(getCurrentCardInfo())
})

app.post('id', function (req, res) {
  currentId = ''
  res.json(getCurrentCardInfo())
})

app.post('/id/:new_id', function (req, res) {
  currentId = req.params.new_id
  res.json(getCurrentCardInfo())
})

app.listen(3000, function () {
  console.log('listening on port 3000')
})

let getCurrentCardInfo = () => {
  return {
    uid: currentId,
    atqa: atqa,
    sak: sak,
    ats: ats
  }
}