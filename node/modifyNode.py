from messageState.agentState import AgentState
from config.promptConfig import modify_prompt
from util.llm import call_llm

def modify_node(state: AgentState) -> AgentState:
    task_id = state['task_id']
    print(f"任务ID为{task_id},进入修改节点")
    original_text = state['original_text']
    polish_text = state['polish_text']
    check_reason = state['check_reason']
    if original_text is None:
        print("原文为空")
    elif check_reason is None:
        print("修改意见为空")
    else:
        system_prompt = modify_prompt
        user_prompt = f"资讯原文为：{original_text}，摘要为：{polish_text}，摘要中出现的问题为：{check_reason}"
        modify_text = call_llm(user_prompt,system_prompt)
        state['polish_text'] = modify_text
    return state