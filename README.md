# cache-redis-config
======================

## Description
---------------

cache-redis-config is a lightweight, open-source configuration manager for Redis caching. It provides a simple and intuitive API for managing Redis connections, cache keys, and expiration times, making it easy to integrate Redis caching into your application.

## Features
------------

*   **Multi-Redis Support**: cache-redis-config allows you to connect to multiple Redis instances, each with its own set of configuration options.
*   **Cache Key Management**: Easily manage cache keys, including setting expiration times, TTLs, and namespace prefixes.
*   **Configurable Cache Behavior**: Control cache behavior, including cache invalidation, cache expiration, and cache eviction policies.
*   **Extensive Logging and Debugging**: cache-redis-config provides detailed logging and debugging capabilities to help you diagnose issues and optimize performance.

## Technologies Used
----------------------

*   **Node.js**: cache-redis-config is built on top of Node.js and utilizes its event-driven, non-blocking I/O model.
*   **Redis**: cache-redis-config uses the Redis client library to interact with Redis instances.
*   **TypeScript**: cache-redis-config is written in TypeScript for improved code maintainability, readability, and scalability.

## Installation
--------------

To install cache-redis-config, run the following command in your terminal:

```bash
npm install cache-redis-config
```

## Usage
-----

### Importing the Module

```javascript
const { RedisConfig, CacheManager } = require('cache-redis-config');
```

### Creating a Redis Configuration

```javascript
const redisConfig = new RedisConfig({
  host: 'localhost',
  port: 6379,
  password: 'your_redis_password',
  db: 0,
});
```

### Creating a Cache Manager

```javascript
const cacheManager = new CacheManager({
  redisConfig,
  cacheKeys: {
    namespace: 'your_namespace',
    prefix: 'your_prefix',
  },
  cacheExpiration: 3600, // 1 hour
});
```

### Setting and Getting Cache Values

```javascript
cacheManager.set('key1', 'value1', (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log(result);
  }
});

cacheManager.get('key1', (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log(result);
  }
});
```

## Contributing
--------------

We welcome contributions to cache-redis-config. Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License
---------

cache-redis-config is licensed under the [MIT License](LICENSE).