# ESA_API
Class Assignment 2 API

initialise the program by creating users:
  from db import userInsert
  userInsert("username","pasword","first_name","hash")
  
initialise the program by creating products:
  from db import productInert
  itemInsert("roductId","category","productName","productModel","availableQuantity","price")
  
 how to use the API?
 example program:
 
 step 1: run ws.py
 
 step 2:
 
        http://localhost:5000/addCart/{insert_username}/{insert_productID}/{insert_quantity} This link adds item to cart
        
        http://localhost:5000/editCart/{insert_username}/{insert_itemID}/{insert_quantity} This link edits an item which is already in cart
        
        http://localhost:5000/deleteCart/{insert_username}/{insert_itemID} This link deletes an item which is already in cart
        
         http://localhost:5000/products This link shows all items 
         
         http://localhost:5000/viewCart This link shows all items in cart
        
        
        
  
