from bs4 import BeautifulSoup

html = """
        <div class='test1'>雄霸</div>
        <div class='test1'>幽若</div> 
        
        <div class='test2'>
        <span>第二梦</span>
        </div>"""

soup = BeautifulSoup(html, 'lxml')
r_list = soup.find_all('div', {'class': 'test1'})
for r in r_list:
    print(r.get_text())

soup1 = BeautifulSoup(html, 'lxml')
t_list1 = soup.find_all('div', {'class': 'test2'})
for r in t_list1:
    print(r.span.string)
