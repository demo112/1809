from lxml import etree

html = """
        <div class="wrapper">
            <i class="iconfont icon-back" id="back"></i>
            <a href="/" id="channel">新浪社会</a>
            <ul id="nav">
                <li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
                <li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
                <li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
                <li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
                <li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
                <li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
                <li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
                <li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
                <li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
                <li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
            </ul>
            <i class="iconfont icon-liebiao" id="menu"></i>
        </div>
        """
parse_html = etree.HTML(html)
# 获取所有a节点下的文字
r_list = parse_html.xpath('//a/text()')
print(r_list)
# ['新浪社会', '国内', '国际', '军事', '图片', '社会', '娱乐', '科技', '体育', '财经', '汽车']

child_list = parse_html.xpath('//li/a/text()')
print(child_list)
# ['国内', '国际', '军事', '图片', '社会', '娱乐', '科技', '体育', '财经', '汽车']

href_list = parse_html.xpath('//a/@href')
print(href_list)
# ['/', 'http://domestic.firefox.sina.com/', 'http://world.firefox.sina.com/', 'http://mil.firefox.sina.com/', 'http://photo.firefox.sina.com/', 'http://society.firefox.sina.com/', 'http://ent.firefox.sina.com/', 'http://tech.firefox.sina.com/', 'http://sports.firefox.sina.com/', 'http://finance.firefox.sina.com/', 'http://auto.firefox.sina.com/']

child_href_list = parse_html.xpath('//li/a/@href')
print(child_href_list)
# ['http://domestic.firefox.sina.com/', 'http://world.firefox.sina.com/', 'http://mil.firefox.sina.com/', 'http://photo.firefox.sina.com/', 'http://society.firefox.sina.com/', 'http://ent.firefox.sina.com/', 'http://tech.firefox.sina.com/', 'http://sports.firefox.sina.com/', 'http://finance.firefox.sina.com/', 'http://auto.firefox.sina.com/']
