# Quora Poe reverse-engineered API
This is a self hostable, reverse-engineered API for Quora's Poe that allows access to the following chatbots:

1. Sage - OpenAI (capybara)
4. Claude - Anthropic (a2)
5. ChatGPT - OpenAI (chinchilla)
### Requirements
To use this API, you will need to have the following cookies:

2. Quora-Formkey: This is obtained by logging in to Quora.com, viewing the page source, and finding the "formkey" dictionary key (Normally line 14). Use its value in the Quora-Formkey field.
3. Cookie: 'm-b=xxxx' - This is the value of the cookie with the key m-b, which is present in the list of cookies used on Quora.com (not poe.com), you can simply inspect cookies in Chrome to get it.
### Setup
<details>
<summary>Simple Setup</summary>

<br>

- Clone this repository

```bash
git clone https://github.com/aspekts/PoeAPI.git
```

- Install dependencies

```bash
pip install requests uvicorn fastapi
```

- Run the API

```bash
uvicorn api:app --reload
```

- Verify that the API is running by running:

```bash
curl localhost:8000
```

- Get a url for the API by running:

```bash
ngrok http 8000
```

Access that URL in your browser to confirm it works. This is your bot server URL.
</details>

### Example
```bash
curl http://127.0.0.1/chat/capybara -H "Cookie: m-b=xxxx" -H "formkey: xxxxx" -d '{"message":"What is the meaning of life?"}'
```
Response:
```json
{"message":"The meaning of life is to live it.","status":"success", "chat_id": "xxxxx"}
```

### Disclaimer
This repository is for educational and research purposes only, and the use of this API for any other purpose is at your own risk. We are not responsible for any actions taken by users of this API.

### Credits

POE.com Reverse Engineered CLI - [Credits to Vaibhavk97](https://github.com/vaibhavk97/Poe)
