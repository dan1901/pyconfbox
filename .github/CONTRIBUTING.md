# Contributing to PyConfBox

We welcome contributions to PyConfBox! This document provides guidelines for contributing to the project.

> **한국어 기여 가이드**: [CONTRIBUTING_ko.md](CONTRIBUTING_ko.md) | **English Guide**: CONTRIBUTING.md (current)

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Documentation](#documentation)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/pyconfbox.git
   cd pyconfbox
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   uv sync
   ```

## 🛠️ Development Setup

### Project Structure
- `packages/pyconfbox/` - Main package
- `packages/pyconfbox-*` - Plugin packages
- `docs/` - Documentation
- `tests/` - Test files

### Installing in Development Mode
```bash
cd packages/pyconfbox
pip install -e .
```

## 🔄 Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Add tests** for new functionality

4. **Update documentation** if needed

5. **Run tests** to ensure everything works:
   ```bash
   uv run pytest
   ```

## 📖 Documentation

We maintain documentation in both English and Korean:

- **English**: `docs/en/`
- **한국어**: `docs/ko/`

When adding new features:
1. Update both language versions
2. Keep technical accuracy consistent
3. Use appropriate terminology for each language

### Documentation Standards
- Use clear, concise language
- Include code examples
- Update table of contents
- Cross-reference related sections

## 🧪 Testing

### Running Tests
```bash
# Run all tests
uv run pytest

# Run specific package tests
cd packages/pyconfbox
uv run pytest -v

# Run with coverage
uv run pytest --cov=pyconfbox
```

### Writing Tests
- Write tests for all new functionality
- Use descriptive test names
- Include edge cases
- Mock external dependencies

## 📝 Pull Request Process

1. **Update documentation** for any new features
2. **Add tests** that cover your changes
3. **Ensure all tests pass**
4. **Update the changelog** if applicable
5. **Create a pull request** with:
   - Clear title and description
   - Reference to related issues
   - Screenshots if UI changes

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Updated documentation

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
```

## 🎨 Code Style

### Python Code
- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters
- Use meaningful variable names

### Tools
We use these tools for code quality:
- **ruff** for linting and formatting
- **pytest** for testing
- **mypy** for type checking

### Pre-commit Setup
```bash
# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## 🐛 Reporting Issues

When reporting issues:
1. Use the issue template
2. Include Python version and OS
3. Provide minimal reproduction example
4. Include error messages and stack traces

## 💬 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community support
- **Email**: edc1901@gmail.com for direct contact

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to PyConfBox! 🚀 