import numpy as np
import pandas as pd

# 랜덤 시드 고정
np.random.seed(42)

# 기간 및 지역 설정
years = np.arange(2010, 2024)
regions = ['서울', '부산', '대구', '인천', '광주', '대전']

# 데이터 저장을 위한 리스트 초기화
data = []

# 가상 데이터 생성
for year in years:
    for region in regions:
        # 경제적 지표
        unemployment_rate = np.clip(np.random.normal(5, 1.5), 2, 10)  # 실업률 (%)
        household_income = np.clip(np.random.normal(40000, 5000), 20000, 80000)  # 가계 소득 (달러)
        poverty_rate = np.clip(np.random.normal(15, 3), 5, 30)  # 빈곤율 (%)
        gini_index = np.clip(np.random.normal(0.3, 0.05), 0.2, 0.5)  # 지니계수

        # 사회적 지표
        divorce_rate = np.clip(np.random.normal(3, 0.5), 1, 5)  # 이혼율 (%)
        domestic_violence_reports = int(np.clip(np.random.normal(1500, 300), 500, 3000))  # 가정 폭력 신고 건수
        education_level = np.clip(np.random.normal(80, 5), 60, 100)  # 고졸 이상 비율 (%)
        population_density = np.clip(np.random.normal(10000, 3000), 1000, 30000)  # 인구 밀도 (명/km²)

        # 건강 관련 지표
        mental_health_issue_rate = np.clip(np.random.normal(10, 2), 5, 20)  # 정신 건강 문제 발생률 (%)
        substance_abuse_rate = np.clip(np.random.normal(5, 1), 2, 10)  # 알코올 및 약물 남용률 (%)
        psychiatric_hospitalization_rate = np.clip(np.random.normal(2, 0.5), 0.5, 5)  # 정신과 입원율 (%)
        suicide_attempt_hospital_visits = int(np.clip(np.random.normal(200, 50), 50, 500))  # 자살 시도 병원 방문 건수

        # 문화적/지역적 지표
        religious_participation_rate = np.clip(np.random.normal(20, 5), 5, 40)  # 종교 참여율 (%)
        social_support_index = np.clip(np.random.normal(70, 10), 40, 100)  # 사회적 지원 수준 (%)
        social_stigma_index = np.clip(np.random.normal(50, 10), 20, 80)  # 자살에 대한 사회적 낙인 정도 (%)

        # 정부 정책 및 법률 지표
        mental_health_budget = np.clip(np.random.normal(1000, 200), 500, 2000)  # 정신 건강 지원 예산 (백만 달러)
        suicide_prevention_program = np.random.choice([True, False], p=[0.7, 0.3])  # 자살 예방 프로그램 존재 여부
        mental_health_service_accessibility = np.clip(np.random.normal(80, 10), 50, 100)  # 정신 건강 서비스 접근성 (%)

        # 자살률 생성 (실업률, 빈곤율, 지니계수, 정신 건강 문제 발생률과 상관관계 반영)
        suicide_rate = 10 + 0.4 * unemployment_rate + 0.3 * poverty_rate + 5 * gini_index + 0.2 * mental_health_issue_rate

        # 데이터 추가
        data.append([
            year, region, unemployment_rate, household_income, poverty_rate, gini_index,
            divorce_rate, domestic_violence_reports, education_level, population_density,
            mental_health_issue_rate, substance_abuse_rate, psychiatric_hospitalization_rate,
            suicide_attempt_hospital_visits, religious_participation_rate, social_support_index,
            social_stigma_index, mental_health_budget, suicide_prevention_program,
            mental_health_service_accessibility, suicide_rate
        ])

# 컬럼 정의
columns = [
    '연도', '지역', '실업률', '가계 소득', '빈곤율', '지니계수', '이혼율', '가정 폭력 신고 건수',
    '교육 수준', '인구 밀도', '정신 건강 문제 발생률', '알코올 및 약물 남용률', '정신과 입원율',
    '자살 시도 병원 방문 건수', '종교 참여율', '사회적 지원 수준', '사회적 낙인 정도',
    '정신 건강 지원 예산', '자살 예방 프로그램 존재 여부', '정신 건강 서비스 접근성', '자살률'
]

# 데이터프레임 생성
df = pd.DataFrame(data, columns=columns)

# CSV 파일로 저장
csv_file_path = "synthetic_data.csv"
df.to_csv(csv_file_path, index=False)

print(f"CSV 파일이 생성되었습니다: {csv_file_path}")

