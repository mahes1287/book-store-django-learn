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
			summary
			language
			* publisher  | (one to many)
			* author 	 | (one to many)

		#Cost
		    * book  	 | (one to many)
		    * cost
		    	- ebook cost ----> to be added
		    	- print version cost ----> to be added

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

genre app
