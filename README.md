# PyConfBox - Unified Configuration Management System

[![PyPI version](https://badge.fury.io/py/pyconfbox.svg)](https://badge.fury.io/py/pyconfbox)
[![Python Support](https://img.shields.io/pypi/pyversions/pyconfbox.svg)](https://pypi.org/project/pyconfbox/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/dan1901/pyconfbox/workflows/Tests/badge.svg)](https://github.com/dan1901/pyconfbox/actions)

**PyConfBox** is a powerful and flexible configuration management system for Python applications that provides unified management of environment variables, system variables, global variables, and more.

> **한국어 문서**: [README_ko.md](README_ko.md) | **English Documentation**: README.md (current)

## 📦 Package Structure

This repository is organized as a monorepo managing multiple packages:

### Core Package

- **[pyconfbox](packages/pyconfbox/)** - Main package (required)
  - Core configuration management system
  - Built-in storages: Memory, Environment, File, SQLite, Redis
  - Immutability management and type validation

### Plugin Packages

- **[pyconfbox-django](packages/pyconfbox-django/)** - Django Integration
  - Django middleware and settings integration
  - Automatic synchronization with `django.conf.settings`

- **[pyconfbox-mysql](packages/pyconfbox-mysql/)** - MySQL Storage
  - MySQL database storage backend support

- **[pyconfbox-postgresql](packages/pyconfbox-postgresql/)** - PostgreSQL Storage
  - PostgreSQL database storage backend support

- **[pyconfbox-mongodb](packages/pyconfbox-mongodb/)** - MongoDB Storage
  - MongoDB document database storage backend support

## 🚀 Quick Start

### 1. Install Core Package

```bash
pip install pyconfbox
```

### 2. Basic Usage

```python
from pyconfbox import Config

# Create configuration instance
config = Config(default_storage='environment', fallback_storage='memory')

# Store configuration values
config.set('API_KEY', 'your-secret-key', scope='secret', immutable=True)
config.set('DEBUG', True, scope='global')
config.set('DATABASE_URL', 'sqlite:///app.db', scope='env')

# Retrieve configuration values
api_key = config.get('API_KEY', scope='secret')
debug_mode = config.get('DEBUG', scope='global')

# Lock all configurations (apply immutability)
config.release()
```

### 3. Install Plugins (Optional)

```bash
# Django integration
pip install pyconfbox-django

# Database storage backends
pip install pyconfbox-mysql
pip install pyconfbox-postgresql
pip install pyconfbox-mongodb
```

## 🏗️ Key Features

### 🎯 Scope System
- **env**: Environment variables
- **global**: Global variables
- **local**: Local variables  
- **system**: System variables
- **secret**: Secret variables
- **django**: Django settings (plugin)

### 🔒 Immutability Control
- Individual configuration immutability settings
- Global configuration locking with `release()` method
- Exception throwing when attempting to modify immutable settings

### 💾 Multiple Storage Backends
- **Built-in storages**: Memory, Environment, File (JSON/YAML/TOML), SQLite, Redis
- **Plugin storages**: MySQL, PostgreSQL, MongoDB
- **Custom storages**: Extensible via `BaseStorage` inheritance

### 🔧 Type Validation and Conversion
- Automatic type detection and conversion
- Custom type converter support
- Type safety guarantees

## 📖 Documentation

For detailed documentation of each package, refer to the README.md in the respective package directory:

- [pyconfbox Documentation](packages/pyconfbox/README.md)
- [pyconfbox-django Documentation](packages/pyconfbox-django/README.md)
- [pyconfbox-mysql Documentation](packages/pyconfbox-mysql/README.md)
- [pyconfbox-postgresql Documentation](packages/pyconfbox-postgresql/README.md)
- [pyconfbox-mongodb Documentation](packages/pyconfbox-mongodb/README.md)

## 🔨 Development

### Build All Packages

```bash
# Build all packages
python tools/build_all.py
```

### Build Individual Package

```bash
cd packages/pyconfbox
python -m build
```

### Testing

```bash
# Test main package
cd packages/pyconfbox
uv run pytest -v

# Test plugins
cd packages/pyconfbox-django
pytest -v
```

## 📄 License

MIT License - See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 📞 Support

- 🐛 Bug Reports: [GitHub Issues](https://github.com/dan1901/pyconfbox/issues)
- 💡 Feature Requests: [GitHub Issues](https://github.com/dan1901/pyconfbox/issues)
- 📧 Email: edc1901@gmail.com

---

Experience better configuration management with **PyConfBox**! 🚀
