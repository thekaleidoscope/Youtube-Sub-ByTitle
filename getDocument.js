var http = require("http");

let path = process.argv[2].split(" ").join("+");
// console.log(path);
var options = "https://www.youtube.com/results?search_query=" + path;
const getScript = url => {
  return new Promise((resolve, reject) => {
    const http = require("http"),
      https = require("https");

    let client = http;

    if (url.toString().indexOf("https") === 0) {
      client = https;
    }

    client
      .get(url, resp => {
        let data = "";

        // A chunk of data has been recieved.
        resp.on("data", chunk => {
          data += chunk;
        });

        // The whole response has been received. Print out the result.
        resp.on("end", () => {
          resolve(data);
        });
      })
      .on("error", err => {
        reject(err);
      });
  });
};

(async url => {
  console.log(await getScript(url));
})(options);
