# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
        result_list = []                    #结果列表
    close_set = set()                   #保存所有已经探索过的位置的集合
    stack = util.Stack()                #保存当前探索路径的栈，节点为三元组successor
    cur_state = problem.getStartState() 
    cur_node = (cur_state,'Start',0)
    close_set.add(cur_state)
    stack.push(cur_node)

    # while(not stack.isEmpty()):
    while(True):
        cur_node = stack.pop()          #获取栈顶节点
        cur_state = cur_node[0]         #栈顶节点的位置
        if(problem.isGoalState(cur_state)):     #栈顶节点是终点，则将栈全部弹出后倒转，所得列表即为答案
            # print("Search is done.")
            result_list.append(cur_node[1])
            while(not stack.isEmpty()):
                i = stack.pop()
                result_list.append(i[1])
            result_list.pop()
            result_list.reverse()
            # print("result list:",result_list)
            break
        else:                                   #否则，获取栈顶节点的后继节点，并遍历
            cur_successors = problem.getSuccessors(cur_state)
            for i in cur_successors:            
                if i[0] in close_set:           #若遍历到的后继节点已经探索过，则跳过
                    # print("node:",i,"has been explored.")
                    continue    
                else:                           #若遍历到的后继节点未探索，则将其压入栈中，开始下一轮循环
                    # print("node:",i,"is added to the stack.")
                    close_set.add(i[0])
                    stack.push(cur_node)
                    stack.push(i)
                    break
    # print("result list:",result_list)
    # print("cost:",problem.getCostOfActions(result_list))
    return result_list
    # cur_state = problem.getStartState()
    # close_set = set()                   #保存所有已经探索过的位置的集合
    # stack = util.Stack()                #栈
    # result_list = []                    #结果列表
    # stack.push((cur_state, []))
    # while(not problem.isGoalState(cur_state)):  #在找到终点前一直搜索
    #     cur_node = stack.pop()
    #     close_set.add(cur_node[0])
    #     successor = problem.getSuccessors(cur_node[0])
    #     for i in successor:
    #         if not i[0] in close_set:   #判断i是否已经探索过
    #             stack.push((i[0], cur_node[1] + [i[1]]))
    #         cur_state = i[0]
    #     result_list = cur_node[1] + [i[1]]
    # return result_list


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions

    prenode_dict = {}               #父节点字典，prenode_dict[state]表示state的父节点信息
    result_list = []                #结果列表
    close_set = set()               #保存所有已经探索过的位置的集合
    queue = util.Queue()            #队列

    cur_state = problem.getStartState()
    cur_node = (cur_state,'Start',0)
    close_set.add(cur_state)
    queue.push(cur_node)
    prenode_dict[cur_node] = cur_node

    while(True):
        cur_node = queue.pop()
        cur_state = cur_node[0]
        if(problem.isGoalState(cur_state)): #出队节点是终点
            # print("Search Done")
            while(cur_node[0] != problem.getStartState()): 
                result_list.append(cur_node[1])
                cur_node = prenode_dict[cur_node]
                # print(pre_node,"is the prenode of ",cur_node)
                # cur_node = pre_node
            result_list.reverse()
            break
        else:
            cur_successors = problem.getSuccessors(cur_state)
            for i in cur_successors:        #将当前节点的后继节点加入队列中
                if i[0] in close_set:
                    # print("node:",i,"has been explored.")
                    continue
                else:
                    # print("node:",i,"is added to the queue.")
                    queue.push(i)
                    close_set.add(i[0])
                    prenode_dict[i] = cur_node
    # print(result_list)
    return result_list

    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # result_list = []                                        #结果列表
    # priority_queue = util.PriorityQueue()                   #优先队列
    # # close_set = set()             
    # prenode_dict = {}                                       #父节点字典，prenode_dict[state]表示state的父节点信息
    # cur_state = problem.getStartState() 
    # # print(cur_state)
    # cur_node = (cur_state,'Start',0)
    # # close_set.add(cur_state)
    # priority_queue.push(cur_state,0)
    # prenode_dict[cur_state] = cur_node
    # while(True):
    #     cur_state = priority_queue.pop()                    #优先队列出队
    #     cur_node = prenode_dict[cur_state]
    #     # print("current position:",cur_state)
    #     # cur_state = cur_node[0]
    #     if(problem.isGoalState(cur_state)):                 #当前节点是终点，则根据父节点字典回推得到路径
    #         # cur_node = (cur_state,)
    #         # print("Search Done")
    #         while(cur_node[0] != problem.getStartState()): 
    #             result_list.append(cur_node[1])
    #             # print(prenode_dict[cur_node[0]]," is the prenode of ",cur_node)
    #             cur_node = prenode_dict[cur_node[0]]
    #         result_list.append(cur_node[1])                 #将第一步加进结果列表
    #         result_list.reverse()                           #结果列表倒转，得到答案
    #         break            
    #     cur_successors = problem.getSuccessors(cur_state)   #当前节点不是终点，则获取后继节点
    #     for i in cur_successors:                            #遍历后继节点，若某一后继节点已经在父节点字典的key中，则根据代价值更新优先队列
    #         if(i[0] in prenode_dict):                      
    #             if(i[2] + prenode_dict[cur_state][2] < prenode_dict[i[0]][2]):
    #                 prenode_dict[i[0]][1] = i[1]
    #                 prenode_dict[i[0]][2] = i[2] + prenode_dict[cur_state][2]
    #                 priority_queue.update(i[0],prenode_dict[i[0]][2])
    #                 # print(i," is updated.")
    #             else:
    #                 continue
    #         else:                                           #若该节点不在父节点字典的key中，即该节点没有探索过
    #             # close_set.add(i[0])
    #             prenode_dict[i[0]] = (cur_state,i[1],i[2] + prenode_dict[cur_state][2])
    #             priority_queue.update(i[0],prenode_dict[i[0]][2])
    #             # print(i," is added to the priority queue.")
    # return result_list
    cur_state = problem.getStartState()
    close_set = set()                       #保存所有已经探索过的位置的集合
    queue = util.PriorityQueue()            #优先队列
    queue.push((cur_state, []) ,0)
    result_list = []
    while(True):
        cur_node = queue.pop()
        result_list = cur_node[1]
        if problem.isGoalState(cur_node[0]):
            return result_list
        if cur_node[0] not in close_set:
            successors = problem.getSuccessors(cur_node[0])
            for i in successors:
                if i[0] not in close_set:
                    new_actions = result_list + [i[1]]
                    queue.update((i[0], result_list + [i[1]]), problem.getCostOfActions(new_actions))
        close_set.add(cur_node[0])
    return result_list

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # result_list = []        #结果列表
    # # priority_queue = util.PriorityQueueWithFunction(heuristic)
    # priority_queue = util.PriorityQueue()  #优先队列
    # prenode_dict = {}       #父节点字典，prenode_dict[state]表示state的父节点信息
    # cur_state = problem.getStartState()
    # cur_node = (cur_state,'Start',0)
    # priority_queue.push(cur_state,heuristic(cur_state,problem)) 
    # prenode_dict[cur_state] = (cur_state,'Start',heuristic(cur_state,problem))
    
    # while(True):
    #     cur_state = priority_queue.pop()
    #     cur_node = prenode_dict[cur_state]
    #     if(problem.isGoalState(cur_state)): #当前节点是终点，则根据父节点字典回推得到路径
    #         # cur_node = (cur_state,)
    #         # print("Search Done")
    #         while(cur_node[0] != problem.getStartState()): 
    #             result_list.append(cur_node[1])
    #             # print(prenode_dict[cur_node[0]]," is the prenode of ",cur_node)
    #             cur_node = prenode_dict[cur_node[0]]
    #         result_list.append(cur_node[1]) #将第一步加进结果列表
    #         result_list.reverse()           #结果列表倒转，得到答案
    #         break               
    #     cur_successors = problem.getSuccessors(cur_state)#当前节点不是终点，则获取后继节点
    #     for i in cur_successors:            #遍历后继节点，若某一后继节点已经在父节点字典的key中，则根据启发函数更新优先队列
    #         next_state = i[0]
    #         if(next_state in prenode_dict):
    #             if(heuristic(next_state,problem) + prenode_dict[cur_state][2] < prenode_dict[next_state][2]):
    #                 prenode_dict[next_state][1] = i[1]
    #                 prenode_dict[next_state][2] = i[2] + heuristic(next_state,problem) + prenode_dict[cur_state][2]
    #                 priority_queue.update(next_state,prenode_dict[next_state][2])
    #                 # print(i," is updated.")
    #             else:
    #                 continue
    #         else:                           #若该节点不在父节点字典的key中，即该节点没有探索过
    #             # close_set.add(next_state)
    #             prenode_dict[next_state] = (cur_state,i[1],heuristic(next_state,problem) + prenode_dict[cur_state][2])
    #             priority_queue.update(next_state,prenode_dict[next_state][2])
    #             # print(i," is added to the priority queue.")
    # return result_list
    # util.raiseNotDefined()
    cur_state = problem.getStartState()
    close_set = set()                       #保存所有已经探索过的位置的集合
    queue = util.PriorityQueue()            #优先队列
    queue.push((cur_state, []) ,nullHeuristic(cur_state,problem))
    result_list = []
    while(True):
        cur_node = queue.pop()
        result_list = cur_node[1]
        if problem.isGoalState(cur_node[0]):
            return result_list
        if cur_node[0] not in close_set:
            successors = problem.getSuccessors(cur_node[0])
            for i in successors:
                if i[0] not in close_set:
                    new_actions = result_list + [i[1]]
                    new_cost = problem.getCostOfActions(new_actions) + heuristic(i[0], problem)
                    queue.update((i[0], result_list + [i[1]]), new_cost)
        close_set.add(cur_node[0])
    return result_list
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
