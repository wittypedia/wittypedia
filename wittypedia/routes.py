# external libraries :-
import os
import pickle
import requests

import urllib.parse
from flask import redirect, render_template, request
# from googletrans import Translator

# our own libraries
from wittypedia import app, db
from wittypedia.forms import *
from wittypedia.search import *
from wittypedia.scrape import *
from wittypedia.gen_tools import *
from wittypedia.translate import *
from wittypedia.models import *


@app.route('/', methods=['GET', 'POST'])
# @app.route('/index')
def index():
    form = TopicForm()

    if form.validate_on_submit():
        data = request.form.get('wiki_topic', default="")
        if "favicon" in data:
            ...
        else:
            return redirect(f"/search/{urllib.parse.quote(data)}")
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(err_msg)

    return render_template("index.html", form=form)

    # if form.validate_on_submit():
    #     flash('Login requested for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     # return redirect('/index')
    # return render_template('index.html', title='Sign In', form=form)


@app.route("/search/<wiki_topic>", methods=['GET', 'POST'])
def search(wiki_topic):
    # form = URLForm()
    search_results = search_wiki(wiki_topic, 10)
    sendable_results = search_results_fmt(search_results)
    return render_template("search_page.html", search_results=sendable_results)


@app.route("/<wiki_page_name>", methods=['GET', 'POST'])
def about_page(wiki_page_name):

    final_list = []
    form = LinkSearchForm()

    is_cached = Link.query.filter_by(wiki_topic=wiki_page_name).first()

    if is_cached:
        final_list = is_cached.wiki_links

    useless = Link.query.filter_by(wiki_topic="favicon.ico").first()
    if useless:
        Link.query.filter_by(wiki_topic="favicon.ico").delete()
        db.session.commit()

    # if f"{wiki_page_name}.dat" in os.listdir("wiki_files/"):
    #     if not wiki_page_name.startswith("favicon"):
    #         with open(f"wiki_files/{wiki_page_name}.dat", "rb") as f:
    #             final_list = pickle.load(f)
    else:

        URL = MAIN_WIKI_URL + wiki_page_name

        final_list = scrape_url(URL)
        final_list = setify_in_order(final_list)

        # with open(f"wiki_files/{wiki_page_name}.dat", "wb") as f:
        #     pickle.dump(final_list, f)
        new_link_added = Link(wiki_topic=wiki_page_name, wiki_links=final_list)
        db.session.add(new_link_added)
        db.session.commit()

    sendable_links = wiki_links_fmt(final_list)

    if form.validate_on_submit():
        linksearch_query = request.form.get('linksearch')
        linksearch_results = wiki_links_fmt(
            fuzzy_search(linksearch_query, final_list))
        return render_template("links_page.html",
                               links_list=linksearch_results,
                               form=form)
    else:

        return render_template("links_page.html",
                               links_list=sendable_links,
                               form=form)


# @app.route('/', defaults={'path': 'index'})
@app.route("/lang_<language>/<path:path>/", methods=['GET', 'POST'])
def languages(path, language):
    # print("----------------------\n", path)
    # page = f"/{path}"
    return translate_html(path, language)


@app.route("/random", methods=["GET", "POST"])
def random_page():
    rng_topic = randomize_topic()
    return redirect(f"/{rng_topic}")

@app.route("/show_images_<wiki_topic>/<path:path>", methods = ["GET", "POST"])
def image(wiki_topic, path):
    images_list = get_images(wiki_topic)
    formatted = []
    for i, j in enumerate(images_list):
        formatted.append((i + 1, wiki_topic, j))

    return render_template("images.html", images = formatted)
