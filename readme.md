# Summarized-Energy-Feed

### submission for the ****Schlumberger's New Year Hackathon****

### (there are links in the project too, all the references in this file, it will take you to the particular resource.)

# Introduction

The task for the hackathon was to take an existing news feed about energy and carbon, and then summarize the content of the website. This pdf will explain how I solved this task in a short and concise manner. the code for the project is on [GitHub](https://github.com/realhardik18/Summarized-Energy-Feed).

# Getting the links to all the blogs

the problem statement listed 4 feeds from which we could crawl and summarize the content from. I decided to go with [MIT climate portal](https://climate.mit.edu/). Then I wrote a [script](https://github.com/realhardik18/Summarized-Energy-Feed/blob/master/helpers/crawler/crawler.py) to get the links of all the blogs on the website and save it to a [text file](https://github.com/realhardik18/Summarized-Energy-Feed/blob/master/helpers/crawler/links.txt)

# Summarizing the content

after getting all the links, I then started looking for NLP tools I could use to summarize the content. Eventually I decided to go with [TLDRThis](https://rapidapi.com/tldrthishq-tldrthishq-default/api/tldrthis) on [RapidAPI](https://rapidapi.com/hub). I then wrote a [script](https://github.com/realhardik18/Summarized-Energy-Feed/blob/master/helpers/content%20summarization/main.py) to summarize all the content from the websites and save them along with additional information in a [folder](https://github.com/realhardik18/Summarized-Energy-Feed/tree/master/helpers/content%20summarization/summarizedContent) as a JSON file.

# Displaying the summarized content

to showcase the summary of each of these articles, I created a [markdown generator](https://github.com/realhardik18/Summarized-Energy-Feed/blob/master/MarkDownGenerator.py) which took the summarized content and created a nice looking markdown file. these markdown files were then saved in a [folder](https://github.com/realhardik18/Summarized-Energy-Feed/tree/master/SummarizedContentAsMarkdown).

# What can be improved/added

even though the project does exactly what it was meant to do, if I had some more time I’d add/work on the following things

- work on getting more content from other resources
- work on making it real time (the moment a website would launch a new article, it would add it to the summarized feed automatically)
- making the whole feed into its own website

# Thank you!