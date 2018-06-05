import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/wiki/"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <h1 id="firstHeading" class="firstHeading" lang="zh-CN">美国</h1>
        title_node = soup.find('h1', id="firstHeading", class_="firstHeading")
        res_data['title'] = title_node.get_text()

        # <p><b>美利坚合众国</b>（<span class="LangWithName">英语：<span lang="en"><b>United States of America</b></span></span>，简称为 <span lang="en">United States</span>、<span lang="en">America</span>、<span lang="en">The States</span>，缩写为 <span lang="en">U.S.A.</span>、<span lang="en">U.S.</span>），通称<b>美国</b>，是由其下辖50个<a href="/wiki/%E7%BE%8E%E5%9B%BD%E5%B7%9E%E4%BB%BD" title="美国州份">州</a>、<a href="/wiki/%E8%8F%AF%E7%9B%9B%E9%A0%93%E5%93%A5%E5%80%AB%E6%AF%94%E4%BA%9E%E7%89%B9%E5%8D%80" class="mw-redirect" title="华盛顿哥伦比亚特区">华盛顿哥伦比亚特区</a>、<a href="/wiki/%E7%BE%8E%E5%9B%BD%E9%A2%86%E5%9C%9F#非合并建制领土" class="mw-redirect" title="美国领土">五个自治领土</a>及<a href="/wiki/%E7%BE%8E%E5%9B%BD%E6%9C%AC%E5%9C%9F%E5%A4%96%E5%B0%8F%E5%B2%9B%E5%B1%BF" title="美国本土外小岛屿">外岛</a>共同组成的<a href="/wiki/%E8%81%94%E9%82%A6" class="mw-redirect" title="联邦">联邦</a><a href="/wiki/%E5%85%B1%E5%92%8C%E5%88%B6" title="共和制">共和国</a><span id="noteTag-cite_ref-sup"><sup id="cite_ref-16" class="reference"><a href="#cite_note-16">[注 1]</a></sup></span>。<a href="/wiki/%E7%BE%8E%E5%9C%8B%E6%9C%AC%E5%9C%9F" title="美国本土">美国本土48州和联邦特区</a>位于<a href="/wiki/%E5%8C%97%E7%BE%8E%E6%B4%B2" title="北美洲">北美洲</a>中部，东临<a href="/wiki/%E5%A4%A7%E8%A5%BF%E6%B4%8B" title="大西洋">大西洋</a>，西临<a href="/wiki/%E5%A4%AA%E5%B9%B3%E6%B4%8B" title="太平洋">太平洋</a>，北面是<a href="/wiki/%E5%8A%A0%E6%8B%BF%E5%A4%A7" title="加拿大">加拿大</a>，南部和<a href="/wiki/%E5%A2%A8%E8%A5%BF%E5%93%A5" title="墨西哥">墨西哥</a>及<a href="/wiki/%E5%A2%A8%E8%A5%BF%E5%93%A5%E7%81%A3" class="mw-redirect" title="墨西哥湾">墨西哥湾</a>接壤，本土位于温带、副热带地区。<a href="/wiki/%E9%98%BF%E6%8B%89%E6%96%AF%E5%8A%A0%E5%B7%9E" title="阿拉斯加州">阿拉斯加州</a>位于北美大陆西北方，东部为加拿大，西隔<a href="/wiki/%E7%99%BD%E4%BB%A4%E6%B5%B7%E5%B3%BD" class="mw-redirect" title="白令海峡">白令海峡</a>和<a href="/wiki/%E4%BF%84%E7%BE%85%E6%96%AF" class="mw-redirect" title="俄罗斯">俄罗斯</a>相望；<a href="/wiki/%E5%A4%8F%E5%A8%81%E5%A4%B7%E5%B7%9E" title="夏威夷州">夏威夷州</a>则是太平洋中部的<a href="/wiki/%E7%BE%A4%E5%B3%B6" title="群岛">群岛</a>。美国在<a href="/wiki/%E5%8A%A0%E5%8B%92%E6%AF%94%E6%B5%B7" title="加勒比海">加勒比海</a>和太平洋还拥有多处<a href="/wiki/%E7%BE%8E%E5%9C%8B%E9%A0%98%E5%9C%9F" class="mw-redirect" title="美国领土">境外领土</a>和<a href="/wiki/%E5%B3%B6%E5%B6%BC%E5%9C%B0%E5%8D%80" title="岛屿地区">岛屿地区</a>。此外，美国还在全球140多个国家和地区拥有着374个海外<a href="/wiki/%E8%BB%8D%E4%BA%8B%E5%9F%BA%E5%9C%B0" class="mw-redirect" title="军事基地">军事基地</a>。</p>
        summary_node = soup.find('p')
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
