import requests

url = "https://api.openai.com/v1/chat/completions"
api_key = "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"  # Dán API key thật vào đây

print("=== CHATBOT TRỢ GIẢNG (Gõ 'thoát' để dừng) ===")

while True:
    user_input = input("Anh: ")
    
    if user_input.lower() == 'thoát':
        print("Chatbot: Tạm biệt!")
        break

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Bạn là trợ giảng thân thiện. Hãy trả lời ngắn gọn."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        
        # Lấy nội dung câu trả lời từ API
        bot_reply = result['choices'][0]['message']['content']
        print(f"Chatbot: {bot_reply}\n")
        
    except Exception:
        print("Chatbot: Lỗi kết nối hoặc API Key chưa đúng. Vui lòng kiểm tra lại!\n")