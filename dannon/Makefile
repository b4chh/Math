NAME	=	301dannon

SRC	=	301dannon.py	\
		algorithms/selection_sort.py	\
		algorithms/insertion_sort.py	\
		algorithms/bubble_sort.py	\
		algorithms/merge_sort.py	\
		algorithms/quicksort.py

all:
	cp 301dannon.py $(NAME)
	chmod +x $(NAME)

fclean:	clean
	rm -f $(NAME)

re: fclean all

tests_run:

.PHONY: all tests_run clean fclean re