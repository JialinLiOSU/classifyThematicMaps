# use google images api to download map images
# importing google_images_download module 
from google_images_download import google_images_download  
def downloadimages(query): 
    arguments = {"keywords": query, "format": "png", "limit":100, 
                    "print_urls":True, "size": "medium",
                    "chromedriver":"C:\\Program Files (x86)\\Google\\Chrome\\chromedriver\\chromedriver.exe"} 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":100, 
                     "print_urls":True,  
                     "size": "medium",
                     "chromedriver":"C:\\Program Files (x86)\\Google\\Chrome\\chromedriver\\chromedriver.exe"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
# creating object 
response = google_images_download.googleimagesdownload()  
  
search_queries = ['world map']
  
# Driver Code 0
for query in search_queries: 
    downloadimages(query)  
    print()  

