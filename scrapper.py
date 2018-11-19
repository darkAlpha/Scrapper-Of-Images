
# coding: utf-8

# In[17]:


from requests import get
url = "https://www.lamoda.kz/b/1061/brand-adidas/"
response = get(url)
print(response.text[:10000])


# In[18]:



from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)




# In[35]:


# clothes_container = html_soup.find_all('div', class_ = 'products-list-item dyother dyMonitor')
# clothes_container = html_soup.find_all('div', class_ = 'products-catalog__list')
clothes_container = html_soup.find_all('div', class_ = 'products-list-item')


print(type(clothes_container))
print(len(clothes_container))


# In[36]:


first_clothes = clothes_container[0]
first_clothes

