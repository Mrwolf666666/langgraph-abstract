from messageState.agentState import AgentState
from config.promptConfig import polish_prompt
from util.llm import call_llm
def polish_node(state: AgentState) -> AgentState:
    task_id = state['task_id']
    print(f"任务ID为{task_id},进入润色节点")
    abstract_text = state['abstract_text']
    if abstract_text is None:
        print("摘要文本为空")
    else:
        system_prompt = polish_prompt
        user_prompt = f"需要润色的摘要为：{abstract_text}"
        polish_text = call_llm(user_prompt,system_prompt)
        state['polish_text'] = polish_text
    return state