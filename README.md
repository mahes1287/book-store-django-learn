# Django-book-store

Store the Book Details:

	Storing the following details associated with it.
		Hint: # indicates Model name under the particular app
	- Book app
		#Book
			* name
			* isbn
				- ebook_isbn ----> to be added
				- print_isbn ----> to be added
			* pages
			* summary        -----> need to be connected
			* language		-----> need to be connected	
			* genre			-----> need to be connected
			* publisher  | (one to many)
			* author 	 | (one to many)

		#Cost
		    * book  	 | (one to many)
		    * cost
		    	- ebook cost ----> to be added
		    	- print version cost ----> to be added
		#Language -----> need to be implemented
		#Genre    -----> need to be implemented

	- Author app
		#Author
			*  name
			*  country

	- Publisher app
		#Publisher
			*  name
			*  address_line
			*  city
			*  state
			*  country
			*  pincode
