import requests
from config.llmConfig import model,base_url
def call_llm(user_prompt,system_prompt):
    result = ""
    request_json = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "stream": False,
        "stop": []
    }

    # 发起post请求
    response = requests.post(url=base_url, json=request_json)

    # 检查请求是否成功
    if response.status_code == 200:
        # 获取响应内容
        response_data = response.json()
        result = response_data['choices'][0]['message']['content']
        print(result)

    return result