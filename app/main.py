# from dotenv import load_dotenv
import os
import yaml
from fetch import api_fetcher, rss_fetcher
from process import normalizer
from store import postgres_store

# load_dotenv()

def load_config():
    # load the config file
    with open('app/config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # override the config postgres config with the container's postgres config
    config['postgres'] =  {
            "host": os.getenv('POSTGRES_HOST', config['postgres']['host']),
            "port": os.getenv('POSTGRES_PORT', config['postgres']['port']),
            "user": os.getenv('POSTGRES_USER', config['postgres']['user']),
            "password": os.getenv('POSTGRES_PASSWORD', config['postgres']['password']),
            "database": os.getenv('POSTGRES_DB', config['postgres']['database'])
    }
    return config


def main():
    config = load_config()
    # fetch the data
    api_data = api_fetcher.fetch_news_via_api(config['news_api_url'], api_key=config['api_key'])
    rss_data =  rss_fetcher.fetch_rss_feeds(url= config['news_api_url'])

    # process the data
    normalized_data = normalizer.normalize_data(data=api_data +  rss_data)

    # store the data
    postgres_store.store_in_postgres(record=normalized_data, db_config=config['postgres'] )


if __name__ == '__main__':
    main()