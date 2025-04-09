from messageState.agentState import AgentState
from config.promptConfig import check_prompt
from util.llm import call_llm
import json
import re
def check_node(state: AgentState) -> AgentState:
    task_id = state['task_id']
    print(f"任务ID为{task_id},进入审查节点")
    original_text = state['original_text']
    polish_text = state['polish_text']
    if original_text is None:
        print("原文为空")
    elif polish_text is None:
        print("修改文本为空")
    else:
        system_prompt = check_prompt
        user_prompt = f"""
        原文：{original_text}
        需要审查的摘要：{polish_text}
        """
        check_response = call_llm(user_prompt,system_prompt)
        # 从字符串中提取出json内容
        pattern = r'\{[^{}]*\}'
        matches = re.findall(pattern, check_response)
        check_response_json = json.loads(matches[0])
        check_result = check_response_json['result']
        state['check_result'] = check_result
        check_reason = check_response_json['reason']
        state['check_reason'] = check_reason

    return state