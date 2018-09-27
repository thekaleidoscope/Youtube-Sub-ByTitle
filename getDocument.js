const request = require("request");
const cheerio = require("cheerio");

let path = process.argv[2].split(" ").join("+");
// console.log(path);
var link = "https://www.youtube.com/results?search_query=" + path;

request.get(link, function(error, response, html) {
  // Use cheerio to parse and create the jQuery-like DOM based on the retrieved html string
  let $ = cheerio.load(html);
  console.log(
    "WHAT .." + $("a.yt-simple-endpoint style-scope ytd-video-renderer")
  );
});
