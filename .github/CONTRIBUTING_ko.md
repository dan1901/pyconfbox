# PyConfBox 기여하기

PyConfBox에 기여해주셔서 감사합니다! 이 문서는 프로젝트 기여를 위한 가이드라인을 제공합니다.

> **한국어 기여 가이드**: CONTRIBUTING_ko.md (현재) | **English Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)

## 📋 목차

- [시작하기](#시작하기)
- [개발 환경 설정](#개발-환경-설정)
- [변경사항 만들기](#변경사항-만들기)
- [문서화](#문서화)
- [테스트](#테스트)
- [풀 리퀘스트 과정](#풀-리퀘스트-과정)
- [코드 스타일](#코드-스타일)

## 🚀 시작하기

1. **GitHub에서 저장소 포크**
2. **로컬에 포크 클론**:
   ```bash
   git clone https://github.com/your-username/pyconfbox.git
   cd pyconfbox
   ```
3. **가상 환경 생성**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
4. **의존성 설치**:
   ```bash
   uv sync
   ```

## 🛠️ 개발 환경 설정

### 프로젝트 구조
- `packages/pyconfbox/` - 메인 패키지
- `packages/pyconfbox-*` - 플러그인 패키지
- `docs/` - 문서
- `tests/` - 테스트 파일

### 개발 모드로 설치
```bash
cd packages/pyconfbox
pip install -e .
```

## 🔄 변경사항 만들기

1. **기능 브랜치 생성**:
   ```bash
   git checkout -b feature/기능-이름
   ```

2. **코딩 표준을 따라 변경사항 작성**

3. **새로운 기능에 대한 테스트 추가**

4. **필요시 문서 업데이트**

5. **테스트 실행으로 정상 작동 확인**:
   ```bash
   uv run pytest
   ```

## 📖 문서화

영어와 한국어 두 언어로 문서를 관리합니다:

- **English**: `docs/en/`
- **한국어**: `docs/ko/`

새로운 기능 추가 시:
1. 두 언어 버전 모두 업데이트
2. 기술적 정확성 일관성 유지
3. 각 언어에 적절한 용어 사용

### 문서 표준
- 명확하고 간결한 언어 사용
- 코드 예제 포함
- 목차 업데이트
- 관련 섹션 상호 참조

## 🧪 테스트

### 테스트 실행
```bash
# 모든 테스트 실행
uv run pytest

# 특정 패키지 테스트 실행
cd packages/pyconfbox
uv run pytest -v

# 커버리지와 함께 실행
uv run pytest --cov=pyconfbox
```

### 테스트 작성
- 모든 새로운 기능에 대한 테스트 작성
- 설명적인 테스트 이름 사용
- 엣지 케이스 포함
- 외부 의존성 모킹

## 📝 풀 리퀘스트 과정

1. **새로운 기능에 대한 문서 업데이트**
2. **변경사항을 다루는 테스트 추가**
3. **모든 테스트 통과 확인**
4. **해당시 변경로그 업데이트**
5. **다음을 포함한 풀 리퀘스트 생성**:
   - 명확한 제목과 설명
   - 관련 이슈 참조
   - UI 변경시 스크린샷

### 풀 리퀘스트 템플릿
```markdown
## 설명
변경사항에 대한 간단한 설명

## 변경 유형
- [ ] 버그 수정
- [ ] 새로운 기능
- [ ] 문서 업데이트
- [ ] 성능 개선

## 테스트
- [ ] 로컬에서 테스트 통과
- [ ] 새로운 테스트 추가
- [ ] 문서 업데이트

## 체크리스트
- [ ] 코드가 스타일 가이드라인을 따름
- [ ] 자체 리뷰 완료
- [ ] 문서 업데이트
```

## 🎨 코드 스타일

### Python 코드
- PEP 8 준수
- 타입 힌트 사용
- 최대 줄 길이: 88자
- 의미있는 변수명 사용

### 도구
코드 품질을 위해 다음 도구들을 사용합니다:
- **ruff** - 린팅 및 포맷팅
- **pytest** - 테스트
- **mypy** - 타입 검사

### Pre-commit 설정
```bash
# pre-commit 훅 설치
pre-commit install

# 수동 실행
pre-commit run --all-files
```

## 🐛 이슈 보고

이슈 보고 시:
1. 이슈 템플릿 사용
2. Python 버전과 OS 포함
3. 최소 재현 예제 제공
4. 에러 메시지와 스택 트레이스 포함

## 💬 도움 받기

- **GitHub Issues**: 버그 및 기능 요청
- **GitHub Discussions**: 질문 및 커뮤니티 지원
- **이메일**: edc1901@gmail.com (직접 연락)

## 📄 라이선스

기여함으로써 귀하의 기여가 MIT 라이선스 하에 라이선스됨에 동의합니다.

---

PyConfBox에 기여해주셔서 감사합니다! 🚀 