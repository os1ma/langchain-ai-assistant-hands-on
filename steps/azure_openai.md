# Azure OpenAI を使用する場合のコードの変更箇所

OpenAI API の障害などにより Azure OpenAI を使う必要がある場合のコードの変更箇所です。

agent_app.py は次のように変更します。

```
from langchain.chat_models import AzureChatOpenAI

        :

    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True)
    llm = AzureChatOpenAI(
        openai_api_base="your-api-base",
        openai_api_version="2023-07-01-preview",
        deployment_name="your-deployment-name",
        openai_api_key=os.environ["OPENAI_API_KEY"],
        openai_api_type="azure",
        temperature=0,
        streaming=True,
    )
```
