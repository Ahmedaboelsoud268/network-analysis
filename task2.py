#!/usr/bin/env python
# coding: utf-8

# In[6]:


import networkx as nx


# In[7]:


nx.__version__


# In[158]:


G = nx.Graph()
G.add_node('a')
nodes_to_add =['b','c','d']
G.add_nodes_from(nodes_to_add)
G.add_edge('a','b')
edges_to_add=[('a','c'), ('b','c'), ('c','d')]
G.add_edges_from(edges_to_add)
nx.draw(G, with_labels=True, node_color='green', node_size=1000,font_color='white', font_size=30)


# In[60]:


list(G.neighbors('b'))

for neighbor in G.neighbors('a'):
    print(neighbor)
nx.is_tree(G)


# In[46]:


nx.is_connected(G)


# In[49]:


G.has_node('f')


# In[51]:


G.has_edge('a','b')


# In[53]:


G.has_edge('a','d')


# In[59]:


('a','d') in G.edges


# In[57]:


('a','c') in G.edges


# In[64]:


len(list(G.neighbors('c')))


# In[69]:


G.degree('d')


# In[119]:


#ex1
a=[]
def get_leaves(x):
    for node in x.nodes:
        if x.degree(node)==1:
            a.append(node)
    return a            
get_leaves(G)
    


# In[159]:


#ex3
l=[]
def mutual_friends(g, node_1, node_2):
    n1=list(g.neighbors(node_1))
    n2=list(g.neighbors(node_2))
    for node1 in n1:
        for node2 in n2:
            if node1==node2:
                l.append(node1)
    return l

mutual_friends(G, 'a', 'b')


# In[147]:


#ex2
l=[]
def max_degree(G):
    d=0
    n=''
    for node in G.nodes:
        if d < G.degree(node):
            d=G.degree(node)
            n=node
    l.append(('name',n))
    l.append(('degree',d))
    return l 
max_degree(G)


# In[118]:


x=['ahmed','a','aboelsoud']
[x.upper() for x in x]


# In[100]:


max(len(x) for x in  x)


# In[102]:


min(len(x) for x in x)


# In[150]:


c=nx.Graph()
c.add_nodes_from(['asd','asd1','asd2','asd3'])
c.add_edge('asd2','asd1')
nx.draw(c,with_labels=True, node_color='red',font_size='15', node_size=1000)


# In[153]:




