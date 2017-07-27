<<<<<<< HEAD
# 7/26 Reinforcement Learning (Q-Learning)

## [Example Code by royel](https://github.com/Royeqiu/ReinforcementLearningExample)

## [GitHub of mine](https://github.com/LonEdit120/reinforcement_learning/blob/master/q_learning/rl.py)

## Action sequence
- State (開始到結束的每個階段)
- Action (一個state到下一個state)
- Reinforcement learning -> 從所有Action和State中找出最佳解

## Requirements for using Reinforced Learning
- 要知道所有State和Action
- 要有明確的target

## 分數更新概念：

幫每個STATE到STATE的ACTION評分.找最高分.如果有更好就更新他
一直執行到分數變化不大
![](https://i.imgur.com/eUl8Rc3.png)
- discount factor : 用來解決環的發生可性
- learning rate : 決定學習速度（愈小愈準確.但費時更久）.類從波浪曲線圖找最低點
- jump probability : 為了防止有路線沒被走到.有不選當前最高分的可能性（不能太高）

![](https://i.imgur.com/Au6Pkj6.png)


=======
# reinforcement_learning
# reinforcement_learning
>>>>>>> fd16260853054e87c90f320588520a77397f5fcb
