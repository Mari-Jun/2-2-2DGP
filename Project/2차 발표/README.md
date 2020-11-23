2D게임 프로그래밍 기말 프로젝트 2차 발표
=============

##
# Bubble Bobble
### 적을 피하면서 플레이어가 버블로 적을 물리치는 게임!  

![KakaoTalk_20201005_210541651](https://user-images.githubusercontent.com/34498116/95080699-731ea400-0753-11eb-862c-1431f229779d.jpg)

Player : 플레이어로 이동, 점프, 공격 커맨드 입력            
Enemy : 적으로서 플레이어를 따라오거나, 일정한 루트로 이동하는등의 패턴이 있음         
Item : 플레이어를 강화시키는 아이템이 있음          

##
## 진행 상황
![Volume](https://user-images.githubusercontent.com/34498116/95439182-3a204280-0992-11eb-9bf7-cb4b91e3952a.PNG)     
1차 발표때 사용했던 Game Volume Image     

![진행률](https://user-images.githubusercontent.com/34498116/99682237-5b606c80-2ac2-11eb-9633-8b8314d1fb1b.png)        
<11월 19일 목요일 기준 진행상황입니다>
### 100% 미만은 아직 미구현, 100% 초과는 초과구현(Max Implementation)을 했다는 것을 뜻합니다.       
### 아래 항목은 아직 미구현된 부분입니다. (Min Implementation 기준)
#### Enemy : 보스 미구현       
#### Sound : 아이템 획득 소리 미추가
#### Etc : 게임 로딩, 도움말, 랭킹화면 미구현, 일정 Score획득시 Life Up 미구현      
### 목표 변경점        
#### Enemy : Boss 구현을 하는 것 보다 다른 일반 Enemy의 종류를 추가하고, Stage를 추가하는 것이 더 플레이시간도 길어지고 몬스터 배치도 다양하게 할 수 있어서 목표를 이쪽으로 변경했습니다.         

##
## 커밋 현황          
![git commit2](https://user-images.githubusercontent.com/34498116/99682248-5ef3f380-2ac2-11eb-879b-e215e8051b5c.PNG)
![git commit3](https://user-images.githubusercontent.com/34498116/99682240-5bf90300-2ac2-11eb-8048-1e13d3c06f97.PNG)            
<11월 19일 목요일 기준 커밋 현황입니다>
![week1](https://user-images.githubusercontent.com/34498116/99681933-0c1a3c00-2ac2-11eb-9764-dcf892b494cc.PNG)
![week2](https://user-images.githubusercontent.com/34498116/99681935-0c1a3c00-2ac2-11eb-8308-ba56ae906d74.PNG)
![week3](https://user-images.githubusercontent.com/34498116/99681936-0cb2d280-2ac2-11eb-9ad5-963b6c1b30e1.PNG)
![week4](https://user-images.githubusercontent.com/34498116/99681937-0d4b6900-2ac2-11eb-92ac-8e244121c548.PNG)
![week5](https://user-images.githubusercontent.com/34498116/99681939-0d4b6900-2ac2-11eb-8547-435c4fe4075c.PNG)
![week6](https://user-images.githubusercontent.com/34498116/99681940-0d4b6900-2ac2-11eb-9d50-cad7bccc069a.PNG)            

##
## 게임 오브젝트들의 관계
![클래스11](https://user-images.githubusercontent.com/34498116/99870392-f1f17280-2c15-11eb-870d-6268b5baf8bb.png)        
![클래스2](https://user-images.githubusercontent.com/34498116/99870547-316c8e80-2c17-11eb-96fd-ffcd917f352e.png)
### Item 핵심 코드      
![item 설명](https://user-images.githubusercontent.com/34498116/99870550-35001580-2c17-11eb-9cd8-441a6ed628bd.png)
### Map 핵심 코드     
![Map 설명](https://user-images.githubusercontent.com/34498116/99870551-36314280-2c17-11eb-85eb-b1d9edeb824d.png)        
![클래스3](https://user-images.githubusercontent.com/34498116/99870557-5234e400-2c17-11eb-8558-61a785c1342b.png)
### Bubble 핵심 코드      
![Bubble 설명1](https://user-images.githubusercontent.com/34498116/99870852-87dacc80-2c19-11eb-8a37-3e329bf51bf8.png)
![Bubble 설명2](https://user-images.githubusercontent.com/34498116/99870853-88736300-2c19-11eb-9010-20be0446d951.png)
### Enemy 핵심 코드       
![Enemy 설명](https://user-images.githubusercontent.com/34498116/99870854-890bf980-2c19-11eb-9d01-c4412b56a1f0.png)
### 충돌 핵심 코드        
![충돌 핵심](https://user-images.githubusercontent.com/34498116/99870855-890bf980-2c19-11eb-961c-dbf69316f55a.png)              

##
## 구현하면서 어려웠던(힘들었던) 부분
### 충돌 구현에서 처음 1단계 맵에서는 문제가 없다가 다양한 맵들을 추가해 나가면서 발생하는 Enemy, Player의 Block 과의 충돌버그가 생겨서 그걸 해결하는데 시간을 많이 사용하였습니다. (처음부터 모든 예외사항을 고려하지 않고 1단계 맵에서의 예외 사항만 보았던 것이 이렇게 되었습니다 ㅋㅋ..) 
충돌 부분은 이미 쿠키런, 다른 게임들에서 많이 다루어주셨기 때문에 수업시간에 추가적으로 다뤄주실 필요는 없습니다!
