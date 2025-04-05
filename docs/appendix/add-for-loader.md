# **Loader补充说明**

**Apify Reader**

Apify Reader 提供了一个 Python 接口，用于与 Apify 平台交互，以实现 Web 工作流的自动化。你可以在这里获取所需要的[APIKEY](https://console.apify.com/settings/integrations)。

初始化客户端，设置所需参数。

```python
from camel.loaders import Apify
import os

os.environ["APIFY_API_KEY"] = "你的apikey"

apify = Apify()

run_input = {
    "startUrls": [{"url": "https://www.camel-ai.org/"}],
    "maxCrawlDepth": 0,
    "maxCrawlPages": 1,
}
actor_result = apify.run_actor(
    actor_id="apify/website-content-crawler", run_input=run_input
)
```

检索结果数据库 ID 并使用 get\_dataset\_items 方法访问它。

```python
dataset_result = apify.get_dataset_items(
    dataset_id=actor_result["defaultDatasetId"]
)

print(dataset_result)

>>>
[{'url': 'https://www.camel-ai.org/', 'crawl': {'loadedUrl': 'https://www.camel-ai.org/', 'loadedTime': '2025-02-06T07:11:19.056Z', 'referrerUrl': 'https://www.camel-ai.org/', 'depth': 0, 'httpStatusCode': 200}, 'metadata': {'canonicalUrl': 'https://www.camel-ai.org/', 'title': 'CAMEL-AI', 'description': 'CAMEL-AI.org is the 1st LLM multi-agent framework and an open-source community dedicated to finding the scaling law of agents.', 'author': None, 'keywords': None, 'languageCode': 'en', 'openGraph': [{'property': 'og:title', 'content': 'CAMEL-AI'}, {'property': 'og:description', 'content': 'CAMEL-AI.org is the 1st LLM multi-agent framework and an open-source community dedicated to finding the scaling law of agents.'}, {'property': 'twitter:title', 'content': 'CAMEL-AI'}, {'property': 'twitter:description', 'content': 'CAMEL-AI.org is the 1st LLM multi-agent framework and an open-source community dedicated to finding the scaling law of agents.'}, {'property': 'og:type', 'content': 'website'}], 'jsonLd': None, 'headers': {'content-type': 'text/html', 'transfer-encoding': 'chunked', 'connection': 'keep-alive', 'date': 'Wed, 05 Feb 2025 21:46:50 GMT', 'cf-ray': '90d61869d8a0ef20-PDX', 'cf-cache-status': 'MISS', 'content-encoding': 'gzip', 'last-modified': 'Wed, 05 Feb 2025 21:46:50 GMT', 'strict-transport-security': 'max-age=31536000', 'surrogate-control': 'max-age=432000', 'surrogate-key': 'www.camel-ai.org 6659a154491a54a40551bc78 pageId:6686a2bcb7ece5fb40457491 679b765c27842bdba036423f 668181a0a818ade34e653b24 6659a155491a54a40551bd7e', 'x-lambda-id': 'ce2c42a4-c711-4bd7-b262-58374d893ffa', 'set-cookie': '_cfuvid=55wNMTV.q_HQ_jKuXybjfL5A9sxw0Wd30vX5Ff26cJA-1738792010775-0.0.1.1-604800000; path=/; domain=.cdn.webflow.com; HttpOnly; Secure; SameSite=None', 'x-cluster-name': 'us-west-2-prod-hosting-red', 'vary': 'Accept-Encoding', 'x-cache': 'Hit from cloudfront', 'via': '1.1 6a783450a00c2b23baf9dd1c4a552cb0.cloudfront.net (CloudFront)', 'x-amz-cf-pop': 'LAX54-P3', 'x-amz-cf-id': 't9nN-HwYopeCl40sOYSwOcFNJJT3I_KFOsxZuiD3I_23GLC9K5OEBA==', 'age': '33862'}}, 'screenshotUrl': None, 'text': 'Building Multi-AgentSystems for World Simu_\nCAMEL’s multi-agent approach streamlines large-scale synthetic data creation and labeling. By assigning different specialized roles to each agent, it encourages dynamic, chain-of-thought collaborations that yield high-quality outputs. The orchestrated interaction ensures comprehensive coverage of data variations and consistency across domains. This makes it ideal for generating training sets, question-answer pairs, or other structured content.\nCAMEL powers automated workflows by breaking down complex tasks among coordinated agents. Each agent assumes a specific role, collaborating through an iterative conversational framework. This reduces manual intervention, minimizes errors, and accelerates solution delivery—especially useful for repetitive or logic-intensive processes.\nCAMEL enables simulations of dynamic, interactive worlds. Agents act as entities with distinct personas, communicating and responding in real time. This setup can be used for modeling scenarios, building interactive storylines, or testing multi-layered strategies. By capturing the nuances of diverse viewpoints, CAMEL creates immersive simulations for experimentation, training, and creative exploration.', 'markdown': '# Building Multi-AgentSystems for World Simu\\_\n\nCAMEL’s multi-agent approach streamlines large-scale synthetic data creation and labeling. By assigning different specialized roles to each agent, it encourages dynamic, chain-of-thought collaborations that yield high-quality outputs. The orchestrated interaction ensures comprehensive coverage of data variations and consistency across domains. This makes it ideal for generating training sets, question-answer pairs, or other structured content.\n\n![](https://cdn.prod.website-files.com/6659a154491a54a40551bc78/672e156ad52bd8476c306541_Customise%20agents.png)\n\nCAMEL powers automated workflows by breaking down complex tasks among coordinated agents. Each agent assumes a specific role, collaborating through an iterative conversational framework. This reduces manual intervention, minimizes errors, and accelerates solution delivery—especially useful for repetitive or logic-intensive processes.\n\n![](https://cdn.prod.website-files.com/6659a154491a54a40551bc78/672e1566bf0de60de5388268_Multi-agent.png)\n\nCAMEL enables simulations of dynamic, interactive worlds. Agents act as entities with distinct personas, communicating and responding in real time. This setup can be used for modeling scenarios, building interactive storylines, or testing multi-layered strategies. By capturing the nuances of diverse viewpoints, CAMEL creates immersive simulations for experimentation, training, and creative exploration.\n\n![](https://cdn.prod.website-files.com/6659a154491a54a40551bc78/672e1566b57b7e778cfe6253_Data%20Generation.png)'}]
```

这个函数通常用于从Apify平台获取爬取或处理后的数据，以便在后续程序中使用这些数据。

***

**Firecrawl Reader**

你可以从[此处](https://www.firecrawl.dev/)获得你的FirecrawlAPI

Firecrawl Reader 提供了一个 Python 接口来与 Firecrawl API 交互，允许用户将网站转换为大型语言模型可读的 markdown 格式。

初始化客户端并设置要从中检索信息的 URL。当状态为 “completed” 时，信息检索已完成并可供阅读。

```python
from camel.loaders import Firecrawl

os.environ["FIRECRAWL_API_KEY"] = "你的apikey"

firecrawl = Firecrawl()

response = firecrawl.crawl(url="https://www.camel-ai.org/about")
print(response["status"])

>>>
completed
```

直接从返回的结果中检索信息。

```python
print(response["data"][0]["markdown"])
```

```python
>>>Camel-AI Team

We are finding the  
scaling law of agent

🐫 CAMEL is an open-source library designed for the study of autonomous and 
communicative agents. We believe that studying these agents on a large scale 
offers valuable insights into their behaviors, capabilities, and potential 
risks. To facilitate research in this field, we implement and support various 
types of agents, tasks, prompts, models, and simulated environments.

**We are** always looking for more **contributors** and **collaborators**.  
Contact us to join forces via [Slack](https://join.slack.com/t/camel-kwr1314/shared_invite/zt-1vy8u9lbo-ZQmhIAyWSEfSwLCl2r2eKA)
 or [Discord](https://discord.gg/CNcNpquyDc)...
```

***

**Jina\_url Reader**

JinaURL Reader 是 Jina AI 的 URL 读取服务的 Python 客户端，经过优化，可从 URL 提供更清晰、对 LLM 可读的内容。该reader提供一定额度的免费调用次数。无需注册API也可使用。

```python
from camel.loaders import JinaURLReader
from camel.types.enums import JinaReturnFormat

jina_reader = JinaURLReader(return_format=JinaReturnFormat.MARKDOWN)
response = jina_reader.read_content("https://www.datawhale.cn/home")

print(response)

>>>
Datawhale-学用AI，从此开始
===============  

![Image 1: logo](https://www.datawhale.cn/assets/logo-vAxrscYT.png)

[HOME首页](https://www.datawhale.cn/home)[OPEN 1+XAI 通识课](https://www.datawhale.cn/open-ai)[ACTIVITY活动](https://www.datawhale.cn/activity)[COURSE课程](https://www.datawhale.cn/learn)[CERTIFICATION认证](https://www.datawhale.cn/cert)[NEWS资讯](https://www.datawhale.cn/article)

![Image 2: wechat](blob:https://www.datawhale.cn/cfd0357cb7301be8879b48a64347d08f)![Image 3: wechat](https://www.datawhale.cn/assets/wechat-qrcode-CPBf96kV.png)

[![Image 4: github](blob:https://www.datawhale.cn/4d659f53c87d622c9cafa1b45920725f)](https://github.com/datawhalechina)

登录

![Image 5](https://www.datawhale.cn/assets/homebanner-left-DQp9I1cY.png)

Datawhale for the learner

![Image 6](https://www.datawhale.cn/assets/banner-title-CqrNZXqM.png)

Datawhale通过开源学习模式，助力AI学习者与知识连接，与人连接，与场景连接，推动AI人才培养。

![Image 7](https://www.datawhale.cn/assets/homebanner-swiper1-CnhP9rkt.png)

![Image 8: logo](blob:https://www.datawhale.cn/7dd095def689b2660c34f51de0662bf6)
...

社交媒体[GITHUB](https://github.com/datawhalechina) [B站](https://space.bilibili.com/431850986) [CSDN](https://blog.csdn.net/Datawhale)

[![Image 30](blob:https://www.datawhale.cn/a1d2760e5d7b70d1dbb76b573944cb7f) 我要反馈](https://jinshuju.net/f/gtuc5x)
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```