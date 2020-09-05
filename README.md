# Django-book-store

Store the Book Details:

	Storing the following details associated with it.
		Hint: # indicates Model name under the particular app
	- Book app
		#Book
			* title
			* book_type
				-ebook
				-paperback
				-hardbound
			* isbn
				- ebook_isbn ----> to be added as model formset in form... should be dymnamically updated as per type in form
				- print_isbn ----> to be added as model formset in form... should be dymnamically updated
			* pages
			* summary        
			* language			
			* genre		 | (many to many)		
			* author 	 | (many to many)
			* publisher  | (one to many)

		#Cost
		    * book  	 | (one to many)
		    * cost
		    	- ebook cost ----> to be added | should be auto populated as per selection in isbn type
		    	- paperback cost ----> to be added
		    	- hardbound cost ----> to be added
		    	
		#Language 
			* name
		#Genre    
			* name

			
	- Author app
		#Author
			*  name
			*  country

	- Publisher app
		#District
			* state
			* district
		#State
			* country
			* state
		#Country
			* country
			* code
			* phone_code
			* currency_code
			* currency_symbol			
		#Publisher
			*  name
			*  address_line
			*  city
			*  district
			*  state
			*  country
			*  pincode
