# news data ingestion

news_ingestion/
├── app/
│   ├── __init__.py
│   ├── fetch/
│   │   ├── __init__.py
│   │   ├── rss_fetcher.py
│   │   ├── api_fetcher.py
│   ├── process/
│   │   ├── __init__.py
│   │   ├── normalizer.py
│   │   ├── extractor.py
│   ├── store/
│   │   ├── __init__.py
│   │   ├── postgres_store.py
│   │   ├── s3_backup.py
│   ├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── prefect_flow.py
├── config/
│   ├── config.yaml
└── README.md
