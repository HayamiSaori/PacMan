**人工智能（COMP3005）课程实验，框架copy的伯克利CS188代码，部分实现为面向CSDN编程**

## Q1.深度优先搜索

见`search.py`文件`breadthFirstSearch(problem)`函数实现
运行命令：

```python
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
## Q2.广度优先搜索
见`search.py`文件`breadthFirstSearch(problem)`函数实现
运行命令：
```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
## Q3.代价一致搜索
见`search.py`文件`uniformCostSearch(problem)`函数实现
运行命令：
```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
## Q4.A\*算法
见`search.py`文件`aStarSearch(problem)`函数实现
运行命令：

```python
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
## Q5.角落问题
见`searchAgents.py`中`CornersProblem`类的
>`__init__(self, startingGameState)`
>`getStartState(self)`
>`isGoalState(self, state)`
>`getSuccessors(self, state)`

方法的实现
运行命令：
```python
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
## Q6.带启发值的角落问题
见`searchAgents.py`中`CornersProblem`类的`cornersHeuristic(state, problem)`函数的实现
运行命令：
```python
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
## Q7.最短路径我全都要
见`searchAgents.py`中`FoodSearchProblem`类的`foodHeuristic(state, problem)`方法的实现
运行命令：
```python
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
## Q8.贪心算法我全都要
见`searchAgents.py`中`ClosestDotSearchAgent`类的`findPathToClosestDot(self, gameState)`方法、
`AnyFoodSearchProblem`类的`isGoalState(self, state)`方法的实现
运行命令：

```python
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```