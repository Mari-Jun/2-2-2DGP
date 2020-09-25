2학년 2학기 2D게임 프로그래밍 기말 프로젝트 폴더
=============

## 게임의 소개
### 제목 : Bubble Bobble
> 국민 오락실 게임 Bubble bobble을 모작   
> 적들을 Bubble안에 가둬 물리치세요.     
> 1P만 가능하게 할 예정    
![버블바블](https://user-images.githubusercontent.com/34498116/94247286-ddfffc00-ff57-11ea-8378-a34f907a2580.png)

## GameState (Scene)

### 게임 프레임워크
![프레임워크 간단](https://user-images.githubusercontent.com/34498116/94248688-c7f33b00-ff59-11ea-8caa-182ec9455433.PNG)

### Loading Scene 
> 게임을 시작할 때 나오는 로딩 화면 (로고 화면이라고 봐도 무방함)   
> 로고만 띄워지고 자동으로 (일정 시간 후) Title Scene으로 넘어감   
> 별다른 이벤트는 없음   
    
 ### Title Scene
> 로딩이 끝난 후 나오게 되는 화면   
> Game Start, Help, Ranking, Quit 버튼등이 존재한다.    
> 키보드, 마우스로 각 버튼을 선택 가능      
>> Game Start Button -> Game Scene    
>> Help Button -> Help Scene    
>> Ranking Button -> Ranking Scene    
>> Quit Button -> Exit Game    
    
### Help Scene
> 게임 방법등의 게임을 하기 위해서 필요한 것들을 설명하는 화면   
> Next, Back 버튼 존재 (Next버튼은 Help페이지가 길어지게 되면 구현할 예정.)  
>> Back Button -> Title Scene
    
### Ranking Scene
> 플레이어의 점수 확인 가능   
> Back 버튼 -> Title Scene   

### Game Scene
> 게임 플레이 화면   
> 즉 실제로 공룡들이 움직이고 적을 처치하는 곳   
> 방향키(이동 및 점프), Ctrl(공격) 키보드 입력을 사용
> 게임 클리어 혹은 사망할 경우 Ranking Scene으로 이동

## 필요한 기술
> 마우스 입력, 키보드 입력   
> 충돌 처리, 델타 타임, 인공지능 (AI), 사운드   
> Sprite(애니메이션 시트) 처리, 파일 입출력    
> 중력가속도 (실제 Bubble Bobble 게임에서는 중력가속도가 없는 것으로 앎. <적용한 버전이 너무 이상하면 중력가속도는 삭제>)   

##### 다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술 
> 모든 강의 자료에서 이 게임을 만드는데에 있어서 필요한 부분은 다 설명되어있는것 같습니다.
