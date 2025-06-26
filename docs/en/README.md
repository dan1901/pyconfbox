# PyConfBox English Documentation

Welcome to the comprehensive English documentation for PyConfBox!

## 📚 Table of Contents

1. **[Getting Started](getting-started.md)** - Installation and basic usage
2. **[API Reference](api-reference.md)** - Complete API documentation
3. **[Configuration Guide](configuration-guide.md)** - Advanced configuration options
4. **[Storage Backends](storage-backends.md)** - Available storage systems
5. **[Django Integration](django-integration.md)** - Django-specific features
6. **[Examples](examples.md)** - Practical usage examples

## 🚀 Quick Start

```python
from pyconfbox import Config

# Create configuration instance
config = Config(default_storage='environment', fallback_storage='memory')

# Store and retrieve values
config.set('API_KEY', 'your-secret-key', scope='secret', immutable=True)
api_key = config.get('API_KEY', scope='secret')

# Lock all configurations
config.release()
```

## 🔗 Related Links

- **[Main Repository](../../README.md)** - Project overview
- **[Korean Documentation](../ko/README.md)** - 한국어 문서
- **[Package Documentation](../../packages/)** - Individual package docs

## 🤝 Contributing

Found an error or want to improve the documentation? Please:

1. Check existing [issues](https://github.com/dan1901/pyconfbox/issues)
2. Create a pull request with your improvements
3. Follow our documentation style guide

---

**Need help?** Open an [issue](https://github.com/dan1901/pyconfbox/issues) or contact us at edc1901@gmail.com 