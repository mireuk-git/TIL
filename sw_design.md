# 소프트웨어 개발 방법론
## 폭포수 기법
정형분석
계획에 중점
## Agile 기법
#### XP(eXtreme Programming)
XP 5가치
- 용기
- 의사소통
- 피드백
- 단순성
- 존중

# 객체지향
상향식 소프트웨어 개발
## 용어
- 일반화 - 상속(Inheritance)
- 추상화(Abstraction) - 구현
- 집단화 - `부분-전체`, `부분`
- 캡슐화(Encapsulation) - 정보 은닉(Information Hiding)
- 다형성(Polymorphism) - overload, override(`상속`)

## 객체지향 분석 방법론
- Rumbaugh: `객체모델링`->`동적모델링`->`기능모델링`
- Coad / Yourdon: `E-R 다이어그램`
- Booch: `미시적`,`거시적`
- Jacobson: `usecase`
- Wirfs-Brocks:`분석과 설계간 구분 없음`, 고객명세서

## 객체지향 설계 원칙(Solid)
- 단일 책임 원칙(SRP,Single Responsibility Principle): 클래스당 1책임
- 개방 폐쇄 원칙(OCP,Open-Close Principle): 수정에 폐쇄적 & 확장에 개방적, 코드 수정 없이 기능 확장
- 리스코프 치환 법칙(LSP, Liskov Substitution Principle): 하위 클래스를 상위 클래스로 대체할 수 있어야 함
- 인터페이스 분리 법칙(ISP,Interface Segregation Principle): 클라이언트 기준으로 인터페이스 분리
- 의존성 역전의 원칙(DIP, Dependency Inversion Principle): 자주 바뀌는 클래스에 의존X

# 요구사항 검토 방법
|검토 방법|내용|
|---|---|
|워크스루|회의 전 미리 요구사항 명세서 배포, 사전 검토 후 회의, 일정한 절차 존재|
|동료검토|비공식적, 동료 개발자와 검토 후 진행|
|인스펙션|작성자 외 전문 검초 그룹이 결함, 표준위배, 문제점 파악|
|CASE|자동화된 요구 사항 관리 도구 이용|

### CASE(Computer Aided Software Engineering)
#### 기능
- 그래픽 지원
- 소프트웨어 생명주기 전 단계 연결
- 다양한 소프트웨어 개발 모형 지원

# 성능 특성 분석
- 응답시간(Response Time): 요청 전달 후 응답까지의 시간
- 경과시간: 작업 요구부터 처리 완료까지의 시간
- 가용성(Availability): 사용하고 싶을 때 언제든 사용할 수 있는지
- 사용율(Utilization): 자원 사용률

# UI 설계 원칙
- 직관성: 누구나 쉽게 이해하고 사용할 수 있어야 함
- 유효성: 사용자의 목적을 정확하게 달성해야 함
- 학습성: 누구나 쉽게 배우고 사용 가능
- 유연성: 사용자 요구사항 최대한 수용, 오류 최소화

# 공통 모듈에 대한 명세 기법
- 상호작용성: 여러 모듈의 협력
- 명확성: 일관되게 이해, 한가지로만 해석
- 독립성: 모듈의 재사용, 결합도를 낮추고 응집도 올리기



# DBMS
#### 분석시 고려사항
- 가용성: 언제든지 쓸 수 있는지
- 성능
- 상호 호환성: 다른 기기와 호환되는지

# 데이터 흐름도(DFD)
|요소|표현법|뜻|
|---|---|---|
|단말(`Terminator`)|사각형|정보 제공자/사용자|
|프로세스(`Process`)|원|정보 처리|
|자료 흐름(`Data Flow`)|화살표|데이터가 어떤 프로세스에서 어떤 프로세스로 가는지|
|자료저장소(`Data Store`)|`=`|데이터 저장소, DB|

# DD(Data Dictionary)
|기호|의미|
|`=`|정의(is composed of)|
|`+`|연결(and)|
|`{}`|반복(iteration of)|
|`[ | ]`|선택(choose only one of)|
|`()`|생략(optional)|
|`**`|주석(comment)|


# UML
상향식 소프트웨어 개발
## UML 모델 구성 요소
#### 사물(things)
관계가 형성될 수 있는 대상들
- 구조(structural) 사물: 개념적, 물리적 요소
  - class
  - use case
  - component
  - node
- 행동(behavioral) 사물: 요소들의 행위
  - 상호작용
  - 상태 머신
- 그룹(grouping) 사물: 요소들을 그룹으로 묶어 표현
  - package
- 주해(annotion) 사물: 부가적인 설명/제약조건
#### 관계(relationship)
- 연관/의존 관계(대시선 화살표)
- 집합 관계(색칠 안된 마름모, 포함하는 쪽을 마름모로 표시)
- 포함 관계(색칠된 마름모)
- 일반화/추상/구체화 관계(색칠안된 삼각형)
- 상속(색칠된 삼각형)
- 의존 관계(점선)
- 실체화 관계
#### diagram
- structural diagram
  - class diagram
  - object(객체) diagram
  - component diagram
  - deployment(배치/배포) diagram
  - composite structure(컴포지트 구조) diagram
  - package diagram
- behavioral diagram
  - usecase diagram
  - sequence diagram
  - communication diagram
  - state(상태) diagram
  - activity(활동) diagram
  - interaction overview diagram
  - timing diagram

# GoF
#### 생성 패턴(5)
- abstract factory
- builder
- factory method
- prototype
- singleton
#### 구조 패턴(7)
- adapter
- bridge
- composite
- decorator
- facade
- flyweight
- proxy
#### 행위 패턴(10)
- chain of responsibility
- command
- interpreter
- mediator
- memento
- observer
- strategy
- state
- template method
- visitor

# HIPO(Hierarchy Input Process Output)
하향식 소프트웨어 개발을 위한 문서화 도구
- 가시적 도표: 시스템 전체 기능, 흐름
- 총체적 도표: 기능, `입력`,처리,`출력`에 대한 전반적 정보
- 세부적 도표: 기능을 구성하는 상세한 기본 요소


# 미들웨어
- 원격 프로시저 호출(RPC,Remote Procedure Call): 클라이언트가 원격에서 동작하는 프로시저 호출
- 메시지 지향 미들웨어(MOM,Message Oriented Middleware): 메시지를 저장하면서 다른 업무를 지속할 수 있게 함
- ORB(Object Request Broker)
- TP monitor
- DB 접속 미들웨어
- WAS(Web Application Server): 웹 어플리케이션 서버
- ESB(Enterprise Service Bus): 엔터프라이즈 서비스 버스

# 일련번호
|순차 코드|일정한 일련번호, 순서대로 부여|
|완전 순차 코드|일정 간격으로 비어있는 번호 부여|
|구분 순차 코드|몇개의 블록으로 나누어 각 블록에 의미 부여|
|연상 코드|코드에 제품의 특징이 들어있음|
|블록 코드|공통성 있는 것 끼리 블록으로 구분|
|표의 숫자 코드|표의 데이터를 기반으로 만든 코드|
|그룹 분류식 코드|대상을 기준에 따라 대/중/소분류로 구분|