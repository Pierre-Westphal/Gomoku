##
## EPITECH PROJECT, 2021
## Gomoku
## File description:
## Makefile
##

SRC	=	main.py

NAME	=	pbrain-gomoku-ai

all:	$(NAME)

$(NAME):
	@cp $(SRC) $(NAME)
	chmod +x $(NAME)

clean:
	@echo "done"

fclean:	clean
	@rm -f $(NAME)

re:	fclean	all