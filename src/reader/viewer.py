"""Functions for displaying the Real Python feed."""

# Standard library imports
from typing import List


def show(article: str) -> None:
    """Show one article."""
    print(article)


def show_list(site: str, titles: List[str]) -> None:
    """Show list of articles."""
    print(f"The latest tutorials from {site}") 
    # This is an f-string, a way to include expressions inside string literals for formatting
    for article_id, title in enumerate(titles):
        print(f"{article_id:>3} {title}")
    # This part of the f-string formats article_id. The > symbol is used for right-aligning the text. 
    # The number 3 specifies the minimum width for this part of the output, 
    # meaning that article_id will be printed with at least 3 characters wide, 
    # adding spaces to the left if article_id is less than 3 digits, ensuring alignment in the output.
