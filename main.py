from openai import OpenAI

client = OpenAI(
    api_key ="",
    base_url="https://api.deepseek.com/v1"
)


def read_email(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()

system_promt = """Ты специалист по безопастности  фишингу. Ты должен читать электронные письма и анализировать безопасные они или нет. 
Смотри на признаки, подрепи свой вердикт. Напиши совет конкретно по этому письму. Твой ответ должен состоять из трех частей вердикт, признаки и советы.
Вердикт напиши намного короче, признаки пронумеруй и не пиши в них лишней воды, совет дай небольшой на 3-5 предложений.
Пиши без MARKDOWN.
"""

def check_email(text):
    response =  client.chat.completions.create(
        model = "deepseek-chat",
        messages= [
            {"role":"system","content":system_promt},
            {"role":"user","content":text}
        ],
        temperature= 0.2
    )
    return response.choices[0].message.content

a = read_email("email.txt")
print(check_email(a))