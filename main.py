import os
import yaml
from redis import Redis

class RedisConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_redis_config(self):
        return self.config.get('redis', {})

class CacheRedisConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = RedisConfig(self.config_file)

    def get_redis_client(self):
        config = self.config.get_redis_config()
        return Redis(host=config['host'], port=config['port'], db=config['db'])

def main():
    config_file = 'config.yaml'
    cache_redis_config = CacheRedisConfig(config_file)
    redis_client = cache_redis_config.get_redis_client()
    print(redis_client.ping())

if __name__ == '__main__':
    main()