## OPENAI API_KEY

Type: str
Required: True

OpenAIのAPI_KEYを書く．

<https://platform.openai.com/account/api-keys>から取得する．

## GPT_MODEL

Type: str
Required: True

使いたいGPTモデルを書く．

- gpt-3.5-turbo
- text-davinci-003
- gpt-4 (in waitlist)
- gpt-4-32k (in waitlist)

<https://platform.openai.com/docs/models/overview>

## TEMPERATURE

Type: float
Required: False(Default: 1)

0-2 の間で指定する．
大きいほど多様な出力になる．(注：Bing AIとかで言うところの「創造的」というやつになる．)

<https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature>
