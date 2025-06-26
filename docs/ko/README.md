# PyConfBox 한국어 문서

PyConfBox의 포괄적인 한국어 문서에 오신 것을 환영합니다!

## 📚 목차

1. **[시작하기](getting-started.md)** - 설치 및 기본 사용법
2. **[API 참조](api-reference.md)** - 완전한 API 문서
3. **[설정 가이드](configuration-guide.md)** - 고급 설정 옵션
4. **[저장소 백엔드](storage-backends.md)** - 사용 가능한 저장소 시스템
5. **[Django 통합](django-integration.md)** - Django 전용 기능
6. **[예제](examples.md)** - 실용적인 사용 예제

## 🚀 빠른 시작

```python
from pyconfbox import Config

# 설정 인스턴스 생성
config = Config(default_storage='environment', fallback_storage='memory')

# 값 저장 및 조회
config.set('API_KEY', 'your-secret-key', scope='secret', immutable=True)
api_key = config.get('API_KEY', scope='secret')

# 모든 설정 고정
config.release()
```

## 🔗 관련 링크

- **[메인 저장소](../../README_ko.md)** - 프로젝트 개요
- **[English Documentation](../en/README.md)** - 영어 문서
- **[패키지 문서](../../packages/)** - 개별 패키지 문서

## 🤝 기여하기

문서에서 오류를 발견했거나 개선하고 싶으시다면:

1. 기존 [이슈](https://github.com/dan1901/pyconfbox/issues)를 확인해주세요
2. 개선사항과 함께 풀 리퀘스트를 생성해주세요
3. 문서 스타일 가이드를 따라주세요

---

**도움이 필요하신가요?** [이슈](https://github.com/dan1901/pyconfbox/issues)를 생성하거나 edc1901@gmail.com으로 연락주세요 