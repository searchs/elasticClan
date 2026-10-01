# elasticClan — Historical Elasticsearch Engineering Lab

elasticClan is retained as a **historical search-engineering lab** covering Elasticsearch ingestion, indexing and search experiments built around the ELK ecosystem.

The repository reflects earlier Elasticsearch/Kibana/Logstash APIs and operational assumptions. It is useful for understanding search/data-ingestion patterns and past implementation work, but it should not be treated as a current production Elasticsearch baseline.

## What this repository contains

- merchant/deal ingestion experiments
- Elasticsearch index-creation and setup scripts
- CSV/JSON transformation and ingestion utilities
- Logstash configuration experiments
- Docker/ELK environment material
- operational shell scripts from the original lab
- search-oriented example material under `examples/`

## City-search example

`examples/city-search/` contains the durable design notes migrated from the former `markets` repository. The original large city dataset and obsolete vendored Elasticsearch browser client were deliberately not migrated; the example preserves the useful search-model and architecture ideas without carrying obsolete dependencies.

## Historical context

The original product experiment explored pulling catalogue/deal data from multiple merchants and making it searchable through Elasticsearch. That product concept is no longer presented as an active commercial application; the engineering value now lies in the ingestion and search patterns.

Many commands and configurations in this repository pre-date current Elasticsearch security defaults, typed-API removals and modern client conventions. Before reusing any code, revisit:

- supported Elasticsearch/client versions
- authentication, TLS and network exposure
- mappings and index lifecycle management
- bulk-ingestion/back-pressure behaviour
- observability and failure handling
- secrets/configuration management
- container and orchestration configuration

## Retention policy

Keep this repository as historical authored engineering work. New Elasticsearch/search implementations should be built in an actively maintained project, selectively carrying forward validated ideas rather than modernising this repository wholesale.
