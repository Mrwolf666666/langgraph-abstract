from messageState.agentState import AgentState
from config.promptConfig import abstract_prompt
from util.llm import call_llm

def abstract_node(state: AgentState) -> AgentState:
    task_id = state['task_id']
    print(f"任务ID为{task_id},进入摘要节点")
    original_text = state['original_text']
    if original_text is None:
        print("原文为空")
    else:
        system_prompt = abstract_prompt
        user_prompt = f"需要生成摘要的原文为{original_text}"
        abstract_text = call_llm(user_prompt,system_prompt)
        state['abstract_text'] = abstract_text
    return state