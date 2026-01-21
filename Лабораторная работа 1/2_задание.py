# TODO Найдите количество книг, которое можно разместить на дискете
full_diskette_size_mb = 1.44
pages = 100
sheets = 50
quantity_symbols = 25
bytes_on_char = 4
bytes_in_kb = 1024
kb_to_mb = 1024

book_size_ = pages * sheets * quantity_symbols * bytes_on_char
diskette_size_bytes = full_diskette_size_mb * kb_to_mb * bytes_in_kb

books_count = int(diskette_size_bytes // book_size_)

print("Количество книг, помещающихся на дискету:", books_count)