html = '''
<div class="warp">
    Hello, World
<p>This is a paragraph.</p>    
<div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.warp')
print(wrap.text())

print('------------')
wrap.find('p').remove()
print(wrap.text())