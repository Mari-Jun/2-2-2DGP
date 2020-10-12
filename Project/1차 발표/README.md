2D게임 프로그래밍 기말 프로젝트 1차 발표
=============

# Bubble Bobble
![버블바블](https://user-images.githubusercontent.com/34498116/94247286-ddfffc00-ff57-11ea-8378-a34f907a2580.png)

## Game Concept

적을 피하면서 플레이어가 버블로 적을 물리치는 게임!  
최종보스를 잡아 게임이 클리어!   
적을 빨리 물리치고, 아이템을 먹어가며 최종 스코어를 많이 쌓아올리세요!   
플레이어 강화 아이템을 통해 플레이어를 더욱 강화시키세요!! 물론 죽으면 사라집니다~

![KakaoTalk_20201005_210541651](https://user-images.githubusercontent.com/34498116/95080699-731ea400-0753-11eb-862c-1431f229779d.jpg)

Player : 플레이어로 이동, 점프, 공격 커맨드 입력
> 점프는 중력가속도를 적용, 일정 시간 이상 점프가 지속되면 등속운동     
> 공격     
>> 버블은 등속운동(x축)       
>> 일정 거리를 이동하게 되면 위로 이동      
>> 제일 위로 올라가서는 일정 크기로 반시계방향 이동    

Life : 플레이어의 목숨으로 목숨이 0이 되면 사망         

Enemy : 적으로서 플레이어를 따라오거나, 일정한 루트로 이동하는등의 패턴이 있음  
> 공격을 맞게된 Enemy는 버블 상태로 변함    
> 그 상태에서 플레이어가 버블을 터트리게 되면 적은 사망, 점수 획득    
> 적이 있는 버블을 일정시간 이상 터트리지 않으면 적은 탈출    

Item : 플레이어를 강화시키는 아이템이 있음     
> 플레이어 강화 아이템     
>> 신발 : 플레이어 이동속도 증가        
>> 빨간 포션 : 플레이어 공격속도 증가       
>> 노란 포션 : 버블의 이동속도 증가     
>> 파란 포션 : 버블의 이동거리(사정거리) 증가       

Stage : 게임    

## Game Flow
![111](https://user-images.githubusercontent.com/34498116/95089343-01e4ee00-075f-11eb-899d-701e8725da22.jpg)
### 적을 버블로 가둔다.     

![222](https://user-images.githubusercontent.com/34498116/95089346-027d8480-075f-11eb-962e-3c7cb9974cf3.jpg)
### 적이 있는 버블을 터트려서 적을 죽이고, 점수를 획득한다.       

![333](https://user-images.githubusercontent.com/34498116/95089350-027d8480-075f-11eb-92f9-71739b840a6a.jpg)
### 아이템을 먹어 점수를 획득하는 상황.     

![444](https://user-images.githubusercontent.com/34498116/95089332-ff829400-075e-11eb-9eb1-b2d2f3d82d2c.jpg)
### 적을 모두 처치하여 다음 스테이지로 넘어감.      

![555](https://user-images.githubusercontent.com/34498116/95089340-014c5780-075f-11eb-86f1-32b907c84e91.jpg)
### 목숨이 모두 사라져서 사망하게 됨     


## Game Volume
![Volume](https://user-images.githubusercontent.com/34498116/95439182-3a204280-0992-11eb-9bf7-cb4b91e3952a.PNG)

## Develope Schedule
![Schedule](https://user-images.githubusercontent.com/34498116/95714890-dc4a6e00-0ca3-11eb-857a-337fcc4515f6.PNG)
