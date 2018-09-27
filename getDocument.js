var http = require("http");

let path = process.argv[2].split(" ").join("+");
console.log(path);
// var options = {
//   host: "https://www.youtube.com/results?search_query=",
//   path: path
// };
// var request = http.request(options, function(res) {
//   var data = "";
//   res.on("data", function(chunk) {
//     data += chunk;
//   });
//   res.on("end", function() {
//     console.log(data);
//   });
// });
// request.on("error", function(e) {
//   console.log(e.message);
// });
// request.end();
