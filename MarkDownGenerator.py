import json
import os

for file in os.listdir('helpers\content summarization\summarizedContent'):
    with open(f'helpers\content summarization\summarizedContent\{file}','r') as contentFile:
        data=json.load(contentFile)
    markdown_text=f"# {data['article_title']}\n#### link to the original article --> {data['article_url']}\n\n### {data['summary'][0]}\n\n![{data['article_title']}]({data['article_image']})"
    with open(fr"SummarizedContentAsMarkdown\{data['article_title']}.md",'w') as writeFile:
        writeFile.write(markdown_text)