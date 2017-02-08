//Using node module to bulk ingest data in CSV format
//To run: node ingest.js 

var ElasticsearchCSV = require('elasticsearch-csv');

// create an instance of the importer with options
var esCSV = new ElasticsearchCSV({
    es: { index: 'markets', type: 'product', host: '0.0.0.0' },
    csv: { filePath: '/products.csv', headers: true }
});

esCSV.import()
    .then(function (response) {
        // Elasticsearch response for the bulk insert
        console.log(response);
    }, function (err) {
        // throw error
        console.log(err);
        throw err;
    });
