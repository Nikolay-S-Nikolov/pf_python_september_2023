article_title = input()
article_content = input()
print('<h1>')
print(f'    {article_title}')
print('</h1>')
print('<article>')
print(f'    {article_content}')
print('</article>')
while True:
    article_comments = input()
    if article_comments == "end of comments":
        break
    print('<div>')
    print(f'    {article_comments}')
    print('</div>')
