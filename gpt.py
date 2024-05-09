from openai import OpenAI

client = OpenAI(api_key="Your API key here")

#while True:
ask = input("Enter Link:")

 #   if ask == "break":
  #      print("Thank you.")
   #     break
    #else:
response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"What is the category of website {ask}"
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
print(response.choices[0].message.content)
       