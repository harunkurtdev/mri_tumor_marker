from bs4 import BeautifulSoup

html = """<body>
            <table>
                <tbody>
                    <tr>
                        <td>
                            <table>
                                <tbody>
                                    <tr>
                                        <td>
                                            <div>
                                                <div>
                                                    <ul>
                                                        <li>item 1</li>
                                                        <li>item 2</li>
                                                        <li>item 3</li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </body>"""

soup = BeautifulSoup(html, 'html.parser')

ul_list = soup.select_one('body > table > tbody > tr:nth-child(5) > td:nth-child(1) > table > tbody > tr > td:nth-child(1) > div > div > ul')
ul_list = soup.select_one('div > ul')

print(ul_list)
for li in ul_list.find_all('li'):
    print(li.string)
