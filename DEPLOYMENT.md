# PicDrop 배포 가이드

## 📋 사전 준비

### 1. Cloudinary 계정 설정
1. https://cloudinary.com 가입 (무료 티어: 25GB/월)
2. Dashboard에서 `CLOUDINARY_URL` 복사
   - 형식: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`

### 2. Railway 계정 설정
1. https://railway.app 가입
2. GitHub 연동 권장 (자동 배포)

## 🚀 Railway 배포 방법

### Option 1: Railway CLI로 배포 (추천)

```bash
# 1. Railway 로그인
railway login

# 2. 새 프로젝트 생성
railway init

# 3. PostgreSQL 추가
railway add

# 4. 환경변수 설정
railway variables set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
railway variables set DEBUG=False
railway variables set ALLOWED_HOSTS=your-app.railway.app
railway variables set CLOUDINARY_URL=cloudinary://your-credentials
railway variables set CSRF_TRUSTED_ORIGINS=https://your-app.railway.app

# 5. 배포
railway up
```

### Option 2: GitHub 연동 (자동 배포)

1. GitHub에 저장소 생성 및 푸시
```bash
git remote add origin https://github.com/username/picdrop.git
git push -u origin main
```

2. Railway 대시보드에서:
   - New Project → Deploy from GitHub repo
   - 저장소 선택
   - PostgreSQL 서비스 추가
   - 환경변수 설정 (위와 동일)

## 🔐 환경변수 목록

Railway 대시보드 또는 CLI로 다음 환경변수 설정:

| 변수명 | 값 | 비고 |
|--------|-----|------|
| `SECRET_KEY` | 랜덤 문자열 | Django secret key |
| `DEBUG` | `False` | 프로덕션에서는 반드시 False |
| `ALLOWED_HOSTS` | `your-app.railway.app` | Railway 도메인 |
| `DATABASE_URL` | (자동 생성) | Railway PostgreSQL |
| `CLOUDINARY_URL` | `cloudinary://...` | Cloudinary 대시보드에서 복사 |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.railway.app` | HTTPS 포함 |

## ✅ 배포 후 체크리스트

### 1. 관리자 계정 생성
```bash
railway run python manage.py createsuperuser
```

### 2. 서비스 동작 확인
- [ ] 메인 페이지 접속
- [ ] 이벤트 생성
- [ ] QR 코드 생성 확인
- [ ] 이미지 업로드
- [ ] 라이브 월 실시간 갱신
- [ ] 관리자 페이지 접속

### 3. 성능 모니터링
- Railway 대시보드에서 메트릭 확인
- 무료 티어: $5 크레딧/월
- 예상 사용량: 500MB RAM, 0.1 vCPU

## 🔧 트러블슈팅

### 정적 파일이 안 보일 때
```bash
railway run python manage.py collectstatic --noinput
```

### 데이터베이스 마이그레이션 실패
```bash
railway run python manage.py migrate --run-syncdb
```

### 로그 확인
```bash
railway logs
```

## 📊 모니터링

- Railway 대시보드: https://railway.app/dashboard
- Cloudinary 사용량: https://cloudinary.com/console
- 애플리케이션 로그: `railway logs` 또는 대시보드

## 🔄 업데이트 배포

### CLI 사용 시
```bash
git add .
git commit -m "Update features"
railway up
```

### GitHub 연동 시
```bash
git push origin main
# Railway가 자동으로 배포
```

## 💰 비용 관리

### Railway 무료 티어
- $5 크레딧/월
- 예상 소진 시간: 약 500시간 (항상 실행 시)
- 권장: 사용하지 않을 때 sleep 설정

### Cloudinary 무료 티어
- 저장공간: 25GB
- 대역폭: 25GB/월
- 변환: 25,000건/월

## 🎯 다음 단계

1. 커스텀 도메인 연결 (선택)
2. CDN 설정 (Cloudinary가 자동 처리)
3. 백업 설정 (Railway 자동 백업)
4. 모니터링 알림 설정
5. 사용자 피드백 수집

---

**배포 완료 시 확인 사항:**
- ✅ 배포된 URL
- ✅ 관리자 계정 정보 (안전하게 보관)
- ✅ 환경변수 백업
- ✅ 전체 기능 테스트 완료
