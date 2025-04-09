from langgraph.graph import END
from messageState.agentState import AgentState
def check_route_condition(state: AgentState):
    # 根据审查结果决定路由
    if state['check_result'] == 0:# 不符合原文
        return "modifyNode"
    return END