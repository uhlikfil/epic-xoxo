var express = require('express');
var router = express.Router();
var path = require('path')

/* GET home page. */
router.get('/admin', function(req, res, next) {
  res.sendFile(path.resolve('public/admin.html'))
});
router.get('/*', function(req, res, next) {
  console.log();
  res.sendFile(path.resolve('public/index.html'))
});

module.exports = router;
