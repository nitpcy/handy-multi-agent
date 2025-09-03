from camel.toolkits import SearchToolkit
from pprint import pprint 

if __name__ == "__main__":

    # --- 示例1：使用新增的图片搜索 ---
    print("--- 正在执行图片搜索 ---")
    image_query = "鄱阳湖国家湿地公园的图片"
    image_results = SearchToolkit().search_bing_images(query=image_query, max_results=2)
    pprint(type(image_results))
    pprint(image_results)
    print("--- 图片搜索完成 ---")
    print(image_results[0]["image_url"])

# import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)