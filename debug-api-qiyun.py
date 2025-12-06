# #!/usr/bin/env python3
# """
# 调试七牛云API请求格式
# """
# import requests
# import json

# def test_qiniu_api_formats():
#     """测试不同的API请求格式"""
    
#     api_key = "sk-f2382493b0eb9e1a126fddbb77603398818dcaa2eb5838ba44ebdf2b977aebd1"
#     model = "qwen3-32b"
    
#     # 测试数据 - 模拟GraphRAG的实体合并请求
#     test_messages = [
#         {
#             "role": "system",
#             "content": "You are an expert in entity resolution and disambiguation."
#         },
#         {
#             "role": "user", 
#             "content": "请分析以下实体是否指向同一个对象，并给出合并建议：\n实体1: OpenAI\n实体2: OpenAI公司\n请回答是否应该合并这两个实体。"
#         }
#     ]
    
#     # 测试不同的API端点
#     endpoints = [
#         "https://openai.qiniu.com/v1/chat/completions",
#         "https://openai.qiniu.com/chat/completions",
#         "https://api.qiniu.com/v1/chat/completions"
#     ]
    
#     for endpoint in endpoints:
#         print(f"\n🔍 测试端点: {endpoint}")
        
#         # 基本请求格式
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {api_key}"
#         }
        
#         data = {
#             "model": model,
#             "messages": test_messages,
#             "max_tokens": 500,
#             "temperature": 0.0
#         }
        
#         try:
#             response = requests.post(endpoint, headers=headers, json=data, timeout=30)
#             print(f"状态码: {response.status_code}")
            
#             if response.status_code == 200:
#                 print("✅ 请求成功")
#                 result = response.json()
#                 print(f"响应: {result['choices'][0]['message']['content'][:100]}...")
#                 return endpoint  # 返回成功的端点
#             else:
#                 print(f"❌ 请求失败: {response.text}")
                
#         except Exception as e:
#             print(f"❌ 连接错误: {e}")
    
#     return None

# def test_different_parameters():
#     """测试不同的请求参数"""
    
#     api_key = "sk-f2382493b0eb9e1a126fddbb77603398818dcaa2eb5838ba44ebdf2b977aebd1"
#     endpoint = "https://openai.qiniu.com/v1/chat/completions"
    
#     # 测试不同的参数组合
#     test_configs = [
#         {
#             "name": "标准配置",
#             "params": {
#                 "model": "qwen3-32b",
#                 "messages": [{"role": "user", "content": "测试消息"}],
#                 "max_tokens": 100,
#                 "temperature": 0.0
#             }
#         },
#         {
#             "name": "无temperature",
#             "params": {
#                 "model": "qwen3-32b", 
#                 "messages": [{"role": "user", "content": "测试消息"}],
#                 "max_tokens": 100
#             }
#         },
#         {
#             "name": "不同模型名称",
#             "params": {
#                 "model": "qwen-32b",  # 去掉数字3试试
#                 "messages": [{"role": "user", "content": "测试消息"}],
#                 "max_tokens": 100
#             }
#         },
#         {
#             "name": "简化请求",
#             "params": {
#                 "model": "qwen3-32b",
#                 "messages": [{"role": "user", "content": "Hello"}]
#             }
#         }
#     ]
    
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }
    
#     for config in test_configs:
#         print(f"\n🔍 测试配置: {config['name']}")
#         try:
#             response = requests.post(endpoint, headers=headers, json=config['params'], timeout=30)
#             print(f"状态码: {response.status_code}")
            
#             if response.status_code == 200:
#                 print("✅ 成功")
#                 result = response.json()
#                 print(f"响应: {result['choices'][0]['message']['content'][:50]}...")
#             else:
#                 print(f"❌ 失败: {response.text}")
                
#         except Exception as e:
#             print(f"❌ 错误: {e}")

# def check_qiniu_api_docs():
#     """检查七牛云API文档"""
#     print("\n📚 七牛云API可能的问题:")
#     print("1. 模型名称不正确 (qwen3-32b vs qwen-32b)")
#     print("2. API端点路径不正确")
#     print("3. 请求参数格式有限制")
#     print("4. 认证方式有问题")
#     print("5. 请求频率限制")

# if __name__ == "__main__":
#     print("🔧 七牛云API调试工具")
#     print("=" * 50)
    
#     # 测试不同端点
#     working_endpoint = test_qiniu_api_formats()
    
#     if working_endpoint:
#         print(f"\n✅ 找到可用端点: {working_endpoint}")
#     else:
#         print("\n❌ 所有端点都失败，测试不同参数...")
#         test_different_parameters()
    
#     # 显示可能的问题
#     check_qiniu_api_docs()



import os, requests, json
url = "https://openai.com/v1/chat/completions"   # 换成真实端点
headers = {
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY_LLM')}",
    "Content-Type": "application/json"
}
payload = {
    "model": "qwen3-32b",
    "messages": [{"role": "user", "content": "ping"}]
}
resp = requests.post(url, headers=headers, json=payload, timeout=10)
print(resp.status_code, resp.text)

