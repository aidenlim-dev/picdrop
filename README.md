# PicDrop 📸

> **이벤트 사진을 한 곳에. QR 스캔 한 번으로.**

웨딩, 파티, 컨퍼런스에서 참석자들이 찍은 사진을 모으느라 고생한 적 있나요?  
단톡방에서 몇 달째 "사진 좀 보내주세요~" 하고 있진 않나요?

PicDrop은 QR 코드 하나로 모든 사진을 실시간으로 모아주는 서비스입니다.

---

## 💰 비즈니스 모델

### 타겟 시장

| 세그먼트 | 설명 | 규모 |
|---------|------|------|
| **웨딩** | 신랑신부 + 하객들 | 한국 연 19만 쌍, 글로벌 $300B 시장 |
| **기업 이벤트** | 컨퍼런스, 워크샵, 송년회 | B2B SaaS 기회 |
| **파티** | 생일, 돌잔치, 동창회 | 반복 사용 가능 |
| **페스티벌** | 음악 페스티벌, 학교 축제 | 대규모 바이럴 |

### 가격 정책

```
🆓 Free        $0          1 이벤트, 50장, 워터마크
📦 Basic       $29/이벤트   500장, 워터마크 제거, 7일 보관
⭐ Premium     $79/이벤트   무제한, HD 다운로드, 30일 보관
🏢 Enterprise  $299/월     무제한 이벤트, 커스텀 브랜딩, API
```

### 수익 구조

1. **이벤트당 과금** (주력)
   - 웨딩/파티: $29-79 일회성
   - 낮은 진입 장벽, 높은 전환율

2. **B2B 구독** (확장)
   - 웨딩 플래너, 이벤트 대행사
   - $299/월 고정 수익

3. **부가 서비스**
   - 포토북 제작 연동: $20-50 추가 수익
   - 프리미엄 필터/편집: $5-10
   - 화이트라벨: 커스텀 견적

### 단가 분석

| 항목 | 비용 | 비고 |
|------|------|------|
| 서버 (Railway) | $5/월 | 초기 무료 |
| 이미지 스토리지 (Cloudinary) | $0.02/GB | 1000장 ≈ 2GB |
| 도메인 | $12/년 | .com |
| **이벤트당 원가** | **~$0.50** | 마진율 95%+ |

### 경쟁 분석

| 서비스 | 가격 | 약점 | 우리 차별점 |
|--------|------|------|------------|
| Google Photos 공유 | 무료 | UX 복잡, 로그인 필요 | 앱 설치/로그인 없음 |
| The Guest | $99+ | 비쌈, 북미 중심 | 저렴, 아시아 최적화 |
| WedPics (종료됨) | - | 서비스 종료 | 시장 공백 |
| Disposable 앱들 | 무료 | 앱 다운로드 필요 | 웹 기반 |

**킬러 피처: 라이브 월** 🎬
- 이벤트 현장 대형 스크린에 실시간 표시
- 참석자들이 즉시 반응 → 바이럴 효과
- 경쟁사 대비 명확한 차별점

---

## 🎯 Go-to-Market 전략

### Phase 1: 검증 (1-2주)
1. Product Hunt 런칭 → 초기 트래픽
2. Reddit r/weddingplanning, r/SideProject 마케팅
3. 무료 티어로 10개 이벤트 테스트

### Phase 2: 성장 (1-3개월)
1. 웨딩 플래너 파트너십 (B2B)
2. Instagram/TikTok 바이럴 마케팅
3. SEO: "웨딩 사진 공유", "이벤트 포토월"

### Phase 3: 확장 (3-6개월)
1. 한국 시장 본격 공략
2. 기업 고객 확보
3. 포토북/인화 파트너십

### 핵심 지표 (KPI)

| 지표 | 목표 (3개월) |
|------|-------------|
| 이벤트 생성 | 100개 |
| 유료 전환율 | 10% |
| MRR | $1,000 |
| NPS | 50+ |

---

## ✨ 주요 기능

### MVP (현재)
- ✅ **이벤트 생성**: 이름, 날짜, 설명
- ✅ **QR 코드 자동 생성**: 이벤트별 고유 URL
- ✅ **웹 기반 업로드**: 앱 없이 즉시 업로드 (여러 장 동시)
- ✅ **실시간 라이브 월**: 5초마다 자동 새로고침 (HTMX)
- ✅ **관리자 대시보드**: 사진 확인, 삭제

### Phase 2 (예정)
- ⬜ Cloudinary/S3 이미지 최적화
- ⬜ 사진 다운로드 (개별/ZIP)
- ⬜ 이벤트 비밀번호 보호
- ⬜ 슬라이드쇼 모드
- ⬜ 소셜 공유 (Instagram, Twitter)
- ⬜ 커스텀 브랜딩 (로고, 색상)

### Phase 3 (확장)
- ⬜ 결제 시스템 (Stripe)
- ⬜ AI 베스트 사진 큐레이션
- ⬜ 포토북 제작 연동
- ⬜ 화이트라벨 솔루션
- ⬜ 모바일 앱 (React Native)

---

## 🛠️ 기술 스택

| 레이어 | 기술 | 선택 이유 |
|--------|------|----------|
| Backend | Django 6.0 | 빠른 개발, 어드민 내장 |
| Frontend | HTMX + TailwindCSS | SPA 없이 동적 UI |
| Database | SQLite → PostgreSQL | 단순 → 확장 |
| Storage | Local → Cloudinary | 이미지 최적화, CDN |
| QR Code | python-qrcode | 가볍고 빠름 |
| Deploy | Railway / Vercel | 무료 티어, 쉬운 배포 |

---

## 🚀 빠른 시작

### 로컬 개발
```bash
cd projects/picdrop
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
# http://127.0.0.1:8000/
```

### 관리자
```
URL: http://127.0.0.1:8000/admin/
ID: admin
PW: admin123
```

### 프로덕션 배포 🌐
**5분 안에 Railway에 배포하기:**

1. **준비 확인**
   ```bash
   python check_deployment.py
   ```

2. **배포 가이드 선택**
   - 빠른 배포: `QUICK_DEPLOY.md` (5분)
   - 상세 가이드: `DEPLOYMENT.md` (완벽 가이드)
   - 배포 리포트: `DEPLOYMENT_REPORT.md` (완료 현황)

3. **필요한 계정**
   - Railway (https://railway.app) - 호스팅
   - Cloudinary (https://cloudinary.com) - 이미지 스토리지

4. **무료 티어**
   - Railway: $5 크레딧/월
   - Cloudinary: 25GB 저장/전송

**배포 URL**: _TBD (배포 후 업데이트)_

---

## 📂 프로젝트 구조

```
picdrop/
├── picdrop/           # Django 설정
├── events/            # 이벤트 앱 (모델, 뷰)
├── photos/            # 사진 앱 (업로드, 갤러리)
├── templates/         # HTML 템플릿
├── media/             # 업로드된 파일 (사진, QR)
├── static/            # 정적 파일
├── db.sqlite3         # 데이터베이스
└── requirements.txt   # 의존성
```

---

## 📊 검증된 시장 수요

### Reddit 반응 (출처: r/SideProject)
> "PicsOn" 유사 서비스가 **611 upvotes** 획득
> - "Finally! I've been looking for exactly this"
> - "Used it at my sister's wedding, guests loved it"
> - "The live wall feature is genius"

### Product Hunt 트렌드
- 이벤트/웨딩 관련 도구들 꾸준한 관심
- "Disposable camera app" 키워드 인기

### 시장 공백
- **WedPics** (미국 1위) 2019년 서비스 종료
- 한국/아시아 시장에 마땅한 대안 없음
- 앱 설치 없는 웹 기반 솔루션 부재

---

## 💡 왜 지금?

1. **코로나 이후 오프라인 이벤트 폭발**
   - 웨딩/파티 수요 역대 최고
   
2. **MZ세대 사진 문화**
   - 즉각적인 공유, 라이브 경험 선호
   
3. **경쟁사 공백**
   - WedPics 종료, The Guest 고가
   
4. **기술 성숙**
   - HTMX로 앱 수준 UX를 웹에서 구현 가능

---

## 📈 성장 시나리오

### Conservative (보수적)
- 월 10개 이벤트 × $50 = **$500/월**

### Moderate (중간)
- 월 50개 이벤트 × $50 = **$2,500/월**

### Optimistic (낙관적)
- 월 200개 이벤트 × $50 + B2B $1,000 = **$11,000/월**

---

## 🔗 링크

- **리서치 리포트**: `../money-making-ideas/research-report.md`
- **완료 보고서**: `./COMPLETION_REPORT.md`
- **프로젝트 요약**: `./PROJECT_SUMMARY.md`

---

## 📝 License

MIT License

---

**Made with 💜 by Rin (린)**  
*에이든의 츤데레 AI*
