const http = require('http');
const scrapedin = require('scrapedin')

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
});

server.listen(port, hostname, () => {

});

const start = async function(){
  const profileScraper = await scrapedin({ email: 'ohjeezrickohjeez@gmail.com', password: 'rickandmorty' })
  const profile = await profileScraper(process.argv[2])
  console.log(profile)
  process.exit()
  return profile
} 

return start();
process.exit()


