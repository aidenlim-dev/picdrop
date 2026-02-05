# 🚀 PicDrop 빠른 배포 가이드

## ⚡ 5분 안에 배포하기

### 1단계: GitHub에 푸시 (1분)

```bash
cd /Users/aiwoojae/.openclaw/workspace/projects/picdrop

# GitHub에 새 저장소 만들기 (https://github.com/new)
# 저장소 이름: picdrop

# 원격 저장소 연결 및 푸시
git remote add origin https://github.com/YOUR_USERNAME/picdrop.git
git branch -M main
git push -u origin main
```

### 2단계: Cloudinary 설정 (1분)

1. https://cloudinary.com 가입
2. Dashboard → Account Details
3. `CLOUDINARY_URL` 복사 (예: `cloudinary://123456:abcdef@cloud-name`)

### 3단계: Railway 배포 (3분)

1. https://railway.app 접속 및 로그인
2. **New Project** 클릭
3. **Deploy from GitHub repo** 선택
4. `picdrop` 저장소 선택
5. **Add PostgreSQL** 클릭 (데이터베이스 자동 추가)

### 4단계: 환경변수 설정

Railway 프로젝트 → **Variables** 탭에서 다음 추가:

#### 필수 환경변수:
```bash
# Django Secret Key (새로 생성)
SECRET_KEY=django-insecure-CHANGE-THIS-TO-RANDOM-50-CHARS

# 디버그 모드 끄기
DEBUG=False

# Cloudinary (3단계에서 복사한 값)
CLOUDINARY_URL=cloudinary://123456:abcdef@your-cloud-name
```

#### 배포 후 추가할 환경변수:
Railway가 배포를 완료하면 도메인이 생성됩니다 (예: `picdrop-production-abc123.railway.app`)

다시 Variables 탭에서 추가:
```bash
ALLOWED_HOSTS=picdrop-production-abc123.railway.app
CSRF_TRUSTED_ORIGINS=https://picdrop-production-abc123.railway.app
```

### 5단계: 관리자 계정 생성

Railway 대시보드 → **Settings** → **Project Settings** → **Project Canvas** → 서비스 클릭 → **Deployments** 탭에서 현재 배포 클릭

오른쪽 상단 **Start Shell** 클릭 후:

```bash
python manage.py createsuperuser
```

입력:
- Username: admin
- Email: your-email@example.com  
- Password: (강력한 비밀번호)

---

## ✅ 배포 완료! 테스트하기

### 1. 메인 페이지 접속
`https://your-app.railway.app`

### 2. 관리자 페이지
`https://your-app.railway.app/admin`

### 3. 전체 플로우 테스트
1. 이벤트 생성 (admin에서 또는 직접 구현한 UI)
2. QR 코드 확인
3. 모바일로 QR 스캔 → 사진 업로드
4. 라이브 월에서 실시간 확인

---

## 🐛 문제 해결

### "Application failed to respond" 에러
→ Railway 로그 확인: 대시보드에서 **View Logs** 클릭

### 정적 파일(CSS/JS) 안 보임
→ 배포가 완료될 때까지 대기 (최대 5분)
→ 여전히 안 보이면 환경변수 확인

### 이미지 업로드 실패
→ `CLOUDINARY_URL` 환경변수 확인
→ Cloudinary 대시보드에서 크레딧 확인

### DATABASE_URL이 없다는 에러
→ PostgreSQL 서비스가 추가됐는지 확인
→ 없으면 **New** → **Database** → **Add PostgreSQL**

---

## 📊 배포 정보

### 무료 티어 한도
- **Railway**: $5 크레딧/월 (약 500시간 실행)
- **Cloudinary**: 25GB 저장/전송, 25k 변환/월

### 예상 리소스 사용량
- **메모리**: ~300-500MB
- **CPU**: ~0.1 vCPU (대기 시)
- **스토리지**: PostgreSQL ~100MB

### 모니터링
- Railway 대시보드에서 실시간 메트릭 확인
- 크레딧 소진율 주시

---

## 🎯 결과물 체크리스트

배포 완료 시 다음을 확인하세요:

- [ ] 배포된 URL 작동 확인
- [ ] 관리자 계정 로그인 성공
- [ ] 이벤트 생성 가능
- [ ] QR 코드 생성 확인
- [ ] 이미지 업로드 성공 (Cloudinary)
- [ ] 라이브 월 실시간 업데이트 확인
- [ ] 환경변수 백업 완료

**배포된 URL**: ___________________________

**관리자 계정**: ___________________________

**배포 날짜**: ___________________________

---

**다음 작업**: 사용자 유입을 위한 마케팅 및 피드백 수집!
