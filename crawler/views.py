# we will importing these for web-crawling
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
# ..........
# for showing popup messages in case of any error.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # BuiltIn User model
from django.shortcuts import redirect, render
# BuiltIn generic view read documentations
from django.views.generic import DetailView, ListView

from .forms import SearchForm  # Importing our search forms
from .models import Article  # Importing our models


def index(request):
    """ This is our index view, do nothing except showing a simple template."""
    return render(request, 'crawler/index.html')


@login_required  # decorator which will restrict the user for login.
def Search(request):
    """
    This view will take care of all our scraping functionality,
    This will render our search form
    Scrape the search date are show the given data in the form of list in this page.
    This function all take-care of Saving all the scrape date in the Datebase table named
    as Article.
    """
    if request.method == 'POST':
        # checking if the request is POST
        form = SearchForm(request.POST)
        if form.is_valid():

            # grabbing the enter data in the search box
            searched_item = form.cleaned_data['article']
            # ...........
            try:

                # selecting the website which will search for our result
                BASE_ARTICLE_URL = "https://arxiv.org/search/?query={}&searchtype=all&source=header"
                # ....

                # quote_plus is just joing the search item with BASE_ARTICLE_URL
                FINAL_URL = BASE_ARTICLE_URL.format(quote_plus(searched_item))
                # grabbing all the html in a variable with request module
                page = requests.get(FINAL_URL).content
                # ..........

                # Here scraping start with BeautifulSoup
                soup = BeautifulSoup(page, 'html.parser')
                ordered_list = soup.find('ol', {"class": 'breathe-horizontal'})

                list_item = ordered_list.findAll('li')

                num = 1
                for i in list_item[:50]:

                    title = i.find('p', {'class': "title is-5 mathjax"})
                    author = i.find('p', {'class': "authors"})
                    abstract = i.find('span',
                                      {"class":
                                       'abstract-full has-text-grey-dark mathjax'}
                                      )
                    pdf_link = i.find('span').find('a')
                    pdf_link = pdf_link.attrs['href']
                    date = i.find('p', {'class': 'is-size-7'})

                    num = num + 1
                    if title.text == None or author.text == None:
                        continue

                    if abstract == None or pdf_link == None:
                        continue

                    # creating the instance of our Article class to save the scraped date.
                    print("Article Number: ", num)
                    print('Title:', title.text)
                    print('Author: ', author.text.replace('\n', ' '))
                    print('Description: ', abstract.text)
                    print(pdf_link)
                    print(date.text.replace('\n', ' '))
                    # print("Article Detail:\t", comment)

                    print("-"*119)
                    print("-"*119)
                    a = Article.objects.create(
                        title=title.text, author=author.text,
                        abstract=abstract.text, pdf_link=pdf_link, date=date.text)
                    a.save()
                    print(abstract.text, author.text)
            except:
                messages.error(
                    request, "No result found! Please recheck your spelling and try again!")

            return redirect('/search')
    else:
        # if request is not post this will show a blank form
        form = SearchForm()

    # the query below this comment is first getting all the object than ordering all of them
    # According to the searched time and in last getting only the top 30 result for user.
    articles = Article.objects.all().order_by("-searched")[:50]

    context = {'forms': form, 'articles': articles}
    return render(request, 'crawler/search.html.', context)


class ArticleDetailView(DetailView):
    """ This will be show the detail of our scrape article."""
    model = Article
    template_name = 'crawler/detail.html'
    context_object_name = 'articles'
