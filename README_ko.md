# PyConfBox - 통합 설정 관리 시스템

[![PyPI version](https://badge.fury.io/py/pyconfbox.svg)](https://badge.fury.io/py/pyconfbox)
[![Python Support](https://img.shields.io/pypi/pyversions/pyconfbox.svg)](https://pypi.org/project/pyconfbox/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/dan1901/pyconfbox/actions/workflows/test.yml/badge.svg)](https://github.com/dan1901/pyconfbox/actions/workflows/test.yml)

**PyConfBox**는 Python 애플리케이션에서 환경변수, 시스템변수, 글로벌변수 등 모든 설정을 통합 관리할 수 있는 강력하고 유연한 설정 관리 시스템입니다.

> **한국어 문서**: README_ko.md (현재) | **English Documentation**: [README.md](README.md)

## 📦 패키지 구조

이 저장소는 monorepo 구조로 여러 패키지를 관리합니다:

### 핵심 패키지

- **[pyconfbox](packages/pyconfbox/)** - 메인 패키지 (필수)
  - 핵심 설정 관리 시스템
  - 기본 저장소: Memory, Environment, File, SQLite, Redis
  - 불변성 관리 및 타입 검증

### 플러그인 패키지

- **[pyconfbox-django](packages/pyconfbox-django/)** - Django 통합
  - Django 미들웨어 및 설정 연동
  - `django.conf.settings` 자동 동기화

- **[pyconfbox-mysql](packages/pyconfbox-mysql/)** - MySQL 저장소
  - MySQL 데이터베이스 저장소 지원

- **[pyconfbox-postgresql](packages/pyconfbox-postgresql/)** - PostgreSQL 저장소
  - PostgreSQL 데이터베이스 저장소 지원

- **[pyconfbox-mongodb](packages/pyconfbox-mongodb/)** - MongoDB 저장소
  - MongoDB 문서 데이터베이스 저장소 지원

## 🚀 빠른 시작

### 1. 메인 패키지 설치

```bash
pip install pyconfbox
```

### 2. 기본 사용법

```python
from pyconfbox import Config

# 설정 인스턴스 생성
config = Config(default_storage='environment', fallback_storage='memory')

# 설정 값 저장
config.set('API_KEY', 'your-secret-key', scope='secret', immutable=True)
config.set('DEBUG', True, scope='global')
config.set('DATABASE_URL', 'sqlite:///app.db', scope='env')

# 설정 값 조회
api_key = config.get('API_KEY', scope='secret')
debug_mode = config.get('DEBUG', scope='global')

# 모든 설정 고정 (불변성 적용)
config.release()
```

### 3. 플러그인 설치 (선택사항)

```bash
# Django 통합
pip install pyconfbox-django

# 데이터베이스 저장소
pip install pyconfbox-mysql
pip install pyconfbox-postgresql
pip install pyconfbox-mongodb
```

## 🏗️ 주요 특징

### 🎯 변수 범위 (Scope) 시스템
- **env**: 환경변수
- **global**: 글로벌 변수
- **local**: 로컬 변수  
- **system**: 시스템 변수
- **secret**: 비밀 변수
- **django**: Django 설정 (플러그인)

### 🔒 불변성 (Immutability) 제어
- 개별 설정의 불변성 설정
- `release()` 메서드로 전체 설정 고정
- 불변 설정 수정 시 예외 발생

### 💾 다양한 저장소 지원
- **내장 저장소**: Memory, Environment, File (JSON/YAML/TOML), SQLite, Redis
- **플러그인 저장소**: MySQL, PostgreSQL, MongoDB
- **커스텀 저장소**: `BaseStorage` 상속으로 확장 가능

### 🔧 타입 검증 및 변환
- 자동 타입 감지 및 변환
- 커스텀 타입 변환기 지원
- 타입 안전성 보장

## 📖 문서

각 패키지의 상세한 문서는 해당 패키지 디렉토리의 README.md를 참조하세요:

- [pyconfbox 문서](packages/pyconfbox/README.md)
- [pyconfbox-django 문서](packages/pyconfbox-django/README.md)
- [pyconfbox-mysql 문서](packages/pyconfbox-mysql/README.md)
- [pyconfbox-postgresql 문서](packages/pyconfbox-postgresql/README.md)
- [pyconfbox-mongodb 문서](packages/pyconfbox-mongodb/README.md)

## 🔨 개발

### 전체 빌드

```bash
# 모든 패키지 빌드
python tools/build_all.py
```

### 개별 패키지 빌드

```bash
cd packages/pyconfbox
python -m build
```

### 테스트

```bash
# 메인 패키지 테스트
cd packages/pyconfbox
uv run pytest -v

# 플러그인 테스트
cd packages/pyconfbox-django
pytest -v
```

## 📄 라이선스

MIT License - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 🤝 기여

기여는 언제나 환영합니다! 다음 절차를 따라주세요:

1. 이 저장소를 포크합니다
2. 기능 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다

## 📞 지원

- 🐛 버그 리포트: [GitHub Issues](https://github.com/dan1901/pyconfbox/issues)
- 💡 기능 요청: [GitHub Issues](https://github.com/dan1901/pyconfbox/issues)
- 📧 이메일: edc1901@gmail.com

---

**PyConfBox**로 더 나은 설정 관리를 경험해보세요! 🚀 