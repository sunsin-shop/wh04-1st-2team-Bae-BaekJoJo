# 스마트 어시스턴트 (Smart Assistant)

**Team Name**: 배백조조  
**Version**: 0.5.0v  
**Web Link**:  [Smart Assistant](https://bae-baekjojo.streamlit.app/)
 
**Requirements and Scenarios**: [요구사항&시나리오](https://github.com/sunsin-shop/wh04-1st-2team-Bae-BaekJoJo/wiki/%EA%B3%A0%EA%B0%9D-%EC%A0%95%EC%9D%98---%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD-%EB%B6%84%EC%84%9D-&-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4)

**research and benchmarking**: [시장조사&벤치마킹](https://github.com/sunsin-shop/wh04-1st-2team-Bae-BaekJoJo/wiki/%EC%8B%9C%EC%9E%A5-%EC%A1%B0%EC%82%AC-%EB%B0%8F-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%82%B9)

**review**: [회고록](https://github.com/sunsin-shop/wh04-1st-2team-Bae-BaekJoJo/wiki/%ED%9A%8C%EA%B3%A0%EB%A1%9D)

---

## 📜 프로젝트 소개

🎛️ **스마트 어시스턴트**는 사용자의 업무를 더 스마트하고 효율적으로 처리할 수 있는 플랫폼입니다.  

일정 관리, 경로 추천, 가전제품 추천, 음악 추천 등 다양한 기능을 제공하여 업무 속 편리함을 선사합니다.  

이 앱을 통해 근무 일정 관리, 최적의 경로를 안내받으며, 영업을 위한 가전제품 추천 시스템, 이동과 업무 중 리프레시를 위한 음악을 추천받는 등 스마트한 경험을 즐기세요!

## 주요 소비층
✅ 출장과 미팅이 많아 일정 관리가 필수인 직장인

✅ 고객에게 맞춤형 가전제품을 추천하고, 효과적으로 영업 성과를 내야 하는 세일즈 맨

✅ 업무 중 이동 시간이 많아 최적 경로 탐색이 중요한 근무자

## 🎯기대 효과

**시간 절약:** 일정 & 경로 최적화로 출장 업무 효율 증가

**영업 성과 향상:** 고객 맞춤 가전제품 추천으로 효과적인 영업 가능

**피로 감소:** 이동 중 음악 추천 기능으로 스트레스 해소 및 집중력 유지

→ 💡 "효율적인 일정 관리 + 스마트 영업 + 이동 중 리프레시"를 한 번에 해결하는 필수 도구!


## 📚페이지 구성

**🏠메인페이지**
- 각 기능으로 이동할 수 있는 **버튼 UI** 제공.
  
**🔍고객 정보 확인 가전 제품 추천 페이지**
- 고객 이름을 입력하면 보유한 가전제품과 **추천 제품을 제공**해 줍니다.
  
**🗓️일정 계획 페이지** 
- 사용자가 **일정을 효율적으로 관리**할 수 있도록 도와줍니다.  
📆 **캘린더 기반 일정 관리 기능** 제공

**🛣️출장 경로 추천 페이지**
- 날짜, 시간, 출발지와 목적지를 입력하면 **경로 추천**을 제공합니다.  

**🎧노래 추천&플레이리스트 자동 생성 페이지**
- 키워드를 입력하면 **분위기에 맞는 음악을 추천/ PLAYLIST** 를 생성해 줍니다. 

---

## 🛠️ 개발 환경

### 1. 프로젝트 설정
```bash
$ pdm init  # 프로젝트 초기화
$ source .venv/bin/activate  # 가상 환경 활성화
$ pdm install  # 필요한 패키지 설치
```
### 2. 로컬 실행
```bash
$ source .venv/bin/activate  # 가상 환경 활성화
$ streamlit run Main.py  # Streamlit 애플리케이션 실행
```
