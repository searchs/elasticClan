# City Search Example

This example consolidates the useful search/indexing lessons from the retired `markets` repository without carrying its 12.9 MB city dataset, vendored Elasticsearch browser client, or Elasticsearch 6/7-era typed APIs.

## Original learning goals

- create a searchable city index
- bulk-index JSON documents
- expose a simple HTTP search endpoint
- query Elasticsearch by city name
- run Elasticsearch locally with Docker

## Modernised direction

Use a current Elasticsearch/OpenSearch client and typeless indices. Keep dataset loading separate from the query API and use the bulk helper rather than constructing one very large in-memory request manually.

Pseudo-flow:

```text
city dataset
    |
    v
normalise records
    |
    v
bulk index -> cities index
                 |
                 v
            search API
                 |
                 v
          match city name
```

### Indexing considerations

- validate each city record before indexing
- use deterministic document IDs when a stable source identifier exists
- batch records to bound memory use
- collect and report partial bulk failures
- avoid deprecated mapping types such as `_type`

### Search considerations

- bound result size and paginate rather than returning hundreds of records by default
- validate/normalise user query input
- keep Elasticsearch connection settings in environment/configuration rather than source code
- add integration tests against a disposable container

## Provenance

Consolidated from `searchs/markets`, an authored 2020 Elasticsearch/Express experiment. The large `cities.json` file and bundled `elasticsearch.min.js` were intentionally not migrated.
