import requests
import time

def get_multiple_image_urls(num_images=5, delay=1):
    """
    获取多个图片直链并保存到文件
    num_images: 需要获取的图片数量
    delay: 每次请求之间的延迟(秒)
    """
    image_urls = []
    api_url = "https://api.lolicon.app/setu/v2"
    
    for i in range(num_images):
        try:
            response = requests.get(api_url)
            data = response.json()
            
            if data["data"]:
                image_url = data["data"][0]["urls"]["original"]
                image_urls.append(image_url)
                print(f"已获取第 {i+1} 个图片直链: {image_url}")
            else:
                print(f"第 {i+1} 次请求失败")
                
            if i < num_images - 1:
                time.sleep(delay)
                
        except Exception as e:
            print(f"第 {i+1} 次请求发生错误: {str(e)}")
            continue
    
    # 将直链写入文件
    try:
        with open('tu.txt', 'a', encoding='utf-8') as f:
            for url in image_urls:
                f.write(url + '\n')
        print(f"\n已成功将 {len(image_urls)} 个直链保存到 tu.txt 文件中")
    except Exception as e:
        print(f"写入文件时发生错误: {str(e)}")
    
    return image_urls

# 调用函数获取5个图片直链
urls = get_multiple_image_urls(num_images=1000, delay=0)
