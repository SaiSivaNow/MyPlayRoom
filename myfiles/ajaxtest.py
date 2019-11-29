import requests

payload ={
    'RequestVerificationToken':'969Kk9vPlhQOAqgQXMXX-1Z_nHC8YtXbgl1VLa05QCyPopl7kXO_RzmSAubLPq33mjiILnzRRPOYZKFDPZn6OJyBHS7tfZ0zZgpXwqQphFzOyxJj3VkZ72rghQ1RRdLS5gWwlQ2',
    'Rank':'-1',
    'Type':'-1',
    'Nature':'-1',
    'SubNature':'-1',
    'cmdAum':'1',
    'Period':'1Year',
    'ShortingOrder':'DESC',
    'hdHeaderId':'1Year'
    }

session =requests.Session()

session.head('https://www.mutualfundindia.com/MF/return/TopFunds?id=3')

response=session.get('https://www.mutualfundindia.com/MF/return/TopFunds?dataMfiPageIndex=1',data=payload)
print(response.text)
