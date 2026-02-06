# UNIX
- 쉘: 명령어 해석기, 시스템과 사용자 간의 인터페이스
- `ls`: 디렉토리의 내용물 출력
- `cat`: 문자열 합성
- `chmod`: 권한 변경
- `fork`: 새 프로세스 생성

# OSI-7계층
|계층|이름|TCP-IP|전달단위|사용 프로토콜|
|7|응용계층|application|Data|http,telnet,ftp,smtp/ssh/snmp,dhcp,dns|
|6|표현계층|application|Data|mime,tls,ssl,jpeg,mpeg,smb,afp|
|5|세션계층|application|Data|ssh,tls,rpc|
|4|전송계층(transport)|transport|Header+Data=`Segment`|TCP,UDP,sctp,rtp|
|3|네트워크계층(network)|internet|Header+Segment=`Packet`|IP,ICMP,ARP,RARP|
|2|데이터링크(datalink)|network|Header+Packet=`Frame`|ehternet,atm,pop|
|1|물리(physical)|network|Frame|허브, 리피터|

### 네트워크 계층
종단간 신뢰성 담당
- TCP 계열: telnet, FTP, HTTP, POP, SMTP
- UDP 계열: DHCP, SNMP, DNS
#### 프로토콜
- IP - 주소
- ICMP - 전달여부 확인
- ARP - IP -> MAC
- RARP - MAC -> IP
### 데이터링크 계층

# 프로세스 상태(생태주기)
- `ready` -`dispatch`-> `execute` -`Block`-> `wait` -`wakeup`-> `ready`
- `execute` -`timeout`-> `ready`

# IPv4, IPv6
|구분|IPv4|IPv6|
|주소길이|32bit(4Byte)|128bit(16Byte)|
|표시방법|8bit씩 4부분|16bit씩 8부분|
|주소개수|약 43억|약 31조|
|주소할당|A,B,C,D,E 클래스 단위 비 순차적 할당|네트워크 규모 및 단말기 개수에 따라 순차할당|
|품질제어|보장X|보장O|
|헤더크기|고정|가변|
|QualityofService|BestEffort|등급별, 서비스별 패킷 구분|
|보안기능|IPSec 따로 설치|확장기능에서 기본제공|
|plug&play|X|O|
|모바일IP|X|O|
|웹캐스팅|X|O|
|전송방식|MultiCast,UniCast,BroadCast|MultiCast,UniCast,AnyCast|

# 결합도 & 응집도
모듈의 독립성, 프로그램의 재사용성과 직결
## 결합도
|결합도|내용|
|---|---|
|데이터(`data`)|자료값만 전달|
|스탬프(`stamp`)|배열,오브젝츠,스츠럭쳐 전달|
|제어(`control`)|다른 모듈의 제어 요소 전달|
|외부|외부로 선언한 변수를 다른 모듈에서 참조|
|공통(`common`)|전역변수 참조|
|내용(`content`)|다른 모듈 내부의 변수나 기능을 다른 모듈에서 사용|
아래로 갈 수록 결합도 높음 = 독립성 낮음
## 응집도
|응집도|내용|
|---|---|
|기능적|모듈 내부의 모든 기능이 단일한 목적을 위해 수행|
|순차적|`모듈 내에서` 한 활동으로부터 나온 `출력값을 다른 활동이 사용`|
|통신적|`동일한 입력과 출력`을 사용해 다른 기능 수행|
|절차적|모듈 안의 구성 요소들이 기능을 `순차적`으로 수행할 경우|
|시간적|특정 `시간`에 처리되어야 하는 활동을 한 모듈에서 처리|
|논리적|`유사한 성격`을 갖거나 특정 형태로 분류되는 처리요소를 한 모듈에서 관리|
|우연적|연관이없음|
아래로 갈수록 응집도 낮음 -> 독립성 낮음

# 교착상태
서로 다른 프로세스가 점유하고 있는 자원을 요구하며 서로의 작업이 끝나길 기다리며 영원히 안끝나는 상황
## 발생 원인
아래의 조건이 모두 참이어야 함
- 상호배제(mutual exclusion): 한번에 한개의 프로세스만이 공유자원 사용가능
- 점유와 대기(hold and wait): 프로세스가 자원을 가진 상태에서 다른 자원을 기다림
- 비선점(no preemption): 이미 할당된 자원을 강제적으로 빼앗을 수 없음
- 환형대기(circular wait): 프로세스의 자원 점유 및 점유된 자원의 요구 관계가 선형을 이루며 대기
## 해결방법
- 예방(Prevention): 교착상태 발생 원인 중 하나만 예방해도 교착되지 않음
- 회피(Avoidance): `은행가 알고리즘`, `Wait-Die`, `wound-wait`
- 발견(Detection): 시스템 상태를 `감시 알고리즘`을 통해 교착상태 검사
- 회복(Recovery): Deadlock이 없어질 때까지 `프로세스를 순차적으로 kill`

# 프로세스 스케줄링
- 선점형: 실행중인 프로세스를 Block하고 우선순위가 위인 프로세스를 먼저 Dispatch 가능
- 비선점형: 프로세스가 실행중이면 그 프로세스가 끝날 때까지 새로운 프로세스가 점유할 수 없음

- 기아현상: 프로세스가 우선순위가 밀려 리소스를 오랫동안 할당받지 못함
- 에이징: 기아현상을 방지하기 위해 일정시간동안 대기한 프로세스의 우선순위를 높여줌
- 대기시간: 작업 들어가기 전 대기하는 시간
- 반환시간: 대기부터 작업이 끝날 때까지의 시간
## 선점형
- Round Robin(RR)
- Shortest Remaining Time first(SRT)
- Multi Level Queue(MLQ)
- Multi Level Feedback Queue(MFQ)
#### Round Robin(RR)
프로세스마다 같은 크기의 CPU 시간을 할당, 프로세스가 할당된 시간 내에 처리를 못하면 준비 큐 리스트의 맨 뒤로 보내짐
#### Shortest Remaining Time first(SRT)
작업중이더라도 남은 작업시간이 더 짧은 작업이 쿠에 들어오면, 원래 하던 직업을 Block하고 짧은 프로세스를 선점시킴
#### Multi Level Queue(MLQ)
- 우선순위로 나누어진 여러 큐 중에 들어오는 작업이 어디로 갈지 정해서 수행
- 우선순위가 높은 큐의 작업이 먼저 수행
#### Multi Level Feedback Queue(MLFQ, MFQ)
- MLQ+RR
- 프로세스가 큐들 사이를 이동할 수 있음
- 한 프로세스가 너무 많은 시간을 소요하면 하위큐로 삽입
- 최하위에선 RR을 실행
## 비선점형
- First Come First Served(FCFS)
- Shortest Job First(SJF)
- Highest Response ratio Next(HRN)
- 우선순위
- 기한부
#### First Come First Served(FCFS)
- 비선점형
- 대기 큐에 먼저 온 프로세스가 먼저 CPU에 할당
#### Shortest Job First(SJF)
- 작업시간이 가장 짧은 걸 우선
- 비선점형이라 큐에 갑자기 더 짧은 게 나타났다고 Block해버리진 않음
#### Highest Response ratio Next(SRN)
- SJF의 기아현상 보완
- 우선순위 = (대기시간+실행시간)/(실행시간)
#### 기한부
정해진 시간 안에 완료하지 못하면 프로세스 제거/재실행

# 페이지 교체 알고리즘
메모리에 필요한 페이지가 없을 때(page-fault) 프레임을 비우고 로딩하기 위해 희생당할 프레임(victim frame)을 고르는 알고리즘
- FIFO(First In First Out)
- LRU(Least Recently Used)
- LFU(Least Frequently Used)
- OPT(optimal)
- NUR(Not Used Recently)
- SCR(Second Chance Replacement, 자주 사용되는 페이지의 교체 방지)
#### First In First Out(FIFO)
- 가장 먼저 메모리에 올라온 페이지를 가장 먼저 삭제
- Belady`s Anomaly: 프레임 수가 늘어도 page-fault는 해소되지 않고 오히려 늘어남
#### Least Recently Used(LRU)
- 가장 오랫동안 사용되지 않은 페이지 교체
- 큐로 구현해 사용된 큐는 위로 이동, 교체시 하단에서 삭제
#### Least Frequently Used(LFU)
- 참조횟수가 가장 적은 페이지 교체
- 교체 대상이 여러개면 그중 가장 오랫동안 사용하지 않은 것을 교체
- 가장 최근에 불러온 페이지가 교체될 수도 있음


# 언어
## 컴파일 언어
프로그램 전체를 처음부터 끝까지 해독해 목적코드로 만든 후 실행
- C
- C++
- COBOL
- Ada
- FORTRAN
- PASCAL
## 인터프리터 언어
프로그램 라인 단위로 한줄씩 해석해 진행
- javascript
- BASIC
- LISP
## 스크립트 언어
소스코드를 컴파일하지 않고 바로 실행(내장된 번역기 이용)
- javascript
- actionscript
- jsp
- perl
- php
- python
- ruby

# JAVA 접근 제한자
- public
- default
- protected
- private

# 서브넷
IPv4 네트워크를 가상으로 쪼갠 것
## IP주소 클래스
하나의 IP주소를 나누는 방법, 어디까지가 네트워크 식별 영역이고 호스트 식별 영역인지 표기
- A클래스: 첫 옥텟이 0~127(0xxx xxxx...), 첫 옥텟 만으로 네트워크 식별
- B클래스: 첫 옥텟 128~191(10xx xxxx...), 두 옥텟으로 네트워크 식별
- C클래스: 첫 옥텟 192~223(110x xxxx...), 세 옥텟으로 넽워크 식별
- D클래스
- E클래스
## 서브넷 마스크
- IP주소 영역을 더 자유롭게 쪼개는 기술
- `x.x.x.x/X`식의 IP주소에서 `/X`로 표기, `X`의 수만큼 서브넷 마스크에서 네트워크 영역으로 취급
### 클래스별 기본 서브넷 마스크
- A: 255.0.0.0(`/8`)
- B: 255.255.0.0(`/16`)
- C: 255.255.255.0(`/24`)
## 특수 IP 주소
- 첫번째 주소: 네트워크 주소(IP subnet-zero가 적용됐다면)
- 마지막 주소: 브로드캐스트 주소
#### IP subnet-zero
가장 첫번째 주소를 네트워크 주소로 지정함

# 전송속도
- `전송속도` = `변조속도`*`사용하는 비트 수`
- `2^k-PSK 변조`: `사용하는 비트 수`=`k`

# 소프트웨어 보안 취약점
## 메모리
- 버퍼 오버플로: `메모리 오류`
- 허상 포인터: `유효하지 못한 객체`를 가리킨 `포인터`
- NULL POINTER 역참조: `NULL`로 설정된 변수의 주소값 참조
## 입력확인 오류
- 포맷 스트링 버그: `상정되지 않은` 사용자 입력
- SQL 삽입: `SQL문`이 실행되도록 입력값 설정
- 코드 삽입: `스크립트 코드` 실행
- 웹 사이트간 스크립팅(`XSS`): 부정한 `HTML`, `javascript` 삽입
- 이메일 삽입
- 디렉토리 접근 공격
- HTTP 헤더 인젝션
- HTTP 응답 스플리팅
## 경쟁상태
- Time of check to time of use: `동기화 오류`
- 심볼릭 링크 경쟁: `심볼릭 링크`를 이용한 공격
## 권한 혼동 버그
- 웹에서 사이트간 요청 위조
- 클릭 재킹
- FTP 바운스 공격

# 배치 프로그램 필수 요소
|요소|설명|
|---|---|
|대용량 데이터|대용량의 데이터 처리|
|자동화|사용자의 개입 없이 동작|
|견고함|비정상적인 동작 중단 발생 X|
|안정성|어떤 문제가 생겼는지, 언제 발생했는지 추적|
|성능|주어진 시간 내에 처리, 동시에 동작하는 다른 애플리케이션 방해X|

# 메모리 관리 기법
기본적으로 이미 사용하는 영역에는 들어갈 수 없다.
- First Fit: 들어갈 수 있는 제일 첫번째 영역
- Worst Fit: 들어갈 수 있는 가장 큰 영역
- Best Fit: 들어갈 수 있는 가장 작은 영역
## 단편화
- 내부 단편화: 한 영역에 들어갔을 때 영역에 남는 공간
- 외부 단편화: 한 영역보다 프로그램이 클 때 할당되지 못한 부분