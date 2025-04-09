from typing import TypedDict
# 定义状态类型
class AgentState(TypedDict):
    task_id: str         # 任务ID
    original_text: str   # 原始文本
    abstract_text: str   # 摘要文本
    polish_text: str     # 修改文本
    check_result: int    # 审查结果
    check_reason: str    # 审查理由
