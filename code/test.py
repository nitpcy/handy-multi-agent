import os

from camel.agents import ChatAgent
from camel.configs import ZhipuAIConfig
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


# model = ModelFactory.create(
#     model_platform=ModelPlatformType.ZHIPU,
#     model_type=ModelType.GLM_4,
#     model_config_dict=ZhipuAIConfig(temperature=0.2).as_dict(),
#     api_key=os.environ.get("ZHIPUAI_API_KEY"),
#     url=os.environ.get("ZHIPUAI_API_BASE_URL"),
# )
# model = ModelFactory.create(
#     model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
#     model_type="Qwen/Qwen2.5-72B-Instruct",
#     url='https://api-inference.modelscope.cn/v1/',
#     api_key=os.getenv('ModelFactory_Key')
# )
model = ModelFactory.create(
    model_platform=ModelPlatformType.QWEN,
    model_type=ModelType.QWEN_MAX,
    model_config_dict={"temperature": 0},
    api_key=os.getenv('QWEN_MAX_API_KEY')
)
agent = ChatAgent(model=model)
response = agent.step("你是谁?")
print(response)