import os
import gradio as gr
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv

load_dotenv()


def analyze_food_calories(image: Image.Image) -> str:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "錯誤：未設定 GOOGLE_API_KEY，請在 .env 檔案或環境變數中設定。"

    client = genai.Client(api_key=api_key)

    prompt = """請分析這張圖片中的食物，並以繁體中文回答。

步驟一：判斷圖片中是否有食物。
- 如果圖片中沒有食物，請只回覆：「這個不是食物」
- 如果有食物，請繼續步驟二。

步驟二：列出每樣食物的名稱與估計熱量（大卡/kcal），格式如下：

## 食物熱量分析

| 食物名稱 | 份量（估計） | 熱量（kcal） |
|----------|------------|-------------|
| 食物1    | xxx g      | xxx kcal    |
| 食物2    | xxx g      | xxx kcal    |

**總熱量：約 xxx kcal**

> 備註：以上熱量為估計值，實際數值可能因烹調方式、份量而有所差異。"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt, image],
        )
        return response.text
    except Exception as e:
        return f"錯誤：{e}"


with gr.Blocks(title="食物熱量分析") as demo:
    gr.Markdown("# 食物熱量分析器")
    gr.Markdown("上傳一張食物照片，AI 將為你估算熱量。")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="上傳食物照片")
            submit_btn = gr.Button("分析熱量", variant="primary")
        with gr.Column():
            output = gr.Markdown(label="分析結果")

    submit_btn.click(
        fn=analyze_food_calories,
        inputs=image_input,
        outputs=output,
    )


if __name__ == "__main__":
    demo.launch()
